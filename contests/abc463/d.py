def main():
    n, k = map(int, input().split())
    lr_arr = tuple(map(int, input().split()) for _ in range(n))
    rl_arr = [(r, l) for (l, r) in lr_arr]
    rl_arr.sort()

    lo = 0
    hi = rl_arr[-1][0] + 1

    while lo < hi:
        mid = (lo + hi) // 2
        if is_achievable(rl_arr, k, mid):
            lo = mid + 1
        else:
            hi = mid
    
    max_score = lo - 1
    if max_score <= 0:
        print(-1)
    else:
        print(max_score)


def is_achievable(rl_arr: list[tuple[int, int]], k: int, score: int):
    r, l = rl_arr[0]
    current_r = r
    current_idx = 1
    for _ in range(k - 1):
        while current_idx < len(rl_arr) and rl_arr[current_idx][1] < current_r + score:
            current_idx += 1
        if not current_idx < len(rl_arr):
            return False
        r, l =  rl_arr[current_idx]
        current_idx += 1
        current_r = r
    return True
        



if __name__ == "__main__":
    main()
