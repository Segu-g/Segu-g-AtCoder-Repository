MOD = 998244353

def main():
    s = input()
    characters = "abc"
    segment_dp = [[0 for _ in range(len(s))] for _ in characters]
    c_idx = characters.index(s[0])
    segment_dp[c_idx][0] += 1
    for i, c in zip(range(1, len(s)), s[1:]):
        c_idx = characters.index(c)
        for last_c_idx, last_c in enumerate(characters):
            if last_c != c:
                segment_dp[last_c_idx][i] = segment_dp[last_c_idx][i-1]
                segment_dp[c_idx][i] += segment_dp[last_c_idx][i-1]
                segment_dp[c_idx][i] %= MOD
            else:
                segment_dp[c_idx][i] += segment_dp[last_c_idx][i-1] + 1
                segment_dp[c_idx][i] %= MOD
    total= sum(segment_dp[i][-1] for i in range(len(characters)))
    print(total % MOD)


if __name__ == "__main__":
    main()
