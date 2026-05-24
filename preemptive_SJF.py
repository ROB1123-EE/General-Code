n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    at = int(input(f"Enter Arrival Time for P{i+1}: "))
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append([i+1, at, bt, bt])  
completed = 0
current_time = 0
ct = [0] * n
while completed < n:
    idx = -1
    min_rt = 9999
    for i in range(n):
        if processes[i][1] <= current_time and processes[i][3] > 0:
            if processes[i][3] < min_rt:
                min_rt = processes[i][3]
                idx = i
    if idx == -1:
        current_time += 1
        continue
    processes[idx][3] -= 1
    current_time += 1
    if processes[idx][3] == 0:
        completed += 1
        ct[idx] = current_time
result = []
for i in range(n):
    pid, at, bt, rt = processes[i]
    tat = ct[i] - at
    wt = tat - bt
    result.append([pid, at, bt, ct[i], wt, tat])
result.sort(key=lambda x: x[0])
print("\nP\tAT\tBT\tCT\tWT\tTT")
print("-" * 45)
total_wt = 0
total_tat = 0
for r in result:
    pid, at, bt, ct, wt, tat = r
    total_wt += wt
    total_tat += tat
    print(f"P{pid}\t{at}\t{bt}\t{ct}\t{wt}\t{tat}")
print("-" * 45)