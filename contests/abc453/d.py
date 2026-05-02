from enum import Enum
import sys

sys.setrecursionlimit(5*10**6)

Cord = tuple[int, int]


UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

DIRECTIONS = [UP, DOWN, RIGHT, LEFT]
BITMASKS = [0b0001, 0b0010, 0b0100, 0b1000]


def main():
    h, w = map(int, input().split())
    s_mat = [input() for _ in range(h)]
    
    searched_positions: list[list[int]] = [[0 for _ in range(w)] for _ in range(h)]
    routes: list[Cord] = list()
    
    for i in range(h):
        for j in range(w):
            if s_mat[i][j] == "S":
                start_cord = (i, j)
                routes.append(start_cord)
                break
        if len(routes) != 0:
            break
    
    def is_valid_cord(cord: Cord):
        if cord[0] < 0 or h <= cord[0]:
            return False
        if cord[1] < 0 or w <= cord[1]:
            return False
        return True

    def search():
        current_position = routes[-1]
        i, j = current_position
        
        if s_mat[i][j] == "S" or s_mat[i][j] == ".":
            searched_positions[i][j] = 0b1111
            for direction in DIRECTIONS:
                di, dj = direction
                ni, nj = i+di, j+dj
                next_position = (ni, nj)
                if not is_valid_cord(next_position):
                    continue
                if searched_positions[ni][nj] | BITMASKS[dj*dj*2+(1+di+dj)//2]:
                    continue
                searched_positions[ni][nj] |= BITMASKS[dj*dj*2+(1+di+dj)//2]
                routes.append(next_position)
                if search():
                    return True
                else:
                    routes.pop()
        elif s_mat[i][j] == "G":
            return True
        elif s_mat[i][j] == "#":
            return False
        elif s_mat[i][j] == "o":
            pi, pj = routes[-2]
            direction = (i-pi, j-pj)
            di, dj = direction
            ni, nj = i+di, j+dj
            next_position = (ni, nj)
            if not is_valid_cord(next_position):
                return False
            if searched_positions[ni][nj] | BITMASKS[dj*dj*2+(1+di+dj)//2]:
                return False
            searched_positions[ni][nj] |= BITMASKS[dj*dj*2+(1+di+dj)//2]
            routes.append(next_position)
            if search():
                return True
            else:
                routes.pop()
        elif s_mat[i][j] == "x":
            pi, pj = routes[-2]
            p_direction = (i-pi, j-pj)
            for direction in DIRECTIONS:
                di, dj = direction
                ni, nj = i+di, j+dj
                next_position = (ni, nj)
                if p_direction == direction:
                    continue
                if not is_valid_cord(next_position):
                    continue
                if searched_positions[ni][nj] | BITMASKS[dj*dj*2+(1+di+dj)//2]:
                    continue
                searched_positions[ni][nj] |= BITMASKS[dj*dj*2+(1+di+dj)//2]
                routes.append(next_position)
                if search():
                    return True
                else:
                    routes.pop()
        return False
    
    if search():
        outpus = []
        for (pi, pj), (ni, nj) in zip(routes[:-1], routes[1:]):
            direction = (ni-pi, nj-pj)
            if direction == UP:
                outpus.append("U")
            elif direction == DOWN:
                outpus.append("D")
            elif direction == RIGHT:
                outpus.append("R")
            elif direction == LEFT:
                outpus.append("L")
        print("Yes")
        print("".join(outpus))
    else:
        print("No")
    

if __name__ == "__main__":
    main()
