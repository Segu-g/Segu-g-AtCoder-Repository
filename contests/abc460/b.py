def main():
    t = int(input())
    outputs = []
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        if r1 > r2:
            x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
        dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
        if dist_sq < (r2 - r1) ** 2 or (r1 + r2) ** 2 < dist_sq:
            output = "No"
        else:
            output = "Yes"
        outputs.append(output)
    print("\n".join(outputs))

if __name__ == "__main__":
    main()
