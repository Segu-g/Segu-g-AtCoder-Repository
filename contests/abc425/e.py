def main():
    t, m = map(int, input().split())
    n_arr: list[int] = []
    c_arr_arr: list[tuple[int, ...]] = []
    for _ in range(t):
        n = int(input())
        c_arr = tuple(map(int, input().split()))
        n_arr.append(n)
        c_arr_arr.append(c_arr)

    # mを素因数分解する
    m_prime_factor = factorization(m)

    sum_c_arr = [sum(c_arr) for c_arr in c_arr_arr]
    
    p_sc_i_arr = sorted(((sum_c_arr[i], i) for i in range(t)), reverse=True)
    sc_frac_arr = [1 for _ in range(t)]
    current_i = 1
    current_i_frac = 1
    while p_sc_i_arr:
        if p_sc_i_arr[-1][0] == current_i:
            n, i = p_sc_i_arr.pop()
            sc_frac_arr[i] = current_i_frac
        else:
            current_i += 1
            current_i_frac = (current_i_frac * current_i) % m
    
    

    result_arr = []
    for n, c_arr, n_frac in zip(n_arr, c_arr_arr, n_frac_arr):
        result_arr.append(solve(m, n, c_arr, n_frac))

    print("\n".join(map(str, result_arr)))


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

if __name__ == "__main__":
    main()