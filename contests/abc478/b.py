def main():
    n, v = map(int, input().split())
    w_arr = tuple(map(int, input().split()))

    w_sum_arr = [[0 for w_sum in range(v+1)] for _ in range(3)]
    for i, w_i in enumerate(w_arr):
        cost = i + 1
        for i in range(cost, v+1):
            w_sum_arr[2][i] = max(w_sum_arr[2][i], w_sum_arr[1][i-cost] + w_i)
        for i in range(cost, v+1):
            w_sum_arr[1][i] = max(w_sum_arr[1][i], w_sum_arr[0][i-cost] + w_i)
        if cost <= v:
            w_sum_arr[0][cost] = max(w_sum_arr[0][cost], w_i)
    print(max(w_sum_arr[-1]))
                

if __name__ == "__main__":
    main()
