import bisect

def main():
    t = int(input())
    inputs = []
    for _ in range(t):
        n, m = map(int, input().split())
        x_arr = tuple(map(int, input().split()))
        y_arr = tuple(map(int, input().split()))
        inputs.append((n, m, x_arr, y_arr))
    for i in range(t):
        solve(*inputs[i])

def solve(n, m, x_arr, y_arr):
    matrix = [[n * m for _ in range(m)] for _ in range(n)]

    mapping_arr = []
    for i in range(n):
        for j in range(m):
            upper_value = min(x_arr[i], y_arr[j])
            priority = 1 if x_arr[i] == y_arr[j] else 0
            mapping_arr.append((upper_value, priority, (i, j)))
    mapping_arr.sort()

    specified_num_set = set(x_arr).union(set(y_arr))
    rest_specified_num_set = specified_num_set.copy()
    skipped_mapping_arr = []
    for upper_value, priority, (i, j) in reversed(mapping_arr):
        if upper_value in rest_specified_num_set:
            matrix[i][j] = upper_value
            rest_specified_num_set.remove(upper_value)
        else:
            skipped_mapping_arr.append((upper_value, (i, j)))
    skipped_mapping_arr = list(reversed(skipped_mapping_arr))
    

    exist = False
    for current_value in filter(lambda v: v not in specified_num_set, range(n*m, 0, -1)):
        upper_value, (i, j) = skipped_mapping_arr.pop()
        if upper_value >= current_value:
            matrix[i][j] = current_value
        else:
            break
    else:
        exist = True
    
    if exist:
        print("Yes", flush=False)
        print("\n".join((" ".join(map(str, line)) for line in matrix)), flush=False)
    else:
        print("No", flush=False)
    
if __name__ == "__main__":
    main()
