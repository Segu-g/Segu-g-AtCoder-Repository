import heapq


def main():
    x = int(input())
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    lessers = []
    graters = []
    center = x
    outputs = []
    for a,b in queries:
        a, b = sorted((a, b))
        if a <= center and center <= b:
            heapq.heappush(lessers, -a)
            heapq.heappush(graters, b)
        elif a <= center and b <= center:
            heapq.heappush(lessers, -a)
            heapq.heappush(lessers, -b)
            heapq.heappush(graters, center)
            center = - heapq.heappop(lessers)
        elif center <= a and center <= b:
            heapq.heappush(graters, a)
            heapq.heappush(graters, b)
            heapq.heappush(lessers, -center)
            center = heapq.heappop(graters)
        outputs.append(center)
    print("\n".join(map(str, outputs)))
        


if __name__ == "__main__":
    main()
