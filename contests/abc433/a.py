def main():
    x, y, z = map(int, input().split())
    a = x - z * y
    b = z - 1
    if (a % b) == 0 and (a // b) >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
