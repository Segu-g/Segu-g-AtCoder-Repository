import itertools

def main():
    a_mat = [tuple(map(int, input().split())) for _ in range(3)]
    p_result = 0
    for b_arr in itertools.permutations((4, 5, 6), 3):
        p = 1
        for a_arr, b in zip(a_mat, b_arr):
            p *= a_arr.count(b) / len(a_arr)
        p_result += p
    print(p_result)    


if __name__ == "__main__":
    main()
