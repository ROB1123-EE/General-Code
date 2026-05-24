blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

allocation = [-1] * len(blocks)
print("Process No.\tProcess Size\tBlock")
print("-" * 45)
for p_index, p in enumerate(processes):
    worst_index = -1
    for i, block in enumerate(blocks):
        if allocation[i] == -1 and block >= p:
            if worst_index == -1 or block > blocks[worst_index]:
                worst_index = i
    if worst_index != -1:
        allocation[worst_index] = p_index
        blocks[worst_index] -= p
        print(f"{p_index + 1}\t\t{p}\t\t{worst_index + 1}")
    else:
        print(f"{p_index + 1}\t\t{p}\t\tNot Allocated")
print("-" * 45)