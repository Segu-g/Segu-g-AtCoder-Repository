import heapq

def main():
    t = int(input())
    for _ in range(t):
        solve()

def solve():
    n, m = map(int, input().split())
    a_arr = list(map(int, input().split()))
    a_arr.sort()
    first_half = a_arr[:(n + 1)//2].copy()
    second_half = a_arr[(n + 1)//2:].copy()
    heapq.heapify(first_half)
    heapq.heapify(second_half)
    
    rest_m = m
    while rest_m > 0 and ((first_half[0] + 1) // 2 >= second_half[0]):
        pass


    



if __name__ == "__main__":
    main()
