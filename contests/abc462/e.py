#abc462 e

def main():
    t = int(input())
    costs = []
    for _ in range(t):
        a, b, x, y = map(int, input().split())
        cost = solve(a, b, x, y)
        costs.append(cost)
    print("\n".join(map(str, costs)))

def solve(a: int, b: int, x: int, y: int):
    x = abs(x)
    y = abs(y)

    if (x + y) % 2 != 0:
        return min(
            solve(b, a, x - 1, y) + a,
            solve(b, a, x + 1, y) + a,
            solve(b, a, x, y - 1) + b,
            solve(b, a, x, y + 1) + b
        )

    cost = min(x, y) * 2 * min(a, b)
    x, y = x - min(x, y), y - min(x, y)
    rest = max(x, y)
    if min(a, b) * 2 < max(a, b):
        cost += rest * 4 * min(a, b)
    else:
        cost += rest // 2 * (a + b)
    return cost 



if __name__ == "__main__":
    main()
