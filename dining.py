import threading
import time

# Number of philosophers (and forks)
NUM_PHILOSOPHERS = 5

# Semaphore for each fork
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

# Semaphore to ensure at most (n-1) philosophers can eat at the same time (to prevent deadlock)
max_diners = threading.Semaphore(NUM_PHILOSOPHERS - 1)

# Philosopher function
def philosopher(philosopher_id):
    while True:
        # Thinking
        print(f"Philosopher {philosopher_id} is thinking.")
        time.sleep(1)

        # Trying to pick up forks
        max_diners.acquire()  # Ensure at most (n-1) philosophers are dining
        forks[philosopher_id].acquire()  # Pick up left fork
        forks[(philosopher_id + 1) % NUM_PHILOSOPHERS].acquire()  # Pick up right fork

        # Eating
        print(f"Philosopher {philosopher_id} is eating.")
        time.sleep(2)

        # Putting down forks
        forks[(philosopher_id + 1) % NUM_PHILOSOPHERS].release()  # Put down right fork
        forks[philosopher_id].release()  # Put down left fork
        max_diners.release()  # Allow another philosopher to dine

        # Back to thinking
        time.sleep(1)

# Main function to start the simulation
if __name__ == "__main__":
    # Create threads for philosophers
    philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]

    # Start all philosopher threads
    for p in philosophers:
        p.start()

    # Join threads (optional, as this simulates an infinite loop)
    for p in philosophers:
        p.join()
