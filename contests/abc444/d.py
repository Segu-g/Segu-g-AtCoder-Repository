def main():
    n = int(input())
    a_arr = list(map(int, input().split()))
    a_arr.sort(reverse=True)

    carry = 0
    current_digit = 0
    digit_values = []
    while carry != 0 or a_arr:
        carry += len(a_arr)
        digit_values.append(carry % 10)
        carry = carry // 10

        current_digit += 1
        while a_arr and a_arr[-1] <= current_digit:
            a_arr.pop()
    
    print("".join(map(str, reversed(digit_values))))


if __name__ == "__main__":
    main()
