def main():
    c_map = (2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9)
    n = int(input())
    s_arr = input().split()
    c_arr = list()
    for s in s_arr:
        c_idx = ord(s[0]) - ord("a")
        c_arr.append(c_map[c_idx])
    print("".join(map(str, c_arr)))

if __name__ == "__main__":
    main()
