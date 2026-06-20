

def main():
    s = input()
    print("".join(filter(lambda c: c in "0123456789", s)))

if __name__ == "__main__":
    main()
