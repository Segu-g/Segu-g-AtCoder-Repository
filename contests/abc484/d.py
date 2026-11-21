
def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    
    compacted_a_arr = []
    current_state = (a_arr[0], 0)
    for a in a_arr:
        if current_state[0] != a:
            compacted_a_arr.append(current_state)
            current_state = (a, 1)
        else:
            current_state = (a, current_state[1] + 1)   
    compacted_a_arr.append(current_state)


    seq_counts = dict()
    for (a, c_num) in compacted_a_arr:
        if a not in seq_counts:
            seq_counts[a] = 0            
        seq_counts[a] += 1
    seq_counts[None] = 0
    
    pattern = 1
    prev_a = None
    for i, (a, c_num) in enumerate(compacted_a_arr):
        seq_counts[a] -= 1
        pattern += c_num * (len(compacted_a_arr) - i - 1 - seq_counts[a] - seq_counts[prev_a]) + seq_counts[a]
        prev_a = a

    print(pattern)
    

if __name__ == "__main__":
    main()
