

def main():
    n = int(input())
    loss = 0
    for _ in range(n):
        a, b, s = input().split()
        a, b = int(a), int(b)
        otsuri = b - a
        if s == "keep":
            loss += otsuri
    print(loss)

if __name__ == "__main__":
    main()
