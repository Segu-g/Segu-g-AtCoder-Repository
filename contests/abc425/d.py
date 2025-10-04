def main():
    h, w = map(int, input().split())
    stage = [list(input()) for _ in range(h)]

    black_cords = set()
    for i in range(h):
        for j in range(w):
            if stage[i][j] == "#":
                black_cords.add((i, j))
    
    black_count = len(black_cords)

    while black_cords:
        next_black_cords = set()
        
        for black_cord in black_cords:
            for neighbour in neighbours(black_cord, h, w):
                if stage[neighbour[0]][neighbour[1]] != "#" \
                    and change_black(neighbour, stage, h, w):
                    next_black_cords.add(neighbour)
        
        for next_black_cord in next_black_cords:
            ni, nj = next_black_cord
            stage[ni][nj] = "#"
        black_count += len(next_black_cords)
        black_cords = next_black_cords
    
    print(black_count)

def neighbours(cord, h, w):
    neighbours_arr = []
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = cord[0] + di, cord[1] + dj
        if not (ni < 0 or h <= ni or nj < 0 or nj >= w):
            neighbours_arr.append((ni, nj))
    return neighbours_arr

def change_black(cord, stage, h, w):
    count = 0
    for neighbour in neighbours(cord, h, w):
        if stage[neighbour[0]][neighbour[1]] == "#":
            count += 1
    return count == 1

if __name__ == "__main__":
    main()