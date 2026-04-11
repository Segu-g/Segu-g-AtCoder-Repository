from collections import deque
from itertools import product

def main():
    h, w = map(int, input().split())
    s_mat = tuple(input() for _ in range(h))

    grouped = [[False for _ in range(w)] for _ in range(h)]
    
    def is_valid(cord: tuple[int, int]):
        return 0 <= cord[0] and cord[0] < h and 0 <= cord[1] and cord[1] < w
    
    def search(root: tuple[int, int]):
        queue: deque[tuple[int, int]] = deque()
        queue.append(root)
        while len(queue) != 0:
            cord = queue.popleft()
            dif_neighbour = ((-1, 0), (1, 0), (0, -1), (0, 1))
            neighbours = [(cord[0] + dif[0], cord[1] + dif[1]) for dif in dif_neighbour]
            valid_neighbour = filter(is_valid, neighbours)
            for next in valid_neighbour:
                if s_mat[next[0]][next[1]] == "." and not grouped[next[0]][next[1]]:
                    grouped[next[0]][next[1]] = True
                    queue.append(next)
    
    for i in range(w):
        if not grouped[0][i] and s_mat[0][i] == ".":
            grouped[0][i] = True
            search((0, i))
        if not grouped[h-1][i] and s_mat[h-1][i] == ".":
            grouped[h-1][i] = True
            search((h-1, i))
    
    for i in range(h):
        if not grouped[i][0] and s_mat[i][0] == ".":
            grouped[i][0] = True
            search((i, 0))
        if not grouped[i][w-1] and s_mat[i][w-1] == ".":
            grouped[i][w-1] = True
            search((i, w-1))
    
    count = 0
    for i, j in product(range(1, h-1), range(1, w-1)):
        if not grouped[i][j] and s_mat[i][j] == ".":
            grouped[i][j] = True
            search((i, j))
            count += 1

    print(count)

if __name__ == "__main__":
    main()
