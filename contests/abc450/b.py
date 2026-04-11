def main():
    n = int(input())
    cost = [tuple(map(int, input().split())) for _ in range(n-1)]

    flag = False
    for a in range(n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                cost_ac = cost[a][c-a-1]
                cost_ab_bc = cost[a][b-a-1] + cost[b][c-b-1]
                if cost_ab_bc < cost_ac:
                    flag = True
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    print("Yes" if flag else "No")


if __name__ == "__main__":
    main()
