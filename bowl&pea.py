n = int(input())
positions = [1, 2, 3]

for _ in range(n):
    a, b = map(int, input().split())
    positions[a-1], positions[b-1] = positions[b-1], positions[a-1]

pea_position = positions.index(1) + 1

print(pea_position)
