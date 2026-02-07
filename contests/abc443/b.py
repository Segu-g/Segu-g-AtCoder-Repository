n, k = map(int, input().split())

initial_n = n
total = 0

while total < k:
    total += n
    n += 1

print(n - 1 - initial_n)