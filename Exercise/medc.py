for x in range(100000000, 1000000000):
    m = x // 100000000
    o = x // 10000000 - 10 * m
    n = x // 1000000 - 100 * m - 10 * o
    e = x // 100000 - 1000 * m - 100 * o - 10 * n
    y = x // 10000 - 10000 * m - 1000 * o -100 * n - 10 * e
    s = x // 1000 - 100000 * m - 10000 * o - 1000 * n - 100 * e - 10 * y
    r = x // 100 - 1000000 * m - 100000 * o - 10000 * n - 1000 * e - 100 * y - 10 * s
    d = x // 10 - 10000000 * m - 1000000 * o - 100000 * n - 10000 * e - 1000 * y - 100 * s - 10 * r
    if s * 1000 + e * 100 + n * 10 + d + m * 1000 + o * 100 + r * 10 + e == m * 10000 + o * 1000 + n * 100 + e * 10 + y and s!=e and s!=n and s!=d and s!=m and s!=o and s!=r and s!=n and s!=y and e!=n and e!=d and e!=m and e!=o and e!=r and e!=n and e!=y and n!=d and n!=m and n!=o and n!=r and n!=n and n!=y and d!=m and d!=o and d!=r and d!=n and d!=y and m!=o and m!=r and m!=n and m!=y and o!=r and o!=n and o!=y and r!=n and r!=y and n!=y:
        print (x)
print("goodbye")