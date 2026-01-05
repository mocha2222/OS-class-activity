from threading import Semaphore, Thread
import time

a = Semaphore(1)
b = Semaphore(0)
c = Semaphore(0)

def process1():
    a.acquire()
    print("H")
    print("E")
    b.release()

def process2():
    b.acquire()
    print("L")
    c.release()

def process3():
    c.acquire()
    print("L")
    print("O")


if __name__ == "__main__":
    p1 = Thread(target=process1)
    p2 = Thread(target=process2)
    p3 = Thread(target=process3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()