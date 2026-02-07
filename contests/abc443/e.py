def main():
    t = int(input())
    outputs = []
    for _ in range(t):
        outputs.append(solve())
    print("\n".join(outputs))

def solve():
    n, c = map(int, input().split())
    s_mat = [input() for _ in range(n)]

    wallless_mat = [[False for _ in range(n)] for _ in range(n)]
    for col in range(n):
        last_wall_row = None
        for row in range(n):
            if s_mat[row][col] == "#":
                last_wall_row = row
        if last_wall_row is not None:
            for row in range(last_wall_row + 1, n):
                wallless_mat[row][col] = True
    
    # print("wallless")
    # print("\n".join(["".join(["O" if flag else "." for flag in arr]) for arr in wallless_mat]))

    reachable_mat = [[False for _ in range(n)] for _ in range(n)]
    reachable_mat[n-1][c-1] = True
    
    offsets_arr = [(-1, 0, 1) for _ in range(n)]
    offsets_arr[0] = (0, 1)
    offsets_arr[-1] = (-1, 0)
    
    for row in range(n-2, -1, -1):
        for col, offsets in zip(range(n), offsets_arr):
            s = s_mat[row][col]
            is_reachable = any(reachable_mat[row + 1][col + offset] for offset in offsets)
            if is_reachable and wallless_mat[row + 1][col]:
                wallless_mat[row][col] = True
                reachable_mat[row][col] = True
            elif is_reachable and s == ".":
                 reachable_mat[row][col] = True

    # print("reachable")
    # print("\n".join(["".join(["O" if flag else "." for flag in arr]) for arr in reachable_mat]))

    ans = [1 if reachable_mat[0][i] else 0 for i in range(n)]
    return "".join(map(str, ans))

if __name__ == "__main__":
    main()
