#abc478 E

from enum import Enum

class OP(Enum):
    LEQ = 0
    LE = 1


def main():
    n, q = map(int, input().split())
    vertices = [n for _ in range(n)]
    edges: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    reveresed_edges = [[] for _ in range(n)]
    for _ in range(q):
        t, u, v = map(int, input().split())
        u = u - 1
        v = v - 1
        edges[u].append((v, t))
        reveresed_edges[v].append((u, t))

    # dfs 
    def dfs(i: int, checked: list[bool], vr: list[int]):
        if checked[i]:
            return
        checked[i] = True
        for next, _ in edges[i]:
            dfs(next, checked, vr)
        vr.append(i)

    vr = []
    checked = [False for _ in range(n)]
    for i in range(n):
        dfs(i, checked, vr)


    def rev_dfs(i: int, checked: list[bool], groups: set):
        checked[i] = True
        groups.add(i)
        for next, _ in reveresed_edges[i]:
            if not checked[next]:
                rev_dfs(next, checked, groups)

    groups = []
    checked = [False for _ in range(n)]
    for v in vr.reverse():
        if not checked[v]:
            next_group = set()
            rev_dfs(v, checked, next_group)
            groups.append(next_group)

    group_index_arr = [0 for _ in range(n)]
    for g_i, group in enumerate(groups):
        for v in group:
            group_index_arr[v] = g_i

    group_indeg_arr = [0 for g_i in range(len(groups))]
    for g_i, group in enumerate(groups):
        for v in group:
            for next_v, t in edges[v]:
                next_g_i = group_index_arr[next_v]
                if g_i == next_g_i:
                    if t == OP.LE:
                        print("No")
                        return
                else:
                    group_indeg_arr[next_g_i] += 1

    topo_queue: list[int] = []
    for g_i in range(len(groups)):
        if group_indeg_arr[g_i] == 0:
            topo_queue.append(g_i)
    
    group_val = [1 for _ in range(len(groups))]
    while len(topo_queue) != 0:
        g_i = topo_queue.pop()
        for v in groups[g_i]:
            for next_v, t in edges[v]:
                next_g_i = group_index_arr[next_v]
                if next_g_i == g_i:
                    continue
                cand = group_val[g_i] + (1 if t == OP.LE.value else 0)
                group_val[next_g_i] = max(group_val[next_g_i], cand)
                group_indeg_arr[next_g_i] -= 1
                if group_indeg_arr[next_g_i] == 0:
                    topo_queue.append(next_g_i)

    ans = [group_val[group_index_arr[i]] for i in range(n)]
    print("Yes")
    print(*ans)


if __name__ == "__main__":
    main()
