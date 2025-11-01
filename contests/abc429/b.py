from collections import defaultdict

def main():
    n, m = map(int, input().split())
    a_arr = tuple(map(int, input().split()))

    sum_a = sum(a_arr)
    sub_a_arr = tuple(sum_a - a for a in a_arr)
    if m in sub_a_arr:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
