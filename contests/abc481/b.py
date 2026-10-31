

def main():
    n, k = map(int, input().split())
    a_arr = tuple(map(int, input().split()))

    count = 0

    a = a_arr[0]
    if a == k:
        count += 1
    for a_next in a_arr[1:]:
        d = a - k
        d_next = a_next - k
        if d != 0 and (d * d_next) <= 0:
            count += 1
        a = a_next

    print(count)

if __name__ == "__main__":
    main()
