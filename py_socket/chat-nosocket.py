import threading

def chat_window_one(other=None):
    from os import system, name
    if name == 'nt':
        system("cls")    # for windows
    else:
        system("clear")  # for mac and linux

    print("Window One:")
    print("Enter username:")
    username = input(">> ")

    while True:
        message = input("{}> ".format(username))
        if message:
            other.write(message + "\n")

def chat_window_two(other=None):
    from os import system, name
    if name == 'nt':
        system("cls")    # for windows
    else:
        system("clear")  # for mac and linux

    print("Window Two:")
    print("Enter username:")
    username = input(">> ")

    while True:
        message = other.read()
        if message:
            print("{}: {}".format(username, message))

other = threading.local()
other.write = chat_window_one.write
other.read = chat_window_two.read

t1 = threading.Thread(target=chat_window_one, args=(other,))
t2 = threading.Thread(target=chat_window_two, args=(other,))
t1.start()
t2.start()
