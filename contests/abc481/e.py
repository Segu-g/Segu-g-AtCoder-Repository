import math
import functools

def main():
    t = int(input())
    outputs = []
    for _ in range(t):
        outputs.append(solve())
    print("\n".join(map(str, outputs)))

def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    normalized_points = [normalize(point) for point in points]
    normalized_points.sort(key=functools.cmp_to_key(comp))
    rev_point_num = len(tuple(filter(lambda np: np[2], normalized_points)))

    max_point_num = max(rev_point_num, n - rev_point_num)
    rev_cumsum_count = 0
    for i, npoint in enumerate(normalized_points):
        rev_cumsum_count += npoint[2]
        reg_point_num = i + 1 - rev_cumsum_count
        rev_reg_point_num = rev_point_num - rev_cumsum_count + reg_point_num
        max_point_num = max(max_point_num, rev_reg_point_num, n - rev_reg_point_num)
    return max_point_num


def normalize(point: tuple[int, int]) -> tuple[int, int, bool]:
    a, b = point
    gcd = math.gcd(abs(a), abs(b))
    a, b = a // gcd, b // gcd
    rev_flag = False
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
        rev_flag = True
    return (a, b, rev_flag)

def comp(p1: tuple[int, int, bool], p2: tuple[int, int, bool]) -> int:
    a1, b1, _ = p1
    a2, b2, _ = p2
    cross_prod = a1 * b2 - a2 * b1
    return cross_prod

if __name__ == "__main__":
    main()
