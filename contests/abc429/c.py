from collections import defaultdict

def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    a_count = defaultdict(int)
    for a in a_arr:
        a_count[a] += 1
    pattern_count = 0
    for a, count in a_count.items():
        mc2 = (count * (count - 1)) // 2
        rest = n - count
        pattern_count += mc2 * rest
    print(pattern_count)


if __name__ == "__main__":
    main()
