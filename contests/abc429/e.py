from collections import defaultdict
def main():
    n, m = map(int, input().split())    
    neighbours = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        neighbours[u].add(v)
        neighbours[v].add(u)
    is_safe_or_danger = input()

    is_safe = [c == "S" for c in is_safe_or_danger]
    safe_nodes = [i for i in range(n) if is_safe[i]]
    danger_nodes = [i for i in range(n) if not is_safe[i]]

    reached_first: list[tuple[int, int] | None] = [None for i in range(n)]
    reached_cost: list[int] = [None for i in range(n)]
    reached_num = 0
    
    
    current_nodes: defaultdict[int, set[int]] = defaultdict(set)
    
    for safe_node in safe_nodes:
        reached_first[safe_node] = (safe_node, 0)
        for neighbour in neighbours[safe_node]:
            current_nodes[neighbour].add(safe_node)
    current_cost = 1
    while reached_num != n:
        next_nodes: defaultdict[int, set[int]] = defaultdict(set)
        for node, roots in current_nodes.items():
            for root in roots:
                if reached_cost[node] is not None:
                    continue
                if reached_first[node] is None:
                    reached_first[node] = (root, current_cost)
                else:
                    if reached_first[node][0] != root:
                        reached_cost[node] = reached_first[node][1] + current_cost
                        reached_num += 1
                for neighbour in neighbours[node]:
                    next_nodes[neighbour].add(root)
        # print(current_nodes)
        current_nodes = next_nodes
        current_cost += 1
        # print(reached_first)
        # print(reached_cost)
        # print(next_nodes)

    for danger_node in danger_nodes:
        print(reached_cost[danger_node], flush=False)
    



if __name__ == "__main__":
    main()
