

def main():
    t = int(input())
    ans = []
    for _ in range(t):
        ans.append(solve())
    print("\n".join(ans))

def solve():
    px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())
    p = (px, py)
    q = (qx, qy)
    r = (rx, ry)
    s = (sx, sy)

    if len({p, q, r, s}) < 4:
        return "Yes"

    pq = (qx - px, qy - py)
    rs = (sx - rx, sy - ry)

    if pq[0] * rs[1] == pq[1] * rs[0]:
        v_mpq_mrs = tuple(p[i] + q[i] - r[i] - s[i] for i in range(2))
        if v_mpq_mrs[0] * pq[0] + v_mpq_mrs[1] * pq[1] != 0:
            return "No"

    return "Yes" 

if __name__ == "__main__":
    main()
