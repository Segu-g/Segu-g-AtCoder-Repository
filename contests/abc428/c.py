


def main():
    q = int(input())
    queries = [input().split() for _ in range(q)]
    stack = [0]
    for query in queries:
        op, *args = query
        if op == "1":
            c = args[0]
            prev_state = stack[-1]
            if c == "(":
                diff = 1
            else:
                diff = -1
            if prev_state is None or prev_state + diff < 0:
                current_state = None
            else:
                current_state = prev_state + diff
            stack.append(current_state)
        else:
            stack.pop()
        if stack[-1] == 0:
            print("Yes", flush=False)
        else:
            print("No", flush=False)

if __name__ == "__main__":
    main()
