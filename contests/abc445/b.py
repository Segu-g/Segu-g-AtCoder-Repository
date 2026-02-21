def main():
    n = int(input())
    s_arr = [input() for _ in range(n)]
    m = max(len(s) for s in s_arr)
    t_arr = []
    for s in s_arr:
        k = (m - len(s)) // 2
        t_arr.append(f"{'.' * k}{s}{'.' * k}")
    print("\n".join(t_arr))


if __name__ == "__main__":
    main()
