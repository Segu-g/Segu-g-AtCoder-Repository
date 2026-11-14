
def main():
    n = int(input())
    uv_arr = [tuple(map(int, input().split())) for _ in range(n-1)]
    colors = tuple(map(int, input().split()))
    
    edges = [set() for _ in range(n)]
    color_edges = [set() for _ in range(n)]
    for u, v in uv_arr:
        u, v =  u-1, v-1
        edges[u].add(v)
        edges[v].add(u)
        if colors[u] == colors[v]:
            color_edges[u].add(v)
            color_edges[v].add(u)
    
    max_depth = [dict() for _ in range(n)]
    record_depth(None, 0, edges, max_depth)
    propagete_depth(None, 0, 0, edges, max_depth)

    print(edges)
    print(max_depth)

    color_max_depth = [dict() for _ in range(n)]
    for i in range(n):
        if len(color_max_depth[i]) == 0:
            record_depth(None, i, color_edges, color_max_depth)
            propagete_depth(None, i, 0, color_edges, color_max_depth)
    print(color_edges)
    print(color_max_depth)

def record_depth(v_p: int|None, v: int, edges: list[set[int]], max_depth: list[dict[int, int]]):
    for v_c in edges[v]:
        if v_c == v_p:
            continue
        d = record_depth(v, v_c, edges, max_depth)
        max_depth[v][v_c] = d
    if len(max_depth[v]) == 0:
        return 1
    return max(max_depth[v].values()) + 1


def propagete_depth(v_p: int|None, v: int, depth: int, edges: list[set[int]], max_depth: list[dict[int, int]]):
    if v_p is not None:
        max_depth[v][v_p] = depth
    v_c_arr = list(edges[v])
    v_c_arr.sort(key=lambda v_c: max_depth[v][v_c])
    
    for v_c in v_c_arr[:-1]:
        if v_c != v_p:
            propagete_depth(v, v_c, max_depth[v][v_c_arr[-1]] + 1, edges, max_depth)
    if len(v_c_arr) != 0 and v_c_arr[-1] != v_p:
        if len(v_c_arr) >= 2: 
            propagete_depth(v, v_c_arr[-1], max_depth[v][v_c_arr[-2]] + 1, edges, max_depth)
        else:
            propagete_depth(v, v_c_arr[-1], 1, edges, max_depth)
    
         


if __name__ == "__main__":
    main()
