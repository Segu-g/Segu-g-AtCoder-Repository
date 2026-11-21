
def main():
    k = int(input())
    a_arr = tuple(map(int, input().split()))
    a_set = set(a_arr)
    if 9 in a_set:
        print(min(a_set))
    else:
        print(-1)

if __name__ == "__main__":
    main()
