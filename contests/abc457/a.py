def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    x = int(input())
    print(a_arr[x-1])

if __name__ == "__main__":
    main()
