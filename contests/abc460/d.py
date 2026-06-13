from itertools import product
from collections import deque


def main():
    h, w = map(int, input().split())
    s_mat = tuple(input() for _ in range(h))
    mat = [c == "#" for s_arr in s_mat for c in s_arr]

    def matrix():
        return product(range(h), range(w))
    
    def neighbors(i, j):
        neighbors = [(i + di, j + dj) for di in (-1, 0, 1) for dj in (-1, 0, 1)]
        return filter(lambda cord: 0 <= cord[0] < h and 0 <= cord[1] < w, neighbors)
    
    amat = mat.copy()
    bmat = [False for _ in range(h * w)]
    for i, j in matrix():
        if amat[i * w + j]:
            bmat[i * w + j] = False
        for ni, nj in neighbors(i, j):
            if amat[ni * w + nj]:
                bmat[i * w + j] = True
                break
        else:
            bmat[i * w + j] = False
    
    amat = bmat
    bmat = [False for _ in range(h * w)]
    for i, j in matrix():
        if amat[i * w + j]:
            bmat[i * w + j] = False
        for ni, nj in neighbors(i, j):
            if amat[ni * w + nj]:
                bmat[i * w + j] = True
                break
        else:
            bmat[i * w + j] = False
    

    if sum(bmat) == 0:
        print("\n".join("." * w for _ in range(h)))
        return

    state = [None for _ in range(h * w)]
    queue = deque()
    for i, j in matrix():
        if bmat[i * w + j]:
            state[i * w + j] = True
            for ni, nj in neighbors(i, j):
                if not bmat[ni * w + nj] and state[ni * w + nj] is None:
                    state[ni * w + nj] = False
                    queue.append((ni, nj))
    
    while queue:
        i, j = queue.popleft()
        for ni, nj in neighbors(i, j):
            if state[ni * w + nj] is None:
                state[ni * w + nj] = not state[i * w + j]
                queue.append((ni, nj))
    
    print("\n".join("".join("." if state[i * w + j] else "#" for j in range(w)) for i in range(h)))

                
if __name__ == "__main__":
    main()
