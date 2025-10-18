import itertools
from collections import deque

def main():
    h, w = map(int, input().split())
    stage = tuple(
        input() for _ in range(h)
    )

    t_p = (0, 0)
    for i, j in itertools.product(range(h), range(w)):
        if stage[i][j] == "T":
            t_p = (i, j)
        elif stage[i][j] == "#":
            
    
    queue = deque()
    is_t_reachable = [
        [False for _ in range(w)] for _ in range(h)
    ]
    is_t_reachable[t_p[0], t_p[1]] = True

    i_t_p, j_t_p = t_p
    max_i, min_i, max_j, mmin_j = i_t_p, i_t_p, j_t_p, j_t_p
    while queue:
        p = queue.popleft()
        i_p, j_p = p
        for neighbour in neighbours(p, h, w):
            i_n, j_n = neighbour
            if stage[i_n, j_n] != ".":
                continue
            if is_t_reachable[i_n, j_n]:
                continue

            is_t_reachable[i_n, j_n] = True
            max_i = max(max_i, i_n)
            min_i = min(min_i, i_n)
            max_j = max(max_j, j_n)
            min_j = min(min_j, j_n)
            queue.append(neighbour)
    
    flag = False
    cost = float("inf")
    if  max_i + (min_i - i_t_p) >= h-1:
        flag = True
        cost = min(cost, ((h-1) - max_i) * 2)
    if  min_i - (max_i - i_t_p) <= 0:
        flag = True
    if  max_j + (min_j - j_t_p) >= w-1:
        flag = True
    if  min_j - (max_j - j_t_p) <= 0:
        flag = True
    

def neighbours(p: tuple[int, int], h: int, w: int):
    np_arr = []
    for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        if not (p[0] + di < 0 or p[0] + di >= h or p[1] + dj < 0 or p[1] + dj >= w):
            np_arr.append((p[0] + di, p[1] + dj))
    return np_arr

    

if __name__ == "__main__":
    main()
