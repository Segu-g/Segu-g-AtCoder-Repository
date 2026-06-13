from collections import deque

MOD = 998244353

def main():
    n = int(input())
    p_arr = tuple(map(int, input().split()))
    c_arr = tuple(map(int, input().split()))
    d_arr = tuple(map(int, input().split()))

    d_total = sum(d_arr)
    factorial_arr = [1]
    for i in range(d_total+1):
        factorial_arr.append((factorial_arr[-1] * (i + 1)) % MOD)
    factorial_inv_arr = [pow(factorial, MOD-2, MOD) for factorial in factorial_arr]

    def combination(m, l):
        if m < l:
            return 0
        denominator = 1
        for d in range(l):
            denominator = (denominator * (m - d)) % MOD
        return (denominator * factorial_inv_arr[l]) % MOD

    parent_arr = [0] + [p-1 for p in p_arr]

    in_deg_arr = [0 for _ in range(n)]
    for p in p_arr:
        in_deg_arr[p-1] += 1


    rest_candy_arr = list(c_arr)
    pattern_arr = [1 for _ in range(n)]

    queue = deque()
    for i in range(n):
        if in_deg_arr[i] == 0:
            queue.append(i)
    
    while queue:
        target = queue.popleft()
        d = d_arr[target]
        rest_candy = rest_candy_arr[target]
        pattern = pattern_arr[target]
        
        pattern = (pattern * combination(rest_candy, d)) % MOD
        rest_candy = rest_candy - d

        if target != 0:
            parent = parent_arr[target]
            rest_candy_arr[parent] += rest_candy
            pattern_arr[parent] = (pattern_arr[parent] * pattern) % MOD

            in_deg_arr[parent] -= 1
            if in_deg_arr[parent] == 0:
                queue.append(parent)
        else:
            rest_candy_arr[0] = rest_candy
            pattern_arr[0] = pattern % MOD
    print(pattern_arr[0])
        





if __name__ == "__main__":
    main()
