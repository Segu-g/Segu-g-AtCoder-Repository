import math

MOD = 998244353

def main():
    t = int(input())
    outputs = []
    for _ in range(t):
        outputs.append(solve())
    print("\n".join(outputs))

def lcm(a, b):
    gcd = math.gcd(a, b)
    return a * b // gcd

def solve():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    ext_n = 1 << (n - 1).bit_length()
    segment_tree = [1 for _ in range(ext_n * 2)]
    for i in range(n):
        segment_tree[ext_n + i] = a_arr[i] 

    for i in range(ext_n-1, 0, -1):
        segment_tree[i] = lcm(segment_tree[2*i], segment_tree[2*i+1])
    
    def segment_lcm(l: int, r: int):
        ret_lcm = 1
        curr_l = ext_n + l
        curr_r = ext_n + r
        while curr_l < curr_r:
            if curr_l & 1:
                ret_lcm = lcm(ret_lcm, segment_tree[curr_l])
                curr_l += 1
            if curr_r & 1:
                ret_lcm = lcm(ret_lcm, segment_tree[curr_r-1])
            curr_l >>= 1
            curr_r >>= 1
        return ret_lcm
        
    result_arr = []
    for i in range(n):
        result_arr.append(lcm(segment_lcm(0, i), segment_lcm(i+1, ext_n)) % MOD)
    
    return (" ".join(map(str, result_arr)))

if __name__ == "__main__":
    main()
