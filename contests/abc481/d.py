

def main():
    n, m, s, t = map(int, input().split())
    s, t = s-1, t-1

    paths_arr = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        paths_arr[a].append(b)
    
    for i in range(n):
        paths_arr[i].sort()
    
    costs: list[None|int] = [None for _ in range(n)]
    
    current_cost = 0
    costs[s] = current_cost
    reachable = {s}
    while reachable:
        extended_reachable = reachable.copy()
        for alpha in reachable:
            while len(paths_arr[alpha]) and costs[paths_arr[alpha][0]] is None:
                alpha = paths_arr[alpha][0]
                costs[alpha] = current_cost
                extended_reachable.add(alpha)
        
        next_reachable = set()
        next_cost = current_cost + 1
        for beta in extended_reachable:
            for v_next in paths_arr[beta]:
                if costs[v_next] is None:
                    next_reachable.add(v_next)
                    costs[v_next] = next_cost
        
        if costs[t] is None:
            reachable = next_reachable
        else:
            reachable = set()
        current_cost = next_cost
    
    result = -1
    if costs[t] is not None:
        result = costs[t]
    print(result)

if __name__ == "__main__":
    main()
