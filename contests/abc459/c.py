import bisect

def main():
    n, q = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    count_arr = [0 for _ in range(n)]
    sorted_count_set = [0 for _ in range(n)]
    outputs = []
    for query in queries:
        if query[0] == 1:
            _, x = query
            prev_count = count_arr[x-1]
            count_arr[x-1] += 1
            idx = bisect.bisect_right(sorted_count_set, prev_count)
            sorted_count_set[idx-1] += 1
        else:
            _, y = query
            idx = bisect.bisect_left(sorted_count_set, y + sorted_count_set[0])
            outputs.append(n - idx)
    print("\n".join(map(str, outputs)))


if __name__ == "__main__":
    main()
