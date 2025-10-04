from collections import defaultdict

n = int(input())
a_arr = tuple(map(int, input().split()))

a_count = defaultdict(int)
for a in a_arr:
    a_count[a] += 1

flag = False
rest_stack = []
for i in range(1, n+1):
    if a_count[i] > 1:
        flag = True
        break
    elif a_count[i] == 0:
        rest_stack.append(i)



if flag:
    print("No")
else:
    print("Yes")
    p_arr = list(a_arr)
    for i in range(n):
        if p_arr[i] == -1:
            p_arr[i] = rest_stack.pop()
    print(" ".join(map(str, p_arr)))

