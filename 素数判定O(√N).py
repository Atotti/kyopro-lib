# O(√N)
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


X = int(input())
for i in range(100003):
    if is_prime(X + i):
        print(X + i)
        quit()
