import sys
# import numpy as np
import itertools
sys.setrecursionlimit(10**7)


def main():
    m, a, b = map(int, input().split())
    search_flag_arr = [False for _ in range(m*m)]
    result_arr = [False for _ in range(m*m)]
    
    for s1, s2 in itertools.product(range(m), repeat=2):
        # print(f"loop ({s1} {s2})")
        search(m, a, b, s1, s2, search_flag_arr, result_arr)
    
    # print(np.reshape(result_arr, (m, m)))
    print(len(result_arr) - sum(result_arr))

def search(m, a, b, s1, s2, search_flag_arr, result_arr):
    idx = s1*m + s2
    current_flag = s1 == 0 or s2 == 0
    if current_flag:
        search_flag_arr[idx] = True
        result_arr[idx] = current_flag
        return current_flag
    elif search_flag_arr[idx]:
        return result_arr[idx]
    else:
        search_flag_arr[idx] = True
        s3 = ((a * s2) % m + (b * s1) % m) % m
        # print(f"    ({s1} {s2}) -> ({s2} {s3})")
        flag = search(m, a, b, s2, s3, search_flag_arr, result_arr)
        result_arr[idx] = flag
        return flag

if __name__ == "__main__":
    main()