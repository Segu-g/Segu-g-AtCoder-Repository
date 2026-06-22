
def main():
    x, y = map(int, input().split())
    if x*9 == y * 16:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
