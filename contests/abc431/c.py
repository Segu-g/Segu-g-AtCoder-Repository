def main():
    n, m, k = map(int, input().split())
    h_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    h_arr.sort()
    b_arr.sort()

    count = 0
    while len(h_arr) != 0 and len(b_arr) != 0:
        while len(h_arr) != 0 and h_arr[-1] > b_arr[-1]:
            h_arr.pop()
        if len(h_arr) == 0:
            break

        h_arr.pop()
        b_arr.pop()
        count += 1
    
    output = "Yes" if count >= k else "No"
    print(output)


if __name__ == "__main__":
    main()
