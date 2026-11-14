import bisect


def main():
    h, w, n, q = map(int, input().split())
    r_arr = []
    c_arr = []
    for _ in range(n):
        r, c = map(int, input().split())
        r_arr.append(r)
        c_arr.append(c)
    r_arr.sort()
    c_arr.sort()
    arr_dest = [[], r_arr, c_arr]
    ans_arr = []
    for i_q in range(q):
        query_type, b, t = map(int, input().split())
        arr = arr_dest[query_type]
        count = bisect.bisect_left(arr, t+1) - bisect.bisect_left(arr, b)
        ans_arr.append(count)
    print("\n".join(map(str, ans_arr)))

if __name__ == "__main__":
    main()
