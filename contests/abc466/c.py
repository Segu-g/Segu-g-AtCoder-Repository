from collections import deque

def main():
    t = int(input())
    outputs = []
    for _ in range(t):
        outputs.append(solve())
    print("\n".join(map(str, outputs)))

def solve():
    n, d = map(int, input().split())
    a_arr = tuple(map(int, input().split()))
    b_arr = tuple(map(int, input().split()))

    queue = deque()
    for i, (a, b) in enumerate(zip(a_arr, b_arr)):
        queue.append([i, a])
        
        consume = b
        while consume > 0:
            if consume >= queue[0][1]:
                _, c = queue.popleft()
                consume -= c
            else:
                queue[0][1] -= consume
                consume = 0
        
        while len(queue) > 0 and (queue[0][0] + d) <= i:
            queue.popleft()

    total = 0
    for i, rest in queue:
        total += rest
    return total

if __name__ == "__main__":
    main()