def main():
    t = int(input())
    for _ in range(t):
        solve_case()

def solve_case():
    n = int(input())
    tonakai_arr = [tuple(map(int, input().split())) for i in range(n)]
    tonakai_arr.sort(key=lambda t: t[0] + t[1])
    total_weight = sum(t[0] for t in tonakai_arr)
    total_power = 0
    while tonakai_arr and (total_weight > total_power):
        w, p = tonakai_arr.pop()
        total_weight -= w
        total_power += p
    print(len(tonakai_arr), flush=False)

if __name__ == "__main__":
    main()
