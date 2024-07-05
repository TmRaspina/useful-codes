n = int(input())

b =  sum(int(digit) for digit in str(n))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


count = 0
current_num = n + 1
while True:
    if is_prime(current_num):
        count += 1
        if count == b:
            print(current_num)
            break
    current_num += 1

