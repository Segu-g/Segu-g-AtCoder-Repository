import itertools

def main():
    n, d = map(int, input().split())
    st_arr = [tuple(map(int, input().split())) for _ in range(n)]
    st_arr = tuple(filter(lambda st: (st[1] - st[0]) >= d, st_arr))

    start_times = [(st[0], i) for i, st in enumerate(st_arr)]
    end_times = [(st[1], i) for i, st in enumerate(st_arr)]

    start_times.sort(reverse=True)
    end_times.sort(reverse=True)

    timepoints = set(itertools.chain((0,), (st[0] for st in st_arr), (st[1] for st in st_arr)))
    
    current_target = set()
    count = 0
    for t in range(min(timepoints), max(timepoints)):
        while start_times and start_times[-1][0] <= t:
            _, i = start_times.pop()
            current_target.add(i)
        while end_times and end_times[-1][0] < t + d:
            _, i = end_times.pop()
            current_target.remove(i)
        count += (len(current_target) * (len(current_target) - 1)) // 2
    print(count)


if __name__ == "__main__":
    main()
