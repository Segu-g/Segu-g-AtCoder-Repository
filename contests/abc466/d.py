from collections import defaultdict
def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))

    max_seq_len_dict = defaultdict(int)
    for a in reversed(a_arr):
        max_seq_len_dict[a] = max(max_seq_len_dict[a] ,max_seq_len_dict[a+1] + 1)
    print(max(max_seq_len_dict.values()))

if __name__ == "__main__":
    main()
