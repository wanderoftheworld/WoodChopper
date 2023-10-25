#!/usr/bin/env python3

from collections import deque
import random
import socket
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

import threading 

# stores tuple (sender_id, message)
msgs = deque()
 
class ClientThread(threading.Thread): 
    def __init__(self, thread_id, socket): 
        threading.Thread.__init__(self) 
        self.thread_id = thread_id
        self.socket = socket
 
    # helper function to execute the threads
    def run(self): 
        print('Starting thread:', self.thread_id)
        with self.socket:
            while True:
                data = self.socket.recv(1024)
                if not data:
                    break
                # server should forward this data to other open connections
                # sync mechanism TODO
                msgs.append((self.thread_id, data))
            print('Existing thread:', self.thread_id)

class MulticastThread(threading.Thread):
    # dictionary from thread name to reference of a socket
    def __init__(self, client_threads):
        threading.Thread.__init__(self)
        self.client_threads = client_threads

    def cleanup_threads(self):
        for thread_id, ct in self.client_threads.items():
            if not ct.is_alive():
                self.client_threads.pop(thread_id)

    def run(self):
        print('Watching message queue...')
        while True:
            if not msgs:
                self.cleanup_threads()
                time.sleep(0.1)
                continue
            # TODO: sync to protect r/w to msgs??
            sender_id, m = msgs.popleft()
            for thread_id, ct in self.client_threads.items():
                if thread_id == sender_id:
                    continue
                ct.socket.sendall(m)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    # dict key: thread id, val: thread object ref
    client_threads = dict()
    ft = MulticastThread(client_threads)
    ft.start()

    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        id = 0
        while id in client_threads:
            # No more than 2000 ppl in a chat group
            id = random.randint(0, 2000)
        ct = ClientThread(id, conn)
        ct.start()
        client_threads[id] = ct

