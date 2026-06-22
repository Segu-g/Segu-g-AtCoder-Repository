import heapq

def main():
    n = int(input())
    hl_arr = tuple(tuple(map(int, input().split())) for _ in range(n))
    q = int(input())
    t_arr = tuple(map(int, input().split()))

    t_qi_arr = [(t, qi) for qi, t in enumerate(t_arr)]
    t_qi_arr.sort()
    ans_arr = [0 for _ in range(q)]

    mh_l_heap = [(-h, l) for (h, l) in hl_arr]
    heapq.heapify(mh_l_heap)

    for t, qi in t_qi_arr:
        while mh_l_heap[0][1] <= t:
            heapq.heappop(mh_l_heap)
        ans_arr[qi] = - mh_l_heap[0][0]
    
    print("\n".join(map(str, ans_arr)))

if __name__ == "__main__":
    main()
