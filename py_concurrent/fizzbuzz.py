import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.done = False
        self.cv_fizz = threading.Semaphore(0)
        self.cv_buzz = threading.Semaphore(0)
        self.cv_fizzbuzz = threading.Semaphore(0)
        self.cv_number = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.cv_fizz.acquire()
            if self.done:
                return
            printFizz()
            self.cv_number.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.cv_buzz.acquire()
            if self.done:
                return
            printBuzz()
            self.cv_number.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.cv_fizzbuzz.acquire()
            if self.done:
                return
            printFizzBuzz()
            self.cv_number.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.cv_number.acquire()
            if i % 3 == 0 and i % 5 == 0:
                print('Get fizzbuzz')
                self.cv_fizzbuzz.release()
            elif i % 3 == 0:
                print('Get fizz')
                self.cv_fizz.release()
            elif i % 5 == 0:
                print('Get buzz')
                self.cv_buzz.release()
            else:
                printNumber(i)
                self.cv_number.release()
        self.done = True
        self.cv_fizz.release()
        self.cv_buzz.release()
        self.cv_fizzbuzz.release()

def printFizz():
    print('fizz')

def printBuzz():
    print('buzz')

def printFizzBuzz():
    print('fizzbuzz')

def printNumber(i):
    print(i)

# Create four threads
fb = FizzBuzz(5)
thread1 = threading.Thread(target=fb.fizz, args=(printFizz,))
thread2 = threading.Thread(target=fb.buzz, args=(printBuzz,))
thread3 = threading.Thread(target=fb.fizzbuzz, args=(printFizzBuzz,))
thread4 = threading.Thread(target=fb.number, args=(printNumber,))

# Start all four threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
