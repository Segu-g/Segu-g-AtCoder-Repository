import numpy as np
import bisect

def main():
    n, a, b = map(int, input().split())
    s = input()
    a_onehot = tuple(1 if c == "a" else 0  for c in s)
    b_onehot = tuple(1 if c == "b" else 0  for c in s)
    a_cumsum = np.zeros(n+1, dtype=int)
    b_cumsum = np.zeros(n+1, dtype=int)
    a_cumsum[1:] = np.cumsum(a_onehot)
    b_cumsum[1:] = np.cumsum(b_onehot)

    count = 0
    for i in range(n):
        a_prev_sum = a_cumsum[i]
        b_prev_sum = b_cumsum[i]
        a_right = bisect.bisect_right(a_cumsum, a_prev_sum + a - 1)
        b_left = bisect.bisect_left(b_cumsum, b_prev_sum + b)
        count += max(b_left - a_right, 0)
    print(count)


if __name__ == "__main__":
    main()
