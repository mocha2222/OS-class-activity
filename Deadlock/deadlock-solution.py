import threading
import time

class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.lock = threading.Lock()

acc1 = Account(1, 1000)
acc2 = Account(2, 1000)

def transfer_deadlock(from_acc, to_acc, amount):
    print(f"{threading.current_thread().name} locking {from_acc.id}")
    from_acc.lock.acquire()
    time.sleep(1)
    print(f"{threading.current_thread().name} locking {to_acc.id}")
    to_acc.lock.acquire()     # <-- DEADLOCK HAPPENS HERE

    from_acc.balance -= amount
    to_acc.balance += amount

    to_acc.lock.release()
    from_acc.lock.release()

def thread1_deadlock():
    transfer_deadlock(acc1, acc2, 100)

def thread2_deadlock():
    transfer_deadlock(acc2, acc1, 200)

t1 = threading.Thread(target=thread1_deadlock, name="T1-deadlock")
t2 = threading.Thread(target=thread2_deadlock, name="T2-deadlock")

print("\n=== RUNNING DEADLOCK EXAMPLE ===")
t1.start()
t2.start()
t1.join(timeout=3)
t2.join(timeout=3)
print("Deadlock occurred (program froze above).")

def transfer_fixed(from_acc, to_acc, amount):
    # APPLY THE FIRST PHOTO (ORDERED LOCKING)
    # Always lock smaller ID first
    first = from_acc if from_acc.id < to_acc.id else to_acc
    second = to_acc if from_acc.id < to_acc.id else from_acc

    print(f"{threading.current_thread().name} locking {first.id}")
    first.lock.acquire()
    time.sleep(0.5)
    print(f"{threading.current_thread().name} locking {second.id}")
    second.lock.acquire()

    from_acc.balance -= amount
    to_acc.balance += amount

    second.lock.release()
    first.lock.release()

def thread1_fixed():
    transfer_fixed(acc1, acc2, 100)

def thread2_fixed():
    transfer_fixed(acc2, acc1, 200)

t3 = threading.Thread(target=thread1_fixed, name="T1-fixed")
t4 = threading.Thread(target=thread2_fixed, name="T2-fixed")

print("\n=== RUNNING FIXED VERSION (NO DEADLOCK) ===")
t3.start()
t4.start()
t3.join()
t4.join()

print("\nSolution finished — no deadlock.")