package main

import (
	"fmt"
	"sync"
	"time"
)

const TTL = 5
// Simple caching mechanism: API key being map key (no TTL, no sharding)
type CacheEntry struct {
	workloads [] string
	inserted time.Time
}
type Cache struct {
  mu sync.RWMutex
  v  map[string]CacheEntry
}

func (c *Cache) InsertUpdate(key string, v []string, done chan bool) {
  // Acquire lock to block other writers or readers.
	c.mu.Lock()
  c.v[key] = CacheEntry{workloads:v, inserted:time.Now()}
	// Add intentional delay to facilitate testing
	if done != nil {
		done <- true
		time.Sleep(TTL)
	}
  c.mu.Unlock()
}

func (c *Cache) GetAndCleanMaybe(key string) ([]string, bool) {
	// This func may trigger mutation, so we acquire a rw lock
  c.mu.Lock()
	value, expired := c.get(key)
	if (expired) {
		delete(c.v, key)
	}
	c.mu.Unlock()
  return value, expired
}

func (c *Cache) get(key string) ([]string, bool) {
	value, exists := c.v[key]
  expired := false
  if (exists) {
    // check if the item has RemoveExpired
    if time.Now().After(value.inserted.Add(TTL)) {
      delete(c.v, key)
      expired = true
    }
	}
	return value.workloads, expired
}

func (c *Cache) Get(key string) ([]string, bool) {
	c.mu.RLock()
	defer c.mu.RUnlock()
	return c.get(key)
}

func main() {
  cache := Cache{
    v: make(map[string]CacheEntry),
  }

	// Start 3 goroutines: 1 writer, 2 readers
	// Verify that readers cannot read until writer finishes.
	var wg sync.WaitGroup
  // Use chan to enforce an order that writer starts before readers assert
	done := make(chan bool)
	wg.Add(1)
	go func() {
		defer wg.Done()
		cache.InsertUpdate("key1", []string{"value1", "value2"}, done)
	}()
	<- done

	// The 2 readers: 1 of them will trigger data deletion, depending on order
	// of execution, you could see 2 different outputs:
	//    Data from cache: [value1 value2]
	//    Data from cache: [value1 value2]
	// or:
	//    Data from cache: [value1 value2]
	//.   Data from cache: []
	wg.Add(1)
	go func() {
		defer wg.Done()
		data, expired := cache.Get("key1")
		fmt.Println("Data from cache:", data)
		// No go.mod? assert(true, expired)
		if len(data) > 0 && !expired {
			fmt.Println("Concurrency PROBLEM: read should have waited")
		}
	}()
	wg.Add(1)
	go func() {
		defer wg.Done()
		data, expired := cache.GetAndCleanMaybe("key1")
    fmt.Println("Data from cache:", data)
    // No go.mod? assert(true, expired)
    if len(data) > 0 && !expired {
      fmt.Println("Concurrency PROBLEM: read should have waited")
    }
	}()
	wg.Wait()
}
