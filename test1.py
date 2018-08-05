def pow0(x, n):
    value = 1
    for i in range(n): value *= x
    return value


x = 4989
n = 1000000
mod = 123456789

answer = pow0(x, n) % mod

print(answer)
