from collections import defaultdict, deque

def main():
    n, q = map(int, input().split())

    seqs_dic: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for _ in range(q):
        l, r, x = map(int, input().split())
        seqs_dic[x].append((l-1, r))

    merged_seqs: list[tuple[int, int]] = []
    for x, seqs in seqs_dic.items():
        simplified_seqs = []
        seqs.sort(reverse=True)
        current_seq = seqs.pop()
        while len(seqs) != 0:
            target_seq = seqs.pop()
            if current_seq[1] >= target_seq[0]:
                current_seq = (current_seq[0], max(current_seq[1], target_seq[1]))
            else:
                simplified_seqs.append(current_seq)
                current_seq = target_seq
        simplified_seqs.append(current_seq)

        merged_seqs.extend(simplified_seqs)
    
    diff_arr = [0 for _ in range(n+1)]
    for (l, rp) in merged_seqs:
        diff_arr[l] += 1
        diff_arr[rp] -=1

    result_arr = []
    current_active_seq = 0
    for i in range(n):
        current_active_seq += diff_arr[i]
        result_arr.append(current_active_seq)

    print(" ".join(map(str, result_arr)))


if __name__ == "__main__":
    main()
