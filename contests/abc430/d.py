from typing import TypedDict, Union

class Node(TypedDict):
    prev: Union[None, "Node"]
    cord: int
    next: Union[None, "Node"]


def calc_d(node: Node | None):
    if node is None:
        return 0
    if node["prev"] is not None and node["next"] is not None:
        dist_prev = node["cord"] - node["prev"]["cord"]
        dist_next = node["next"]["cord"] - node["cord"]
        return min(dist_prev, dist_next)
    elif node["prev"] is not None and node["next"] is None:
        return node["cord"] - node["prev"]["cord"]
    elif node["prev"] is None and node["next"] is not None:
        return node["next"]["cord"] - node["cord"]
    else:
        return 0

def main():
    n = int(input())
    x_arr = tuple((0, *map(int, input().split())))
    pxi_arr = list(zip(x_arr, range(n + 1)))
    pxi_arr.sort()

    linked_list: list[Node] = [Node(prev=None, next=None) for _ in range(n+1)]
    for i in range(n+1):
        linked_list[pxi_arr[i][1]]["cord"] = pxi_arr[i][0]
        if i + 1 < n + 1:
            linked_list[pxi_arr[i][1]]["next"] = linked_list[pxi_arr[i+1][1]]
            linked_list[pxi_arr[i+1][1]]["prev"] = linked_list[pxi_arr[i][1]]
        if 0 <= i - 1:
            linked_list[pxi_arr[i][1]]["prev"] = linked_list[pxi_arr[i-1][1]]
            linked_list[pxi_arr[i-1][1]]["next"] = linked_list[pxi_arr[i][1]]
    
    # print(list(linked_list[i]["cord"] for i in range(n+1)))
    # print(list(linked_list[i]["prev"] and linked_list[i]["prev"]["cord"] for i in range(n+1)))
    # print(list(linked_list[i]["next"] and linked_list[i]["next"]["cord"] for i in range(n+1)))
    # print(list(linked_list[i]["cord"] for i in range(n+1)))

    d_sum = 0
    for i in range(n+1):
        d_sum += calc_d(linked_list[i])
    
    d_sum_history = []
    for i in range(n, 0, -1):
        d_sum_history.append(d_sum)
        current_node  = linked_list[i]
        prev_node = current_node["prev"]
        next_node = current_node["next"]

        current_d_local_sum = calc_d(current_node) + calc_d(prev_node) + calc_d(next_node)
        if prev_node is not None:
            prev_node["next"] = next_node
        if next_node is not None:
            next_node["prev"] = prev_node
        updated_d_local_sum = calc_d(prev_node) + calc_d(next_node)
        d_local_sum_diff = updated_d_local_sum - current_d_local_sum
        d_sum += d_local_sum_diff
    
    print("\n".join(map(str, reversed(d_sum_history))))
        


if __name__ == "__main__":
    main()
