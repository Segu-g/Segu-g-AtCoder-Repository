from collections import defaultdict

def main():
    n, k = map(int, input().split())
    s = input()

    counts = defaultdict(int)
    for i in range(n - k + 1):
        segment = s[i:i+k]
        counts[segment] += 1
    
    max_count = max(counts.values())
    
    max_segments = []
    for segment, count in counts.items():
        if count == max_count:
            max_segments.append(segment)
    max_segments.sort()
    print(max_count)
    print(" ".join(max_segments))

if __name__ == "__main__":
    main()
