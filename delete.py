def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def count_pairs(N, K):
    count = 0

    for x in range(1, N+1):
        for y in range(1, N+1):
            if gcd(x, y) == K:
                count += 1

    return count


N = 4
K = 2
result = count_pairs(N, K)
print(result)