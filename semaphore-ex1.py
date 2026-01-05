import threading
import time
import random

particle_buffer = []

mutex = threading.Semaphore(1)
empty = threading.Semaphore(50)
full = threading.Semaphore(0)

def producer(producer_id):
    global particle_buffer
    pair_num = 0
    while True:
        time.sleep(random.uniform(0.1, 0.3))
        pair_num += 1
        p1 = f"P{producer_id}-{pair_num}a"
        p2 = f"P{producer_id}-{pair_num}b"

        print(f"Producer {producer_id}: Produced pair ({p1}, {p2})")

        empty.acquire()
        mutex.acquire()

        particle_buffer.append(p1)
        particle_buffer.append(p2)

        mutex.release()
        full.release()

def consumer():
    global particle_buffer
    while True:
        full.acquire()
        mutex.acquire()

        p1 = particle_buffer.pop(0)
        p2 = particle_buffer.pop(0)

        mutex.release()
        empty.release()

        time.sleep(random.uniform(0.15, 0.25))
        print(f"Consumer: Packaged and shipped ({p1}, {p2})")

if __name__ == "__main__":
    num_producers = 3

    consumer_thread = threading.Thread(target=consumer, daemon=True)
    consumer_thread.start()

    producer_threads = []
    for i in range(num_producers):
        t = threading.Thread(target=producer, args=(i + 1,), daemon=True)
        t.start()
        producer_threads.append(t)

    try:
        time.sleep(10)
        print("\n=== Simulation Complete ===")
    except KeyboardInterrupt:
        print("\n=== Interrupted ===")
