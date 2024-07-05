from collections import deque

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def bfs_path(matrix, start, end, n):
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    queue = deque([(start[0], start[1], "")])
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, path = queue.popleft()

        if (x, y) == (end[0], end[1]):
            return path

        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and is_prime(matrix[nx][ny]):
                visited.add((nx, ny))
                queue.append((nx, ny, path + move))
    
    return "No Monaseb Masir!"

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        matrix = []
        
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            index += n
            matrix.append(row)
        
        start = (int(data[index]) - 1, int(data[index + 1]) - 1)
        index += 2
        end = (int(data[index]) - 1, int(data[index + 1]) - 1)
        index += 2
        
        result = bfs_path(matrix, start, end, n)
        results.append(result)
    
    for result in results:
        print(result)

solve()
