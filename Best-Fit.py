blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
allocation = [False] * len(blocks)
print("Process No.\tProcess Size\tBlock")
print("-" * 45)
for p_index, p in enumerate(processes):
    best_index = -1
    for i, block in enumerate(blocks):
        if not allocation[i] and block >= p:
            if best_index == -1 or block < blocks[best_index]:
                best_index = i
    if best_index != -1:
        allocation[best_index] = True
        blocks[best_index] -= p
        print(f"{p_index + 1}\t\t{p}\t\t{best_index + 1}")
    else:
        print(f"{p_index + 1}\t\t{p}\t\tNot Allocated")
print("-" * 45)
