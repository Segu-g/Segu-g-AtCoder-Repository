import heapq

MOD = 998244353

type LinkedList = tuple[int, LinkedList|None]
type LinkedListNumber = tuple[int, LinkedList]

def main():
    n, m = map(int, input().split())
    edge_arr = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        edge_arr[a].append((c, b))
    for i in range(n):
        edge_arr[i].sort()

    min_costs_arr = [float("inf") for _ in range(n)]
    min_costs_arr[0] = 0
    reached_count = 1

    heap: list[tuple[LinkedListNumber, int]] = [((1, cn, None), b) for cn, b in edge_arr[0]]
    heapq.heapify(heap)
    while heap and reached_count != n:
        cost, v = heapq.heappop(heap)
        
        if min_costs_arr[v] < cost:
            continue
        
        min_costs_arr[v] = cost
        reached_count += 1

        for c_edge, next_v in edge_arr[v]:
            next_cost = cost + c_edge
            if next_cost < min_costs_arr[next_v]:
                min_costs_arr[next_v] = next_cost
                heapq.heappush(heap, (next_cost, next_v))

    print("\n".join(map(str, (a % MOD for a in min_costs_arr[1:]))))


if __name__ == "__main__":
    main()
