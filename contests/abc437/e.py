import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def main():
    n = int(input())
    target_arr = [tuple(map(int, input().split())) for _ in range(n)]
    children_dict_arr: list[dict[int, list[int]]] = [defaultdict(list) for _ in range(n+1)]
    for i, (x, y) in enumerate(target_arr):
        children_dict_arr[x][y].append(i+1)
    output = []
    listup([0], children_dict_arr, output)
    print(" ".join(map(str, output[1:])))
    
def listup(
    current_targets: list[int],
    children_dict_arr: list[dict[int, list[int]]],
    output: list[int]
):
    current_targets.sort()
    for current_target in current_targets:
        output.append(current_target)
    
    children_dict = defaultdict(list)
    for current_target in current_targets:
        unmarged_dict = children_dict_arr[current_target]
        for value, children_list in unmarged_dict.items():
            children_dict[value].extend(children_list)
    
    children_keys = list(children_dict.keys())
    children_keys.sort()
    for children_key in children_keys:
        listup(children_dict[children_key], children_dict_arr, output)
    


if __name__ == "__main__":
    main()
