package main

import (
  "net/http"
  "net/http/httptest"
  "testing"
)

func TestInvokeWorkloadHandlerForbidden(t *testing.T) {
	req := httptest.NewRequest(http.MethodGet, "/workload/workload_foo/invoke", nil)
	w := httptest.NewRecorder()

  temp := InitAuthFakeClient()
  server := ProxyServer{authClient: &temp, cache: &Cache{v: make(map[string][]string)}}
	invokeWorkloadHandler := newInvokeHandler(&server)
  invokeWorkloadHandler(w, req)
  res := w.Result()
  defer res.Body.Close()

  if res.StatusCode != http.StatusUnauthorized {
    t.Errorf("Expected http status Unauthorized, but got %d", res.StatusCode)
  }
}

// TODO: add more test: a happy path; an invalid API key etc.