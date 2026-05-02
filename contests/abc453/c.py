from collections import defaultdict

def main():
    n = int(input())
    l_arr = tuple(map(int, input().split()))
    current_pos_dict: defaultdict[int, int] = defaultdict(int)
    current_pos_dict[0] = 0
    for l_value in l_arr:
        next_pos_dict: defaultdict[int, int] = defaultdict(int)
        for current_pos, current_value  in current_pos_dict.items():
            for diff in (l_value, -l_value):
                next_pos = current_pos + diff
                is_current_non_negative = (current_pos >= 0)
                is_next_non_negative =  (next_pos >= 0)
                next_value = current_value + 1 if (is_current_non_negative ^ is_next_non_negative) else current_value
                next_pos_dict[next_pos] = max(next_pos_dict[next_pos], next_value)
        current_pos_dict = next_pos_dict
    print(max(current_pos_dict.values()))

if __name__ == "__main__":
    main()
