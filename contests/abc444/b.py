def main():
    n, k = map(int, input().split())
    count = 0
    for i in range(1, n+1):
        digit_sum = 0
        for _ in range(6):
            digit_sum += i % 10
            i //= 10
        if digit_sum == k:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
