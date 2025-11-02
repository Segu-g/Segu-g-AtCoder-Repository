

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    segment_set: set[str] = set()
    for i_offset in range(n - m + 1):
        for j_offset in range(n - m + 1):
            segment = "\n".join((s[i_offset + diff][j_offset:j_offset+m] for diff in range(m)))
            segment_set.add(segment)
    print(len(segment_set))

if __name__ == "__main__":
    main()
