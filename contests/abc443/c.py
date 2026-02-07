n, t = map(int, input().split())
a_arr = list(map(int, input().split()))
a_arr.append(t)

current_is_open = True
last_opened = 0
last_closed = 0

total_opened = 0

for a in a_arr:
    if current_is_open:
        current_is_open = False
        total_opened += a - last_opened
        last_closed = a
    else:
        last_opened = last_closed + 100
        if last_opened < a:
            total_opened += a - last_opened
            last_closed = a

print(total_opened)