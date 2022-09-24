n = int(input())
a = sorted(map(int,input().split()))
m = int(input())

cnt = 0

for i in range(n):
    if a[i] == m:
        cnt += 1

print(cnt)