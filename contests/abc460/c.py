from collections import deque

def main():
    n, m = map(int, input().split())
    a_arr = tuple(map(int, input().split()))
    b_arr = tuple(map(int, input().split()))
    
    weight_arr = [(a * 2, 1) for a in a_arr] + [(b, 0) for b in b_arr]
    weight_arr.sort()

    b_count = 0
    count = 0
    for weight, type  in weight_arr:
        if type == 0:
            b_count += 1
        elif type == 1 and b_count != 0:
            count += 1 
            b_count -= 1
    print(count)

if __name__ == "__main__":
    main()
