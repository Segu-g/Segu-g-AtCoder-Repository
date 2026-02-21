def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    am1_arr = [a - 1 for a in a_arr]
    rm1_arr = [i for i in range(n)]
    for i in range(n-1, -1, -1):
        rm1_arr[i] = rm1_arr[am1_arr[i]]
    r_arr = [rm1 + 1 for rm1 in rm1_arr]
    print(" ".join(map(str, r_arr)))



if __name__ == "__main__":
    main()
