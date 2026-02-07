from collections import deque

def main():
    n, m = map(int, input().split())
    edge_inputs = [map(int, input().split()) for _ in range(m)]
    q = int(input())
    queries = [map(int, input().split()) for _ in range(q)]

    paths = [set() for _ in range(n)]
    inverse_paths = [set() for _ in range(n)]
    for x, y in edge_inputs:
        x -= 1
        y -= 1
        paths[x].add(y)
        inverse_paths[y].add(x)
    
    black_reachable = [False for _ in range(n)]
    outputs = []
    for t, v in queries:
        v -= 1
        if t == 1:
            update_reachable = deque()
            update_reachable.append(v)
            while update_reachable:
                node = update_reachable.popleft()
                if not black_reachable[node]:
                    black_reachable[node] = True
                    for next in inverse_paths[node]:
                        update_reachable.append(next)
        elif t == 2:
            outputs.append("Yes" if black_reachable[v] else "No")
    
    print("\n".join(outputs))

    

if __name__ == "__main__":
    main()
