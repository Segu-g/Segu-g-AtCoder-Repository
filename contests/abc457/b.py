def main():
    n = int(input())
    l_arr = list()
    a_mat= list()
    for _ in range(n):
        l_i, *a_arr_i = map(int, input().split())
        l_arr.append(l_i)
        a_mat.append(a_arr_i)
    x, y = tuple(map(int, input().split()))
    print(a_mat[x-1][y-1])

if __name__ == "__main__":
    main()
