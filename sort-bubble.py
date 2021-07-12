a = [-3, 5, 0, -8, 1, 10]
N = len(a)

for i in range(N - 1):
    for j in range(N - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
