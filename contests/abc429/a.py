def main():
    n, m = map(int, input().split())
    for i in range(n):
        if i < m:
            message = "OK"
        else:
            message = "Too Many Requests"
        print(message, flush=False)

if __name__ == "__main__":
    main()
