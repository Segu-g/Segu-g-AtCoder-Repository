def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    height = 1
    for i in range(n):
        if height == 0:
            break
        height = max(a_arr[i] - 1, height - 1)
    else:
        i = n
    print(i)


if __name__ == "__main__":
    main()
