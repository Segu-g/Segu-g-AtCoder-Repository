def main():
    n = int(input())
    a_arr = tuple(map(int, input().split()))
    result = []
    for i in range(n):
        ai = a_arr[i]
        for j in range(i-1, -1, -1):
            if a_arr[j] > ai:
                result.append(j+1)
                break
        else:
            result.append(-1)
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()
