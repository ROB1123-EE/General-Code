n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    at = int(input(f"Enter AT for P{i+1}: "))
    bt = int(input(f"Enter BT for P{i+1}: "))
    processes.append([i + 1, at, bt])  
processes.sort(key=lambda x: x[1])
current_time = 0
results = []
for p in processes:
    pid, at, bt = p
    if current_time < at:
        current_time = at
    ct = current_time + bt         
    tat = ct - at                 
    wt = tat - bt
    current_time = ct
    results.append([pid, at, bt, ct, wt, tat])
results.sort(key=lambda x: x[0])
print("\nP\tAT\tBT\tCT\tWT\tTT")
print("-" * 45)
total_wt = 0
total_tat = 0
for r in results:
    pid, at, bt, ct, wt, tat = r
    total_wt += wt
    total_tat += tat
    print(f"P{pid}\t{at}\t{bt}\t{ct}\t{wt}\t{tat}")
print("-" * 45)