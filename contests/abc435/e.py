def main():
    n, q = map(int, input().split())
    query_arr = [tuple(map(int, input().split())) for _ in range(q)]
    segment_set = set()
    for l, r in query_arr:
        segment_set.add(l-1)
        segment_set.add(r)
    segment_set.add(0)
    segment_set.add(n)
    
    segment_arr = list(segment_set)
    segment_arr.sort()

    pos_to_index = dict()
    for i, pos in enumerate(segment_arr):
        pos_to_index[pos] = i

    n_s = len(segment_arr) - 1
    
    lg_expanded_n_s = 1
    for i in range(1, 21):
        if n_s <= 2 ** i:
            lg_expanded_n_s = i
            break
    expanded_n_s = 2 ** lg_expanded_n_s

    print(segment_arr)
    
    segment_tree = [0 for _ in range(expanded_n_s * 2)]
    for left, right in zip(segment_arr[:-1], segment_arr[1:]):
        index = pos_to_index[left]
        segment_tree[expanded_n_s + index] = right - left
    for i in range(expanded_n_s * 2 - 1, 1, -1):
        segment_tree[i//2] += segment_tree[i]
    
    for l, r in query_arr:
        l, r = l-1, r
        left_index = pos_to_index[l]
        right_index = pos_to_index[r]
        query_update(segment_tree, left_index, right_index)
        print(segment_tree[1])


def propagete_upper(
    segment_tree: list[int],
    index: int
):
    if index == 1:
        return
    segment_tree[index//2] = segment_tree[index//2] + segment_tree[index//2+1]

def query_update(
    segment_tree: list[int],
    leaf_left_index: int,
    leaf_right_index: int,
    current_segment_num = 1
):
    print(current_segment_num, leaf_left_index, leaf_right_index)
    leaf_segment_size = len(segment_tree) // 2
    current_segment_size = leaf_segment_size // current_segment_num
    current_segment_left_index = leaf_left_index // current_segment_size
    current_segment_right_index = leaf_right_index // current_segment_size
    target_index = current_segment_num + current_segment_left_index
    if segment_tree[target_index] == 0:
        return
    if current_segment_left_index + 1 == current_segment_right_index:
        segment_tree[target_index] = 0
        propagete_upper(segment_tree, target_index)
    next_segment_num = current_segment_num * 2
    next_segment_size = leaf_segment_size // next_segment_num
    left_element_left_index = leaf_left_index
    left_element_right_index = ((leaf_left_index + next_segment_size) // next_segment_size) * next_segment_size
    right_element_left_index = left_element_right_index
    right_element_right_index = leaf_right_index
    query_update(segment_tree, left_element_left_index, left_element_right_index, next_segment_num)
    query_update(segment_tree, right_element_left_index, right_element_right_index, next_segment_num)
    


if __name__ == "__main__":
    main()
