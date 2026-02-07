import heapq

def main():
    t = int(input())

    n_arr = []
    r_arr_arr = []
    for _ in range(t):
        n_arr.append(int(input()))
        r_arr_arr.append(list(map(int, input().split())))

    outputs = []
    for n, r_arr in zip(n_arr, r_arr_arr):
        outputs.append(solve(n, r_arr))
    
    print("\n".join(map(str, outputs)))

def solve(n, r_arr) :
    heap = [(r, i) for i, r in enumerate(r_arr)]
    heapq.heapify(heap)
    target_arr = [None for _ in range(n)]
    while heap:
        r, i = heapq.heappop(heap)
        if target_arr[i] is None:
            target_arr[i] = r
            left_i = i - 1
            if 0 <= left_i:
                heapq.heappush(heap, (r + 1, left_i))
            right_i = i + 1
            if right_i < n:
                heapq.heappush(heap, (r + 1, right_i))
    return sum(r - t for r, t in zip(r_arr, target_arr))



if __name__ == "__main__":
    main()