def main():
    n, k = map(int, input().split())
    a_arr = tuple(map(int, input().split()))
    a_mod_k_arr = [a % k for a in a_arr]
    a_mod_k_arr.sort()
    cyclic_distance = a_mod_k_arr[0] + k - a_mod_k_arr[-1]
    distance_arr = list(a_j - a_i for a_i, a_j in zip(a_mod_k_arr[:-1], a_mod_k_arr[1:]))
    max_distance = max(cyclic_distance, max(distance_arr)) if len(distance_arr) != 0 else k 
    print(k - max_distance)

if __name__ == "__main__":
    main()
