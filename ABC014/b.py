n, x = map(int, input().split())
a = list(map(int, input().split()))
x = bin(x)[2:]
x = '0' * (n - len(x)) + x
ans = 0
print(x)
for i in range(n):
    if x[i] == '1':
        ans += a[i]
print(ans)