

def main():
    n, m = map(int, input().split())
    a_arr = tuple(map(int, input().split()))
    b_arr = tuple(map(int, input().split()))

    a_pair_sum_arr = tuple(map(sum, zip(a_arr[:-1], a_arr[1:])))
    d_arr = tuple(b - ps for ps, b in zip(a_pair_sum_arr, b_arr))
    

    for i in range(n-1):
        pass
        
if __name__ == "__main__":
    main()
