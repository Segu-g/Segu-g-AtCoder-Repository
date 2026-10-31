

def main():
    q = int(input())

    hash_map = dict()
    current_idx = 1
    outputs = []
    for _ in range(q):
        query = input()
        if query in hash_map:
            outputs.append(hash_map[query])
        else:
            hash_map[query] = current_idx
            outputs.append(current_idx)
            current_idx += 1
    print("\n".join(map(str, outputs)))

if __name__ == "__main__":
    main()
