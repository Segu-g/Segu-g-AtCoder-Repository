MOD = 998244353

def main():
    n, m = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    a_arr.sort()
    b_arr.sort()

    current_result = 0

    while not (not a_arr and not b_arr):
        if not b_arr or (a_arr and a_arr[-1] > b_arr[-1]):
            current_result += a_arr.pop() * (len(b_arr) - (m - len(b_arr)))
            current_result %= MOD
        else:
            current_result += b_arr.pop() * (len(a_arr) - (n - len(a_arr)))
            current_result %= MOD
    print(current_result)


if __name__ == "__main__":
    main()