
def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    b_arr = tuple(map(int, input().split()))

    match_arr = [a==b for a, b in zip(a_arr, b_arr)]
    first_unmach_i = match_arr.index(False) if False in match_arr else None
    if first_unmach_i is None:
        print("Yes")
        return
    
    a_arr = a_arr[first_unmach_i:]
    b_arr = b_arr[first_unmach_i:]

    match_arr = [a==b for a, b in zip(a_arr, b_arr)]
    last_unmach_i = len(match_arr) - match_arr[::-1].index(False)

    a_arr = a_arr[:last_unmach_i]
    b_arr = b_arr[:last_unmach_i]

    if a_arr[0] == b_arr[-1]:
        a_subarr = a_arr[1:]
        b_subarr = b_arr[:-1]
        if a_subarr == b_subarr:
            print("Yes")
            return

    if a_arr[-1] == b_arr[0]:
        a_subarr = a_arr[:-1]
        b_subarr = b_arr[1:]
        if a_subarr == b_subarr:
            print("Yes")
            return

    print("No")

if __name__ == "__main__":
    main()
