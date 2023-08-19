package main

import (
	"log"
	"net/http"
	"strings"

	"github.com/gorilla/mux"
)

const Port = "8090"
const AuthHeaderName = "Authorization"
const AuthzPathSegment = "/authorization/"

// Golang does not support const map.
func getUsernameByApiKey(key string) string {
	theMap := map[string]string{
		"api_key_1": "user1",
		"api_key_2": "user2",
	}

	return theMap[key]
}

func getWorkloadsByUser(username string) []string {
	theMap := map[string][]string{
		"user1": {"workload1", "workload2"},
		"user2": {"workload3"},
	}

	return theMap[username]
}

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/auth", authenticate).Methods("GET")
	r.HandleFunc(AuthzPathSegment + "{username}", authz).Methods("GET")

	log.Printf("Server listening on port %v", Port)
	log.Fatal(http.ListenAndServe(":"+Port, r))
}

func authenticate(w http.ResponseWriter, r *http.Request) {
	var username string
	for name, headers := range r.Header {
		if name == AuthHeaderName {
			for _, api_key := range headers {
				username = getUsernameByApiKey(api_key)
			}
		}
	}
	log.Printf("This request was identified as `%s`", username)
    if username != "" {
	    w.Write([]byte(username))
    } else {
        w.WriteHeader(http.StatusUnauthorized)
        w.Write([]byte("Invalid API key"))
    }
}

// Returns empty payload if the given user has no workloads.
func authz(w http.ResponseWriter, r *http.Request) {
	log.Printf("Received request %v", r.URL)
	username := r.URL.Path[len(AuthzPathSegment):]
    log.Printf("Parsed to username %s", username)
	workloads := getWorkloadsByUser(username)
    if workloads != nil {
	    w.Write([]byte(strings.Join(workloads, ",")))
    } else {
        w.WriteHeader(http.StatusForbidden)
        w.Write([]byte("User not found"))
    }
}
