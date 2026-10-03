def main():
    n, k = map(int, input().split())
    a_arr = tuple(map(int, input().split()))
    sorted_a_arr = sorted(a_arr)

    diff = [a == sa for a, sa in zip(a_arr, sorted_a_arr)]
    if all(diff):
        print("Yes")
        return

    first_diff_i = diff.index(False)
    last_diff_reversed_i = tuple(reversed(diff)).index(False)
    last_diff_i = n - last_diff_reversed_i - 1
    if last_diff_i - first_diff_i + 1 > k:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()
