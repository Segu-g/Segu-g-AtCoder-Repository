

def main():
    n = int(input())
    followers = [set() for _ in range(n)]
    for i in range(n):
        k, *a_arr = map(int, input().split())
        for a in a_arr:
            followers[a-1].add(i+1)
    print("\n".join(" ".join(map(str, [len(follower), *sorted(follower)])) for follower in followers))

if __name__ == "__main__":
    main()
