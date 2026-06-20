STATE = (None, "a", "b", "c")

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())

def solve(s: str, k: int):
    effective_original_states = [None for _ in range(len(s)+1)]
    count = 0
    for i, (c1, c2, c3) in enumerate(zip(s[0:-2], s[1:-1], s[2:])):
        if (c1, c2, c3) == ("a", "b", "c"):
            effective_original_states[i+1] = "a"
            effective_original_states[i+2] = "b"
            effective_original_states[i+3] = "c"
            count += 1
    if len(s) < (count + k) * 3:
        return -1
    
    dk_state = tuple(range(-3, k+1))
    dp = tuple(tuple([len(s) for _ in range(len(s) + 1)] for state in STATE) for dk in dk_state)
    
    dp[dk_state.index(0)][STATE.index(None)][0] = 0
    for p_index, c in enumerate(s):
        n_index = p_index + 1
        # 文字を変更しない場合
        if c in STATE:
            s_idx = STATE.index(c)
            for i_dk, dk in enumerate(dk_state[:-1]): 
                dp[i_dk][s_idx][n_index] = min(dp[i_dk][s_idx][n_index], dp[i_dk][s_idx-1][n_index-1])
        else:
            s_idx = STATE.index(c)
            for i_dk, dk in enumerate(dk_state[:-1]):
                for s_idx
                dp[i_dk][s_idx][n_index] = min(dp[i_dk][s_idx][n_index], dp[i_dk][s_idx-1][n_index-1])
         

if __name__ == "__main__":
    main()
