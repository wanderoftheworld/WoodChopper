There are 2 runnables in this folder: auth server and proxy server. The
auth server in this folder should behave the same as the Python version
provided at https://github.com/basetenlabs/interview-questions/tree/main/authz 

You ought to start the auth server first: cd auth_server/:
$ go run main.go
2023/08/04 15:23:24 Server listening on port 8090

Then start the proxy server: cd proxy_server/:
$ go run main.go auth_client.go 
2023/08/04 15:47:04 Server listening on port 8080

Then send a few http requests to the proxy server:
A 'happy' request:
    `curl -X POST  -H "Authorization: api_key_1" http://localhost:8080/workload/workload1/invoke`

A not-so-happy request (incorrect API key)
    `curl -X POST -i -H "Authorization: apikey_1" http://localhost:8080/workload/workload1/invoke`

Coding decisions:
1. Why auth_client.go
auth_client.go defines an interface and 2 different structs implement that interface. This is
to make code more testable. i.e. in order to test the proxy server's HTTP handler, I want to
avoid having to run a real auth server: AuthFakeClient is easy to maintain and inject into
proxy server's HTTP handler

2. Why type Cache
There are quite a number of open sources libs that implement in memory caches. Since I'm solving
an interview problem, I thought my audience might want to see me writing a cache from 'scratch'.
The implementation only meets the basic requirement, it's missing features such as evict
strategy/TTL, sharding etc.

Mutex is used to make update/access of cache threadsafe: Go's net/http uses 1 goroutine (concepturally corresponds to a thread) for processing 1 http request: we must ensure that concurrent cache update/access are protected.

3. Why type ProxyServer
There is not much logic associate to the struct - I just find having a struct to contain
all dependencies that ought be initialized to start the server makes code more readable.

TODO: write code to proxy workload invocation
TODO: auth_client can use unit tests
