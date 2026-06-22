
def main():
    n, x = input().split()
    n = int(n)
    s_arr = tuple(input() for _ in range(n))
    seat = "ABCDE"
    seat_i = seat.index(x)
    for s in s_arr:
        if s[seat_i] == "o":
            flag = True
            break
    else:
        flag = False
    print("Yes" if flag else "No")

if __name__ == "__main__":
    main()
