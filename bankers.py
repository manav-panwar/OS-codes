# Banker's Algorithm in Python

def is_safe_state(processes, available, max_need, allocation):
    num_processes = len(processes)
    num_resources = len(available)

    # Calculate the need matrix
    need = [[max_need[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]
    
    # Work array to keep track of available resources
    work = available[:]
    finish = [False] * num_processes  # Tracks if a process is finished
    safe_sequence = []  # Stores the safe sequence if found

    # Check for a safe sequence
    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                # Process can be completed
                for j in range(num_resources):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(processes[i])
                found = True

        if not found:  # No further process can be safely executed
            return False, []

    return True, safe_sequence

# Banker's Algorithm main function
def bankers_algorithm(processes, available, max_need, allocation, request, process_id):
    num_resources = len(available)

    # Check if the request can be granted
    if all(request[j] <= max_need[process_id][j] - allocation[process_id][j] and request[j] <= available[j] for j in range(num_resources)):
        # Tentatively allocate the resources
        available = [available[j] - request[j] for j in range(num_resources)]
        allocation[process_id] = [allocation[process_id][j] + request[j] for j in range(num_resources)]

        # Check if the new state is safe
        safe, safe_sequence = is_safe_state(processes, available, max_need, allocation)
        if safe:
            print("Request can be granted.")
            print("Safe Sequence:", safe_sequence)
            return True
        else:
            print("Request cannot be granted as it leads to an unsafe state.")
            # Rollback allocation
            available = [available[j] + request[j] for j in range(num_resources)]
            allocation[process_id] = [allocation[process_id][j] - request[j] for j in range(num_resources)]
            return False
    else:
        print("Request exceeds the available resources or maximum claim.")
        return False


# Example Usage
if __name__ == "__main__":
    # Input example
    processes = [0, 1, 2, 3, 4]  # Process IDs
    available = [3, 3, 2]  # Available resources (A, B, C)
    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3],
    ]  # Maximum demand of resources for each process
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2],
    ]  # Currently allocated resources to processes
    request = [1, 0, 2]  # Resource request by a process
    process_id = 1  # ID of the process making the request

    # Run the Banker's Algorithm
    bankers_algorithm(processes, available, max_need, allocation, request, process_id)
