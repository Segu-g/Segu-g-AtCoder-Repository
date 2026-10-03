

def main():
    n, m = map(int, input().split())
    a_arr = tuple(map(int, input().split()))
    b_arr = tuple(map(int, input().split()))


    cost_add = 0
    cost_nonadd = 0

    for i in range(n-1):
        mod = a_arr[i] + a_arr[i+1] % 2 
        if mod == b_arr[i]:
            cost_add, cost_nonadd = cost_add + 1, cost_nonadd
        else:
            cost_add, cost_nonadd = cost_nonadd + 1, cost_add
    print(min(cost_add, cost_nonadd))

if __name__ == "__main__":
    main()
