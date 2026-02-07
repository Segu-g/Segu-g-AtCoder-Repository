import numpy as np

def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    a_cumsum_arr = np.zeros(n+1, dtype=int)
    a_cumsum_arr[1:] = np.cumsum(a_arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            total = a_cumsum_arr[j+1] - a_cumsum_arr[i]
            for k in range(i, j+1):
                if total % a_arr[k] == 0:
                    break
            else:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
