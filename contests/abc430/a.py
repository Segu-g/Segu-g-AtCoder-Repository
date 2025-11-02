

def main():
    a, b, c, d = map(int, input().split())
    output = "No"
    if a <= c and d < b:
        output = "Yes"
    print(output)

if __name__ == "__main__":
    main()
