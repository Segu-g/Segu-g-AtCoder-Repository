import bisect

def main():
    n, k = map(int, input().split())
    l_arr = list()
    a_mat= list()
    for _ in range(n):
        l_i, *a_arr_i = map(int, input().split())
        l_arr.append(l_i)
        a_mat.append(a_arr_i)
    c_arr = tuple(map(int, input().split()))

    b_index_arr = [0]
    for i in range(n):
        b_index_arr.append(b_index_arr[-1] + l_arr[i] * c_arr[i])
    
    i_k = bisect.bisect_right(b_index_arr, k-1) - 1
    b_pad = (k-1) - b_index_arr[i_k]
    print(a_mat[i_k][b_pad % l_arr[i_k]])

if __name__ == "__main__":
    main()
