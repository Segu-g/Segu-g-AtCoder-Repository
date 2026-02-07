def main():
    x = int(input())
    n = int(input())
    w_arr = tuple(map(int, input().split()))
    q = int(input())

    queries = tuple(int(input()) for _ in range(q))

    current_weight = x
    p_flags = [False for _ in range(n)]
    weight_outputs = []
    for p in queries:
        p -= 1
        if p_flags[p]:
            current_weight -= w_arr[p]
        else:
            current_weight += w_arr[p]
        p_flags[p] = not p_flags[p]
        weight_outputs.append(current_weight)
    print("\n".join(map(str, weight_outputs)))


if __name__ == "__main__":
    main()
