import heapq

n,q = map(int, input().split())

managed_version = 0
unmanaged_versions = []
results = []
for x, y in (map(int, input().split()) for _ in range(q)):
    update_count = 0
    if managed_version < x:
        update_count += x - managed_version
        managed_version = x
    while len(unmanaged_versions) and unmanaged_versions[0][0] <= x:
        v, c = heapq.heappop(unmanaged_versions)
        update_count += c
    results.append(update_count)
    heapq.heappush(unmanaged_versions, (y, update_count))
print("\n".join(map(str, results)))