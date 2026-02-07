
def main():
    n = int(input())
    w_arr = list()
    h_arr = list()
    b_arr = list()
    for _ in range(n):
        w, h, b = map(int, input().split())
        w_arr.append(w)
        h_arr.append(h)
        b_arr.append(b)

    w_max = sum(w_arr)
    weight_dp = [float("-inf") for _ in range(2 * w_max + 1)]
    weight_dp[w_max] = 0
    
    next_weight_dp = [0 for _ in range(2 * w_max + 1)]
    for w, h, b in zip(w_arr, h_arr, b_arr):
        for i in range(2 * w_max + 1):
            next_weight_dp[i] = weight_dp[i]
            if 0 <= i - w:
                next_weight_dp[i] = max(weight_dp[i - w] + b, next_weight_dp[i])
            if i + w < 2 * w_max + 1:
                next_weight_dp[i] = max(next_weight_dp[i], weight_dp[i + w] + h)
        weight_dp, next_weight_dp = next_weight_dp, weight_dp 
    
    print(max(weight_dp[w_max:]))


if __name__ == "__main__":
    main()
