from operator import itemgetter
n = int(input())
ab = []
a = []
b = []
flag = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    ab.append(tmp)
while True:
    if flag == 0:
        flag = 1
        ab.sort(reverse=True, key=itemgetter(0))
        a.append(ab.pop(0)[0])
    else:
        flag = 0
        ab.sort(reverse=True, key=itemgetter(1))
        b.append(ab.pop(0)[1])
    if len(ab) == 0:
        break
print(sum(a) - sum(b))