import math
MOD = 998244353

def main():
    x1, x2, x3 = tuple(map(int, input().split()))
    maximum = max(x1, x2, x3) + 1
    
    inverse_factorials = [1 for _ in range(maximum+1)]
    for i in range(1, maximum+2):
        inverse_factorials[i] = (inverse_factorials[i-1] * pow(i, MOD-2, MOD)) % MOD
    
    factorials = [1 for _ in range(maximum+1)]
    for i in range(1, maximum+2):
        factorials[i] = (factorials[i-1] * i) % MOD
    
    def comb(n, m):
        if m < 0 or m > n:
            return 0
        return (((factorials[n] * inverse_factorials[m]) % MOD) * inverse_factorials[n-m]) % MOD

    for space in range(2, min(x3+x1+1, x2+1+1)):
        space
        p_c3 = comb(x2+1, c3) * comb(x3+1, c3)
        p_c2
        pattern = 




if __name__ == "__main__":
    main()
