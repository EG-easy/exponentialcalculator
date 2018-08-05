def pow1(x, n):
    if n == 0: return 1
    value = pow1(x, int(n / 2))
    value *= value
    if n % 2 == 1: value *= x
    return value


x = 4989
n = 1000000
mod = 123456789

answer = pow1(x, n) % mod

print(answer)
