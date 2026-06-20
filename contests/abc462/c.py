

def main():
    n = int(input())
    cords = [tuple(map(int, input().split())) for _ in range(n)]
    cords.sort()
    
    counts = 1
    y_min = cords[0][1]
    for x, y in cords[1:]:
        if y < y_min:
            counts += 1
        y_min = min(y_min, y)
    print(counts)

if __name__ == "__main__":
    main()
