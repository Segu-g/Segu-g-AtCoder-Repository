from collections import deque

# ABC456

def main():
    t = int(input())
    results = []
    for _ in range(t):
        results.append(solve())
    print("\n".join(results))

def solve():
    n, m = map(int, input().split())
    reachable_arr = [{i} for i in range(n)] 
    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        reachable_arr[u].add(v)
        reachable_arr[v].add(u)
    w = int(input())
    city_holidays = [tuple(map(lambda c: c=="o", input())) for _ in range(n)]
    
    indeg_mat = [[0 for weekday in range(w)] for city in range(n)]
    for weekday in range(w):
        next_weekday = weekday + 1 if weekday != w-1 else 0
        for city in range(n):
            if city_holidays[city][weekday]:
                for next_city in reachable_arr[city]:
                    if city_holidays[next_city][next_weekday]:
                        indeg_mat[next_city][next_weekday] += 1
    queue = deque()
    for weekday in range(w):
        for city in range(n):
            if city_holidays[city][weekday]:
                if indeg_mat[city][weekday] == 0:
                    queue.append((city, weekday))
    
    topological_sorted_node = []
    while queue:
        node = queue.popleft()
        topological_sorted_node.append(node)
        city, weekday = node
        next_weekday = weekday + 1 if weekday != w-1 else 0
        for next_city in reachable_arr[city]:
            if city_holidays[next_city][next_weekday]:
                indeg_mat[next_city][next_weekday] -= 1
                if indeg_mat[next_city][next_weekday] == 0:
                    queue.append((next_city, next_weekday))
    node_num = sum(map(sum, city_holidays))
    topo_node_num = len(topological_sorted_node)
    return "Yes" if node_num != topo_node_num else "No"


if __name__ == "__main__":
    main()
