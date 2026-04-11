# https://atcoder.jp/contests/abc450/tasks/abc450_e

def main():
    x = input()
    y = input()
    len_x, len_y = len(x), len(y)

    def get_count(c: str, end):
        x_c = x.count(c)
        y_c = y.count(c)
        index = 3
        n_x1, n_y1 = 1, 0
        n_x2, n_y2 = 0, 1
        n_x3, n_y3 = n_x1+n_x2, n_y1+n_y2
        len_3 = n_x3 * len_x + n_y3 * len_y
        while len_3 < end:
            index = index + 1
            n_xnext, n_ynext = n_x2+n_x3, n_y2+n_y3
            n_x1, n_y1 = n_x2, n_y2
            n_x2, n_y2 = n_x3, n_y3
            n_x3, n_y3 = n_xnext, n_ynext
            len_3 = n_x3 * len_x + n_y3 * len_y
        count = 0
        len_2 = n_x2 * len_x + n_y2 * len_y
        while 3 <= index and end != 0:
            if  len_2 <= end:
                count += x_c * n_x2 + y_c * n_y2
                end -= len_2

                index = index - 1
                n_xprev, n_yprev = n_x2-n_x1, n_y2-n_y1
                n_x3, n_y3 = n_x2, n_y2
                n_x2, n_y2 = n_x1, n_y1
                n_x1, n_y1 = n_xprev, n_yprev
                
                index = index - 1
                n_xprev, n_yprev = n_x2-n_x1, n_y2-n_y1
                n_x3, n_y3 = n_x2, n_y2
                n_x2, n_y2 = n_x1, n_y1
                n_x1, n_y1 = n_xprev, n_yprev
            else:
                index = index - 1
                n_xprev, n_yprev = n_x2-n_x1, n_y2-n_y1
                n_x3, n_y3 = n_x2, n_y2
                n_x2, n_y2 = n_x1, n_y1
                n_x1, n_y1 = n_xprev, n_yprev
            len_2 = n_x2 * len_x + n_y2 * len_y
        if index == 2:
            count += y[:end].count(c)
        elif index == 1:
            count += x[:end].count(c)
        
        return count

    q = int(input())
    queries = []
    for _ in range(q):
        l, r, c = input().split()
        l, r = int(l), int(r)
        queries.append((l, r, c))
    for l, r, c in queries:
        print(get_count(c, r+1) - get_count(c, l), flush=False)
    print(end="")


if __name__ == "__main__":
    main()
