import pandas as pd

def sjf_scheduling(burst_time, arrival_time, preemptive=False):
    n = len(burst_time)
    completed = [False] * n
    completion_time = [0] * n
    remaining_time = burst_time[:]
    current_time = 0
    finished_processes = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    while finished_processes < n:
        # Find the index of the process to execute next
        idx = -1
        shortest_time = float('inf')
        
        for i in range(n):
            if (arrival_time[i] <= current_time and not completed[i]):
                if preemptive:
                    if remaining_time[i] < shortest_time:
                        shortest_time = remaining_time[i]
                        idx = i
                else:
                    if burst_time[i] < shortest_time:
                        shortest_time = burst_time[i]
                        idx = i
        
        if idx == -1:
            current_time += 1
            continue
        
        if preemptive:
            # Execute the process for 1 unit of time
            remaining_time[idx] -= 1
            if remaining_time[idx] == 0:
                completed[idx] = True
                finished_processes += 1
                completion_time[idx] = current_time + 1
        else:
            # Non-preemptive SJF: complete the process in one go
            completed[idx] = True
            finished_processes += 1
            completion_time[idx] = current_time + burst_time[idx]
            current_time += burst_time[idx]
            continue
        
        current_time += 1
    
    # Calculate Turnaround Time and Waiting Time
    turnaround_time = [completion_time[i] - arrival_time[i] for i in range(n)]
    waiting_time = [turnaround_time[i] - burst_time[i] for i in range(n)]
    
    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n
    
    # Create a dataframe with the important columns
    df = pd.DataFrame({
        'Process': [f'P{i+1}' for i in range(n)],
        'Arrival Time': arrival_time,
        'Burst Time': burst_time,
        'Completion Time': completion_time,
        'Turnaround Time': turnaround_time,
        'Waiting Time': waiting_time
    })
    
    return df, avg_tat, avg_wt

# Process data
burst_time = [6, 2, 8, 3, 4]
arrival_time = [2, 5, 1, 0, 4]

# Calculate for Preemptive SJF
df_preemptive, avg_tat_preemptive, avg_wt_preemptive = sjf_scheduling(burst_time, arrival_time, preemptive=True)

# Calculate for Non-preemptive SJF
df_non_preemptive, avg_tat_non_preemptive, avg_wt_non_preemptive = sjf_scheduling(burst_time, arrival_time, preemptive=False)

# Output results
print("Preemptive SJF:")
print(df_preemptive)
print(f"Average Turnaround Time: {avg_tat_preemptive}")
print(f"Average Waiting Time: {avg_wt_preemptive}")

print("\nNon-preemptive SJF:")
print(df_non_preemptive)
print(f"Average Turnaround Time: {avg_tat_non_preemptive}")
print(f"Average Waiting Time: {avg_wt_non_preemptive}")
