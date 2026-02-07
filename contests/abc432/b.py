def main():
    x = int(input())
    x_str = str(x)
    c_arr = sorted(x_str)
    non_zero_num = "".join(filter(lambda c: c!="0", c_arr))
    ans = non_zero_num[0] + ("0" * c_arr.count("0")) + non_zero_num[1:]
    print(ans)

if __name__ == "__main__":
    main()
