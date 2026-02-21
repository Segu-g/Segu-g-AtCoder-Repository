def main():
    n, m  = map(int, input().split())
    drink_arr = [True for _ in range(m+1)]
    given_arr = [] 
    for _ in range(n):
        l = int(input())
        x_arr = map(int, input().split())
        for x in x_arr:
            if drink_arr[x]:
                drink_arr[x] = False
                given_arr.append(x)
                break
        else:
            given_arr.append(0)
    print("\n".join(map(str, given_arr)))

if __name__ == "__main__":
    main()
