import threading

def printNumber(number):
    print('Ho!', number)

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.sem_zero = threading.Semaphore(1)
        self.sem_even = threading.Semaphore(0)
        self.sem_odd = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i < self.n:
            self.sem_zero.acquire()
            printNumber(0)
            self.i += 1
            if self.i % 2 == 0:
                self.sem_even.release()
            else:
                self.sem_odd.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.sem_even.acquire()
            printNumber(self.i)
            self.sem_zero.release()
            if self.i == self.n or self.i+1 == self.n:
                return

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.sem_odd.acquire()
            printNumber(self.i)
            self.sem_zero.release()
            if self.i == self.n or self.i+1 == self.n:
                return

def main():
    zero_even_odd = ZeroEvenOdd(1)
    thread_zero = threading.Thread(target=zero_even_odd.zero, args=(print,))
    thread_even = threading.Thread(target=zero_even_odd.even, args=(print,))
    thread_odd = threading.Thread(target=zero_even_odd.odd, args=(print,))
    thread_zero.start()
    thread_even.start()
    thread_odd.start()
    thread_zero.join()
    thread_even.join()
    thread_odd.join()

if __name__ == "__main__":
    main()
