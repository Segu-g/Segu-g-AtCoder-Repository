h, w, n = map(int, input().split())
a_mat = [tuple(map(int, input().split())) for _ in range(h)]
b_arr = [int(input()) for _ in range(n)]
b_set = set(b_arr)
count_arr = [sum(a_mat[i][j] in b_set for j in range(w)) for i in range(h)]
print(max(count_arr))
