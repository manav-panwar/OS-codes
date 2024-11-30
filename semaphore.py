import threading
import time

# Semaphores and variables
read_count = 0
read_count_mutex = threading.Semaphore(1)  # Protects read_count
resource_mutex = threading.Semaphore(1)    # Ensures mutual exclusion for writers
iterations = 5  # Number of times readers/writers can access the resource
terminate_flag = False

# Reader function
def reader(reader_id):
    global read_count, terminate_flag
    for _ in range(iterations):
        if terminate_flag:
            break

        # Entry section for readers
        read_count_mutex.acquire()
        read_count += 1
        if read_count == 1:  # First reader locks the resource
            resource_mutex.acquire()
        read_count_mutex.release()

        # Critical section for readers
        print(f"Reader {reader_id} is reading the resource.")
        time.sleep(1)  # Simulate reading time

        # Exit section for readers
        read_count_mutex.acquire()
        read_count -= 1
        if read_count == 0:  # Last reader unlocks the resource
            resource_mutex.release()
        read_count_mutex.release()

        # Simulate time between reading
        time.sleep(2)

# Writer function
def writer(writer_id):
    global terminate_flag
    for _ in range(iterations):
        if terminate_flag:
            break

        # Entry section for writers
        resource_mutex.acquire()

        # Critical section for writers
        print(f"Writer {writer_id} is writing to the resource.")
        time.sleep(2)  # Simulate writing time

        # Exit section for writers
        resource_mutex.release()

        # Simulate time between writing
        time.sleep(3)

# Main function to start threads
if __name__ == "__main__":
    # Create reader and writer threads
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

    # Start the threads
    for r in readers:
        r.start()
    for w in writers:
        w.start()

    # Wait for threads to finish
    for r in readers:
        r.join()
    for w in writers:
        w.join()

    # Set termination flag
    terminate_flag = True

    print("Program completed.")
