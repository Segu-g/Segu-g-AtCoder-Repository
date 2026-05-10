import bisect

def main():
    n, m = map(int, input().split())
    sheets = [tuple(map(int, input().split())) for _ in range(m)]
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    l_sorted_sheats = [(l, r) for l, r in sheets]
    r_sorted_sheats = l_sorted_sheats.copy()
    l_sorted_sheats.sort(key=lambda item: (item[0], -item[1]))
    r_sorted_sheats.sort(key=lambda item: (item[1], item[0]))
    

    outputs = []
    for l_q, r_q in queries:
        l_started_s = bisect.bisect_left(l_sorted_sheats, l_q, key=lambda item: item[0]) 
        l_started_e = bisect.bisect_right(l_sorted_sheats, l_q, key=lambda item: item[0])
        r_started_s = bisect.bisect_left(r_sorted_sheats, r_q, key=lambda item: item[1]) 
        r_started_e = bisect.bisect_right(r_sorted_sheats, r_q, key=lambda item: item[1])

        l_s = bisect.bisect_left(l_sorted_sheats, -r_q, l_started_s, l_started_e, key=lambda item: -item[1])
        r_s = bisect.bisect_left(r_sorted_sheats, l_q, r_started_s, r_started_e, key=lambda item: item[0])
        if l_s == l_started_e or r_s == r_started_e:
            outputs.append("No")
        else:
            left_sheet = l_sorted_sheats[l_s]
            right_sheet = r_sorted_sheats[r_s]
            if left_sheet == right_sheet and l_started_e - l_s == 1 and r_started_e - r_s == 1:
                outputs.append("No")
            elif right_sheet[0] <= left_sheet[1] + 1:
                outputs.append("Yes")
            else:
                outputs.append("No")
    print("\n".join(outputs))


if __name__ == "__main__":
    main()
