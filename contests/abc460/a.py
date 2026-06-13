n, m = map(int, input().split())
count = 0
while m != 0:
    count += 1
    m = n % m
print(count)