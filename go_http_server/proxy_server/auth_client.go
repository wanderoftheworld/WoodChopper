package main

import (
    "io"
    "log"
    "net/http"
    "strings"
    "time"
)

type AuthInterface interface {
    Authn(api_key string) string
    Authz(username string) []string
}

// AuthClient implements AuthInterface: it makes HTTP calls to a server.
type AuthHTTPClient struct {
  httpClient *http.Client
}

func InitAuthHTTPClient() AuthHTTPClient {
    // Keep warm connections to backends
	tr := &http.Transport{
		MaxIdleConns:       10,
		IdleConnTimeout:    30 * time.Second,
		DisableCompression: true,
	}
	return AuthHTTPClient{httpClient: &http.Client{Transport: tr}}
}

// Returns "" if Auth Server cannot recognize the given api key 
func (x *AuthHTTPClient) Authn(api_key string) string {
	req, err := http.NewRequest("GET", AuthBackend+"/auth", nil)
	if err != nil {
		log.Fatalf("Failed to create HTTP request: %v", err)
	}
	req.Header.Set(AuthHeaderName, api_key)

	resp, err2 := x.httpClient.Do(req)
	if err2 != nil {
		log.Fatalf("Authn failed: %v", err2)
	}
    if resp.StatusCode != http.StatusOK {
        return ""
    }

	defer resp.Body.Close()
    // Take username out of response body
    responseData, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
    responseString := string(responseData)
    log.Printf("Authn says this request was identified as `%s`", responseString)
    return responseString
}

func (x *AuthHTTPClient) Authz(username string) []string {
	resp, err := x.httpClient.Get(AuthBackend + AuthzPathSegment + username)
	if err != nil {
		log.Fatalf("Authz failed: %v", err)
	}
    if resp.StatusCode != http.StatusOK {
        return nil
    }

	defer resp.Body.Close()
	// Take workload ids out of response body
	responseData, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	responseString := string(responseData)
	return strings.Split(responseString, ",")
}

// AuthFakeClient implements AuthInterface: it fakes responses
type AuthFakeClient struct {
    apiKeyToUserName map[string]string
    userNameToWorkloads map[string][]string
}

func InitAuthFakeClient() AuthFakeClient {
	return AuthFakeClient{apiKeyToUserName: make(map[string]string), userNameToWorkloads: make(map[string][]string)}
}

func (x *AuthFakeClient) Authn(api_key string) string {
	return x.apiKeyToUserName[api_key]
}

func (x *AuthFakeClient) Authz(username string) []string {
    return x.userNameToWorkloads[username]
}