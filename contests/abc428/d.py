def main():
    t = int(input())
    for _ in range(t):
        solve()

def solve():
    c, d = map(int, input().split())
    str_c, str_cpd = str(c), str(c + d)
    str_c_length = len(str_c)
    maximum = int(str_c + str_cpd)
    current_n = c
    count = 0
    while current_n ** 2 <= maximum:
        current_text = str(current_n ** 2)
        if current_text.startswith(str_c):
            rest_text = current_text[str_c_length:]
            rest_value = int(rest_text)
            diff = rest_value - c
            if 1 <= diff and diff <= d and not rest_text.startswith("0"):
                count += 1
                # print(current_n, current_n**2)
        current_n += 1
    print(count, flush=False)

if __name__ == "__main__":
    main()
