a = [-3, 5, 0, -8, 1, 10]
N = len(a)

for i in range(N - 1):
    for j in range(i + 1, N):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
