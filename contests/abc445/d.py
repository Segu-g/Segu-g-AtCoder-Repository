import bisect


def main():
    orig_h, orig_w, n = map(int, input().split())
    piece_arr = [tuple(map(int, input().split())) for _ in range(n)]
    h_sorted_index = list(range(n))
    h_sorted_index.sort(key=lambda i: piece_arr[i][0])
    w_sorted_index = list(range(n))
    w_sorted_index.sort(key=lambda i: piece_arr[i][1])

    flag_arr = [False for _ in range(n)]
    current_size = [orig_h, orig_w]
    cords = [(0, 0) for _ in range(n)]
    while current_size[0] != 0 and current_size[1] != 0:
        hi = bisect.bisect_left(h_sorted_index, current_size[0], key=lambda i: piece_arr[i][0])
        wi = bisect.bisect_left(w_sorted_index, current_size[1], key=lambda i: piece_arr[i][1])
        # print(hi, piece_arr[h_sorted_index[hi]] if hi < n else "")
        # print(wi, piece_arr[w_sorted_index[wi]] if wi < n else "")

        split_dim = 1
        non_split_dim = 1 - split_dim
        for i in range(hi, n):
            piece_i = h_sorted_index[i]
            if flag_arr[piece_i]:
                break
            piece = piece_arr[piece_i]
            if piece[non_split_dim] != current_size[non_split_dim]:
                break
            flag_arr[piece_i] = True
            cords[piece_i] = ((orig_h+1 - current_size[0], orig_w+1 - current_size[1]))
            current_size[split_dim] -= piece[split_dim]

        split_dim = 0
        non_split_dim = 1 - split_dim
        for i in range(wi, n):
            piece_i = w_sorted_index[i]
            if flag_arr[piece_i]:
                break
            piece = piece_arr[piece_i]
            if  piece[non_split_dim] != current_size[non_split_dim]:
                break
            flag_arr[piece_i] = True
            cords[piece_i] = ((orig_h+1 - current_size[0], orig_w+1 - current_size[1]))
            current_size[split_dim] -= piece[split_dim]
    
    print("\n".join(f"{cord[0]} {cord[1]}" for cord in cords))


if __name__ == "__main__":
    main()
