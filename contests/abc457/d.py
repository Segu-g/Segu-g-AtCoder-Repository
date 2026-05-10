def main():
    n, k = map(int, input().split())
    a_arr = tuple(map(int, input().split()))

    min_value = a_arr[0]
    min_index = 0
    for i, a in enumerate(a_arr):
        if a < min_value:
            min_index = i
            min_value = a

    min_lbound = min_value
    min_ubound = min_value + k * (min_index + 1) + 1
    
    lo = min_lbound
    hi = min_ubound
    while lo < hi:
        mid = (lo + hi) // 2
        # count = a[mid] → min_aをmidにするために必要な数
        count = 0
        for i, a in enumerate(a_arr):
            count += max(0, (mid - a + i) // (i+1))
        # bisect_right相当 (e in a[i:]はe > k)
        if k < count:
            hi = mid
        else:
            lo = mid + 1
    print(lo-1)
    

if __name__ == "__main__":
    main()
