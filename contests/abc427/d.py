def main():
    t = int(input())
    for _ in range(t):
        solve()

def solve():
    n, m, k = map(int, input().split())
    s = input()
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        edges.append((u, v))

    reachable = [set() for _ in range(n)]
    for u, v in edges:
        reachable[u].add(v)
    
    current_winner_map = [1 if c == "A" else -1 for c in s]
    prev_winners_map = [0 for _ in range(n)]
    for _ in range(k):
        for turn in (-1, 1):
            for i in range(n):
                next_state_set = set()
                for next_vertex in reachable[i]:
                    next_state_set.add(current_winner_map[next_vertex])
                if turn in next_state_set:
                    prev_winners_map[i] = turn
                elif (- turn) in next_state_set:
                    prev_winners_map[i] = - turn
                else:
                    prev_winners_map[i] = 0 
            current_winner_map, prev_winners_map = prev_winners_map, current_winner_map
    winner = "Alice"
    if current_winner_map[0] == -1:
         winner = "Bob"
    print(winner, flush=False)

    

if __name__ == "__main__":
    main()
