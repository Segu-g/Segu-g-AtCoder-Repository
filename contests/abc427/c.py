import itertools 

n, m = map(int, input().split())

edges = []

for _ in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    edges.append((u, v))

minimum_count = len(edges)
for _colors in itertools.product((False, True), repeat=n-1):
    colors = (False, *_colors)
    count = 0
    for u, v in edges:
        if colors[u] == colors[v]:
            count += 1
    minimum_count = min(minimum_count, count)

print(minimum_count)