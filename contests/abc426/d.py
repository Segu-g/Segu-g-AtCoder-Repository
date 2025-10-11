t = int(input())
resutls = []
for _ in range(t):
    n = int(input())
    s = input()
    zero_max_seq = 0
    one_max_seq = 0
    zero_count = 0
    one_count = 0

    zero_seq = 0
    one_seq = 0
    for c in s:
        if c == "0":
            zero_count += 1
            if one_seq != 0:
                one_max_seq = max(one_max_seq, one_seq)
                one_seq = 0
            zero_seq += 1
        else:
            one_count += 1
            if zero_seq != 0:
                zero_max_seq = max(zero_max_seq, zero_seq)
                zero_seq = 0
            one_seq += 1
    one_max_seq = max(one_max_seq, one_seq)
    zero_max_seq = max(zero_max_seq, zero_seq)

    one_cost = (n - one_max_seq) + (one_count - one_max_seq)
    zero_cost = (n - zero_max_seq) + (zero_count - zero_max_seq)
    resutls.append(min(one_cost, zero_cost))
print("\n".join(map(str, resutls)))
