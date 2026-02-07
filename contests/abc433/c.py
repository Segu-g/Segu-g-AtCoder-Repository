def main():
    s = input()
    n_arr = tuple(map(int, s))
    
    n_segment_arr = []
    current_n = None
    current_conut = 0

    for n in n_arr:
        if current_n == n:
            current_conut += 1
        else:
            if current_n is not None:
                n_segment_arr.append((current_n, current_conut))
            current_n = n
            current_conut = 1
            
    else:
        n_segment_arr.append((current_n, current_conut))

    pattern_count = 0
    for prev, post in zip(n_segment_arr[:-1], n_segment_arr[1:]):
        if prev[0] + 1 == post[0]:
            pattern_count += min(prev[1], post[1])
    print(pattern_count)

if __name__ == "__main__":
    main()
