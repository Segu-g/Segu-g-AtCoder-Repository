def main():
    n, x, y = map(int, input().split())
    a_arr = list(map(int, input().split()))
    
    weight_diff = y - x
    a_arr.sort()
    # 小さい飴だけの時の重さの差
    a_diff_arr = tuple(a_arr[-1] - a  for a in a_arr)
    weight_offset_arr = tuple(a_diff * x for a_diff in a_diff_arr)
    diff_num_arr = [] 
    for weight_offset in weight_offset_arr:
        if weight_diff == 0:
            if weight_offset == 0:
                diff_num_arr.append(0)     
            else:
                diff_num_arr.append(a_arr[-1] + 1)
        elif weight_offset % weight_diff == 0:
            diff_num_arr.append(weight_offset // weight_diff)
        else:
            diff_num_arr.append(a_arr[-1] + 1)
    
    diff_rest_n_arr = tuple(a - dn for a, dn in zip(a_arr, diff_num_arr))

    min_diff_rest_n = min(diff_rest_n_arr)
    if min_diff_rest_n < 0:
        print(-1)
    else:
        print(min_diff_rest_n * n + sum(diff_num_arr))

if __name__ == "__main__":
    main()
