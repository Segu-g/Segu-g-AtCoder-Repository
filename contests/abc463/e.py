# ABC463 E
# https://atcoder.jp/contests/abc463/tasks/abc463_e

import heapq

def main():
    n, m, y = map(int, input().split())
    edges = tuple(tuple(map(int, input().split())) for _ in range(m))
    x_arr = tuple(map(int, input().split()))

    reachable: list[dict[int, int]] = [dict() for _ in range(n+1)]
    for u, v, t in edges:
        if v in reachable[u]:
            reachable[u][v] = min(reachable[u][v], 2 * t)
            reachable[v][u] = min(reachable[v][u], 2 * t)
        else:
            reachable[u][v] = 2 * t
            reachable[v][u] = 2 * t
    for i, x in enumerate(x_arr):
        reachable[i+1][0] = 2 * x + y
        reachable[0][i+1] = 2 * x + y

    city_arr = [None for _ in range(n+1)]
    time_heap: list[tuple[int, int]] = []

    heapq.heappush(time_heap, (0, 1))
    
    while time_heap:
        time, city = heapq.heappop(time_heap)
        if city_arr[city] is not None:
            continue
        city_arr[city] = time
        for next_city, cost in reachable[city].items():
            if city_arr[next_city] is None:
                heapq.heappush(time_heap, (time + cost, next_city))
    
    ans_arr = tuple(t // 2 for t in city_arr[2:])
    print(" ".join(map(str, ans_arr)))

if __name__ == "__main__":
    main()
