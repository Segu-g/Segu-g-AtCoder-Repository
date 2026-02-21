from collections import defaultdict

def main():
    n, m = map(int, input().split())
    edge_arr = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input.split())
        u, v = u-1, v-1
        edge_arr[u].add(v)
    
    reachable = [False for _ in range(n)]
    reachable_count = 0
    reachable_connected = [0 for _ in range(n)]
    unreachable_connected = [0 for _ in range(n)]

    reachable_connected[0] = 1
    for i in range(n):
        if reachable_connected[i] == 0:
            pass
        else:
            pass

def search(
    reachable: list[int],
    reachable_count: int,
    reachable_connected: list[int],
    unreachable_connected: list[int],
    current_k: int,
    target: int,
    is_target_reachable: bool,
):
    pass

if __name__ == "__main__":
    main()