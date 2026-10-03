

def main():
    h, w = map(int, input().split())
    if 25 * h * h <= w * 100 * 100:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
