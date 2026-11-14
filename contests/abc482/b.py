
def main():
    n = 5
    on = "o"
    s_arr = [input() for _ in range(n)]
    max_count = 0
    for i in range(n):
        max_count = max(max_count, s_arr[i].count(on))
    for i in range(n):
        max_count = max(max_count, "".join(s_arr[j][i] for j in range(n)).count(on))
    max_count = max(max_count, "".join(s_arr[k][k] for k in range(n)).count(on))
    max_count = max(max_count, "".join(s_arr[k][n-1-k] for k in range(n)).count(on))
    print(n - max_count)

if __name__ == "__main__":
    main()
