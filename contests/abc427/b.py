n = int(input())

def f(v: int):
    s = str(v)
    return sum(map(int, s))

current_value = 1
sum_f_a_arr = f(current_value)
for _ in range(n):
    current_value = sum_f_a_arr
    sum_f_a_arr += f(current_value)
    # print(current_value)

print(current_value)
