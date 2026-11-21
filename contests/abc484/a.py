
def main():
    b, r = map(int, input().split())
    h, w = 30 - b, 30 - r
    print(h * w)

if __name__ == "__main__":
    main()
