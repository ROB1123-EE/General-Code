available = [3, 3, 2]
allo = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
maX = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
n, r = len(allo), 3
need = [[maX[i][j] - allo[i][j] for j in range(r)] for i in range(n)]
print (need)

work = available[:]
finish = [False]*n
safe_seq = []

for _ in range(n):
    for i in range(n):
        if not finish[i] and all(need[i][j] <= work[j] for j in range(r)):
            work = [work[j] + allo [i][j] for j in range (r)]
            finish[i] = True
            safe_seq.append(i)
            break
        else:
            continue
if len(safe_seq) == n:
    print("Safe sequence is:", ' -> '.join(f"P{idx}" for idx in safe_seq))
else:
    print("Unsafe State.")
print(work)
