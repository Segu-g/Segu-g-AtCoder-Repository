import numpy as np
def main():
    n, q = map(int, input().split())
    a_arr = tuple(map(int, input().split()))
    rep_a_arr = tuple((*a_arr, *a_arr))
    rep_a_cumsum = np.zeros(2*n+1, dtype=int)
    rep_a_cumsum[1:] = np.cumsum(rep_a_arr)

    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    
    offset = 0
    result_arr: list[int] = []
    for query in queries:
        q_label, *rest_arg = query
        if q_label == 1:
            (c,)  = rest_arg
            offset += c
            offset %= n
        elif q_label == 2:
            (l, r)  = rest_arg
            l, r = l-1, r-1
            result_arr.append(rep_a_cumsum[offset+r+1] - rep_a_cumsum[offset+l])
    print("\n".join(map(str, result_arr)))



if __name__ == "__main__":
    main()