
def main():
    n = int(input())
    x_arr = tuple(map(int, input().split()))
    x_min = x_arr[0]
    x_max = x_arr[-1]
    if n == 1:
        print("0")
        return

    outputs = []
    for i in range(n):
        t_result = float("inf")
        if i-1 >= 0:
            t_offset = (x_arr[i] - x_arr[i-1]) // 2
            t_min = t_offset + max((x_max - x_arr[i]) // 2, (x_arr[i-1] - x_min) // 2)
            t_result = min(t_min, t_result)
        if i+1 < n:
            t_offset = (x_arr[i+1] - x_arr[i]) // 2
            t_min = t_offset + max((x_max - x_arr[i+1]) // 2, (x_arr[i] - x_min) // 2)
            t_result = min(t_min, t_result) 
        outputs.append(t_result)
    print("\n".join(map(str, outputs)))

if __name__ == "__main__":
    main()
