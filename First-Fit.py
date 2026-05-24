blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
print("Process\tSize\tBlock")
print("-" * 30)
for p in range(len(processes)):
    allocated = False
    for b in range(len(blocks)):
        if blocks[b] >= processes[p]:
            print(p + 1, "\t", processes[p], "\t", b + 1)
            blocks[b] = blocks[b] - processes[p]
            allocated = True
            break
    if allocated == False:
        print(p + 1, "\t", processes[p], "\tNot Allocated")
print("-" * 30)