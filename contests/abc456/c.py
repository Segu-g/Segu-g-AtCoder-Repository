MOD = 998244353

def main():
    s = input()
    current_lentgh = 0
    prev_char = ""
    total = 0
    for i, c in enumerate(s):
        if prev_char == c:
            current_lentgh = 1
        else:
            current_lentgh += 1
        total += current_lentgh % MOD
        total %= MOD
        prev_char = c
    print(total)


if __name__ == "__main__":
    main()
