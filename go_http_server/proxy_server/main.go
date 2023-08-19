package main

import (
	"log"
	"net/http"
	"strings"
	"sync"

	"github.com/gorilla/mux"
	"golang.org/x/exp/slices"
)

const Port = "8080"
const AuthBackend = "http://localhost:8090"
const AuthHeaderName = "Authorization"
const AuthzPathSegment = "/authorization/"

// Simple caching mechanism: API key being map key (no TTL, no sharding)
type Cache struct {
	mu sync.RWMutex
	v  map[string][]string
}

func (c *Cache) InsertUpdate(key string, v []string) {
	c.mu.Lock()
	// Lock so only one goroutine at a time can access the cache.
	c.v[key] = v
	c.mu.Unlock()
}

func (c *Cache) Get(key string) []string {
	c.mu.Lock()
	// Lock so only one goroutine at a time can access the cache.
	defer c.mu.Unlock()
	return c.v[key]
}

// Define a type to house dependencies needed by this HTTP server.
type ProxyServer struct {
    cache *Cache
    authClient AuthInterface
}

func main() {
	r := mux.NewRouter()
	temp := InitAuthHTTPClient()
    server := ProxyServer{authClient: &temp, cache: &Cache{v: make(map[string][]string)}}

	r.HandleFunc("/workload/{workload_id}/invoke", newInvokeHandler(&server)).Methods("POST")

	log.Printf("Server listening on port %v", Port)
	log.Fatal(http.ListenAndServe(":"+Port, r))
}

func getApiKeyFromHttpRequest(in *http.Request) string {
    for name, headers := range in.Header {
		if name == AuthHeaderName {
			// There should just be just 1 value
			for _, h := range headers {
				log.Printf("%v: %v\n", name, h)
				return h
			}
		}
	}
    return ""
}

func newInvokeHandler(s *ProxyServer) http.HandlerFunc {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        api_key := getApiKeyFromHttpRequest(r)
        if api_key == "" {
            w.WriteHeader(http.StatusUnauthorized)
            return
        }
        // Get workload id out of URL: <host>/workload/<workload-id>/invoke
        segments := strings.Split(r.URL.Path, "/")
        workload_id := segments[2]
        authorized := false

        value := s.cache.Get(api_key)
        if value == nil {
            // `api_key` does not exist in cache. Make a request to Auth backend
            username := s.authClient.Authn(api_key)
            if username == "" {
                w.WriteHeader(http.StatusUnauthorized)
                return
            }
            authorized_workloads := s.authClient.Authz(username)
            // Add into cache
            s.cache.InsertUpdate(api_key, authorized_workloads)
            log.Printf("User %s, authz returned %s", username, authorized_workloads)
            if slices.Contains(authorized_workloads, workload_id) {
                authorized = true
            }
        } else {
            // The key exists and the value is stored in the `value` variable.
            if slices.Contains(value, workload_id) {
                authorized = true
            }
        }

        if !authorized {
            w.WriteHeader(http.StatusForbidden)
            w.Write([]byte("Caller is not authorized to invoke this payload"))
        } else {
            // Requirement is unclear:
            // There could be another Baseten server that coordinates workload
            // invocation; or we could hit AWS/GCP API?
            // If the former, no auth is needed from this auth server; if the
            // latter, a Baseten-created API key might be used for the Cloud service
            // to know that it is Baseten calling - to passThe auth between proxy server and the service that can actually
            // invoke workload can be API key.
            // In both cases, it might be a good idea to have an interface WorkloadClient
            // to hide the differences in request/header mapping
            w.Write([]byte("Invoking workload"))
        }
    })
}


