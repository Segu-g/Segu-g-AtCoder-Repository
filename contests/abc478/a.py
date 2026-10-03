def main():
    n, m = map(int, input().split())
    ans = [(m // n) + (1 if (i < (m % n)) else 0) for i in range(n)]
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()
