def main():
    n = int(input())
    connected_verteies: list[set] = [set() for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        connected_verteies[a].add(b)
        connected_verteies[b].add(a)
    
    def get_leafs(parent: int, vertex: int, current_depth: int) -> list[tuple[int, int]]:
        if len(connected_verteies[vertex]) == 1:
            return (vertex, current_depth)

        leafs: list[tuple[int, int]] = []
        for child in connected_verteies[vertex]:
            if child == parent:
                continue
            leafs.append(get_leafs(vertex, child, current_depth+1))
        return leafs

if __name__ == "__main__":
    main()
