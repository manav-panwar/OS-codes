import pandas as pd

def priority_scheduling(burst_time, priority):
    n = len(burst_time)
    processes = [{"id": f"P{i+1}", "burst_time": burst_time[i], "priority": priority[i]} for i in range(n)]
    
    # Sort processes by priority (lower number indicates higher priority)
    processes.sort(key=lambda x: x["priority"])
    
    # Initialize tracking variables
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0

    # Calculate Completion Time, Turnaround Time, and Waiting Time
    for i, process in enumerate(processes):
        current_time += process["burst_time"]
        completion_time[i] = current_time
        turnaround_time[i] = completion_time[i]  # Since arrival time is 0 for all
        waiting_time[i] = turnaround_time[i] - process["burst_time"]

    # Average Turnaround Time and Waiting Time
    avg_turnaround_time = sum(turnaround_time) / n
    avg_waiting_time = sum(waiting_time) / n

    # Create a DataFrame with process details
    df = pd.DataFrame({
        'Process': [process['id'] for process in processes],
        'Burst Time': [process['burst_time'] for process in processes],
        'Priority': [process['priority'] for process in processes],
        'Completion Time': completion_time,
        'Turnaround Time': turnaround_time,
        'Waiting Time': waiting_time
    })
    
    return df, avg_turnaround_time, avg_waiting_time

# Example data
burst_time = [7, 10, 5, 3]
priority = [2, 0, 1, 3]

# Calculate priority scheduling
df, avg_tat, avg_wt = priority_scheduling(burst_time, priority)

# Output results
print("Non-preemptive Priority Scheduling:")
print(df)
print(f"\nAverage Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")
