from collections import defaultdict

s = input()


count = defaultdict(int)
for c in s:
    count[c] += 1

for c in s:
    if count[c] == 1:
        print(c)
        break
