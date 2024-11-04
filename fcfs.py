def calculate_times(processes, arrival_time, burst_time):
    n = len(processes)

    # Initialize arrays for completion, turn around, and waiting times
    completion_time = [0] * n
    turn_around_time = [0] * n
    waiting_time = [0] * n

    # Initialize variables to store total waiting time and turn around time
    total_tat = 0
    total_wt = 0

    # Sort processes by arrival time (FCFS Scheduling)
    sorted_indices = sorted(range(n), key=lambda i: arrival_time[i])

    # Sort the processes, arrival times, and burst times based on sorted_indices
    #sorted_processes = [processes[i] for i in sorted_indices]
    sorted_arrival_time = [arrival_time[i] for i in sorted_indices]
    sorted_burst_time = [burst_time[i] for i in sorted_indices]

    # Completion Time calculation for each process
    for i in range(n):
        if i == 0:
            completion_time[i] = sorted_arrival_time[i] + sorted_burst_time[i]
        else:
            if sorted_arrival_time[i] > completion_time[i - 1]:
                completion_time[i] = sorted_arrival_time[i] + sorted_burst_time[i]
            else:
                completion_time[i] = completion_time[i - 1] + sorted_burst_time[i]

        # Turn Around Time (TAT) = Completion Time - Arrival Time
        turn_around_time[i] = completion_time[i] - sorted_arrival_time[i]

        # Waiting Time (WT) = Turn Around Time - Burst Time
        waiting_time[i] = turn_around_time[i] - sorted_burst_time[i]

        # Add to total turn around and waiting time
        total_tat += turn_around_time[i]
        total_wt += waiting_time[i]

    # Calculate average Turn Around Time and Waiting Time
    avg_tat = total_tat / n
    avg_wt = total_wt / n

    # Output the results with improved formatting
    print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Completion':<15}{'TurnAround':<15}{'Waiting':<10}")
    for i in range(n):
        print(f"{sorted_processes[i]:<10}{sorted_arrival_time[i]:<10}{sorted_burst_time[i]:<10}"
              f"{completion_time[i]:<15}{turn_around_time[i]:<15}{waiting_time[i]:<10}")

    print(f"\nAverage Turn Around Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

# Input data
processes = ["P0", "P1", "P2", "P3"]
arrival_time = [0, 2, 1, 3]
burst_time = [5, 3, 8, 6]

# Call the function with the provided data
calculate_times(processes, arrival_time, burst_time)
