import sys
sys.setrecursionlimit(10**5)

def main():
    n, x, y = map(int, input().split())
    queries = tuple(input().split() for _ in range(n))
    segments: list[tuple[int, int, int, int]] = [(0, 0, x, y)]
    for c, a, b in queries:
        a, b = int(a), int(b)
        direc = 0 if c == "X" else 1
        subdirec = 1 if c == "X" else 0
        
        for i in range(len(segments)):
            segment = segments[i]
            base = segment[direc]
            size = segment[2 + direc]
            edge = base + size
            if (base < a and a < edge):
                segments[i] = tuple((
                    *segment[:2+direc],
                    a - base,
                    *segment[2+direc+1:]
                ))
                splitted = tuple((
                    *segment[:direc],
                    a,
                    *segment[direc+1:2+direc],
                    edge - a,
                    *segment[2+direc+1:]
                ))
                segments.append(splitted)
    
        for i in range(len(segments)):
            segment = segments[i]
            segments[i] = tuple((
                *segment[:subdirec],
                segment[subdirec] + (b if a <= segment[direc] else -b),
                *segment[subdirec+1:]))

    uf = [- (segment[2] * segment[3]) for segment in segments]
    for i in range(len(segments) - 1):
        for j in range(i + 1, len(segments)):
            segment_i = segments[i]
            segment_j = segments[j]
            if is_connected(segment_i, segment_j):
                uf_connect(uf, i, j)
    
    connected_elements = [-value for value in uf if value < 0]
    connected_elements.sort()
    print(len(connected_elements))
    print(" ".join(map(str, connected_elements)))

def is_connected(s1, s2):
    for segment_a, segment_b in ((s1, s2), (s2, s1)):
        for direc in (0, 1):
            subdirec = 1 - direc
            a_upper = segment_a[direc] + segment_a[2+direc]
            b_lower = segment_b[direc]
            if a_upper == b_lower:
                subbase_a = segment_a[subdirec]
                subedge_a = subbase_a + segment_a[2+subdirec]
                subbase_b = segment_b[subdirec]
                subedge_b = subbase_b + segment_b[2+subdirec]
                if (subbase_a < subedge_b) and (subbase_b < subedge_a):
                    return True
    return False

def uf_root(uf: list[int], x: int):
    value = uf[x]
    if value < 0:
        return x
    else:
        x_root = uf_root(uf, value)
        uf[x] = x_root
        return x_root
    
def uf_connect(uf: list[int], x: int, y: int):
    x_root = uf_root(uf, x)
    y_root = uf_root(uf, y)
    if x_root == y_root:
        return
    x_root, y_root = sorted((x_root, y_root))
    uf[x_root] += uf[y_root]
    uf[y_root] = x_root

if __name__ == "__main__":
    main()
