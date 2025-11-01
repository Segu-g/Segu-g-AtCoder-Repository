from collections import defaultdict
import bisect

def main():
    n, m, c = map(int, input().split())
    a_arr = tuple(map(int, input().split()))

    ai_count = defaultdict(int)
    ai_count[0] = 0
    ai_count[m] = 0

    for a in a_arr:
        ai_count[a] += 1

    
    
    x_arr = list(ai_count.keys())
    x_arr.sort()

    x_arr_rep = tuple((*x_arr, *x_arr))

    x_count_cumsum = []
    current_cumsum = 0
    for x in x_arr_rep:
        current_cumsum += ai_count[x]
        x_count_cumsum.append(current_cumsum)
    
    count_x_arr = []
    
    right = 0
    for i in range(len(x_arr)):
        start = i
        while x_count_cumsum[right] - x_count_cumsum[start] < c:
            right += 1
        count_x_arr.append(x_count_cumsum[right] - x_count_cumsum[start])

    total = 0
    prev_x = 0
    prev_count = count_x_arr[0]
    for x, count in zip(x_arr, count_x_arr):
        diff = x - prev_x
        total += diff * prev_count
        prev_x = x
        prev_count = count
    # print(x_arr)
    # print(ai_count)
    # print(count_x_arr)
    print(total)



if __name__ == "__main__":
    main()
