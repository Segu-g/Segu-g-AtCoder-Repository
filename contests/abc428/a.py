def main():
    s, a, b, x = map(int, input().split())
    c = a + b
    n, r = x // c, x % c
    result = n * a * s + min(r, a) * s
    print(result)

if __name__ == "__main__":
    main()
