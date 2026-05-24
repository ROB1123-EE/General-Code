n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    at = int(input(f"Enter AT for P{i+1}: "))
    bt = int(input(f"Enter BT for P{i+1}: "))
    processes.append([i+1, at, bt])
completed = 0
current_time = 0
visited = [False] * n
result = []
while completed < n:
    idx = -1
    min_bt = 9999
    for i in range(n):
        if processes[i][1] <= current_time and not visited[i]:
            if processes[i][2] < min_bt:
                min_bt = processes[i][2]
                idx = i
    if idx == -1:
        current_time += 1
        continue
    pid, at, bt = processes[idx]
    ct = current_time + bt
    tat = ct - at
    wt = tat - bt
    result.append([pid, at, bt, ct, wt, tat])
    current_time = ct
    visited[idx] = True
    completed += 1
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