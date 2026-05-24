n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    at = int(input(f"Enter AT for P{i+1}: "))
    bt = int(input(f"Enter BT for P{i+1}: "))   
    processes.append([i+1, at, bt, bt])
tq = int(input("Enter TQ: "))
current_time = 0
completed = 0
queue = []
visited = [False] * n
ct = [0] * n   
while completed < n:
    for i in range(n):
        if processes[i][1] <= current_time and visited[i] == False:
            queue.append(i)
            visited[i] = True
    if len(queue) == 0:
        current_time += 1
        continue
    idx = queue.pop(0)
    if processes[idx][3] > tq:
        processes[idx][3] -= tq
        current_time += tq
    else:
        current_time += processes[idx][3]
        processes[idx][3] = 0
        completed += 1
        ct[idx] = current_time
    for i in range(n):
        if processes[i][1] <= current_time and visited[i] == False:
            queue.append(i)
            visited[i] = True
    if processes[idx][3] > 0:
        queue.append(idx)
result = []
for i in range(n):
    pid, at, bt, rt = processes[i]
    tat = ct[i] - at          
    wt = tat - bt             
    result.append([pid, at, bt, ct[i], wt, tat])
result.sort(key=lambda x: x[0])
print("\nP\tAT\tBT\tTQ\tCT\tWT\tTAT")
print("-" * 50)
total_wt = 0
total_tat = 0
for r in result:
    pid, at, bt, ct_val, wt, tat = r
    total_wt += wt
    total_tat += tat
    print(f"P{pid}\t{at}\t{bt}\t{tq}\t{ct_val}\t{wt}\t{tat}")
print("-" * 50)
