n, m = map(int, input().split())
requests = []
computers = [0] * n

for _ in range(m):
    s, l = map(int, input().split())
    requests.append((s, l))
    
computers = [0] * n
for s, l in requests:
    answer = False

    for start in range(s-1, n-l+1):
        if all(computers[start + i] == 0 for i in range(l)):
            for i in range(start, start + l):
                computers[i] = 1
            answer = True
            break
    
    
    print(''.join(map(str, computers)))
