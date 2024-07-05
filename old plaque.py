def find_plaque(x, y):
    # پیدا کردن لایه
    layer = max(abs(x), abs(y))
    
    if layer == 0:
        return 1
    
    # پیدا کردن شروع پلاک در لایه
    start_plaque = 1 + 4 * layer * (layer - 1)
    
    if x == layer:
        return start_plaque + (y + layer)
    if y == -layer:
        return start_plaque + (3 * layer + x)
    if x == -layer:
        return start_plaque + (5 * layer - y)
    return start_plaque + (7 * layer - x)

# خواندن ورودی‌ها
# import sys
# input = sys.stdin.read
# data = input().split()

t = int(input())
index = 1
results = []

for _ in range(t):
    data = input().split()
    x = int(data[0])
    y = int(data[1])
    results.append(find_plaque(x, y))

# چاپ خروجی‌ها
for result in results:
    print(result)
