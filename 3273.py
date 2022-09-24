n = int(input())
#a = map(int,input().split()) -> <map object at 0x00000234D59C04F0>
a = sorted(map(int,input().split())) #-> [,,,]
m = int(input())

i = 0
j = n - 1
cnt = 0
while i != j:
    ans = a[i] + a[j]
    if ans == m:
        cnt += 1
        i += 1
    elif ans > m:
        j -= 1
    else:
        i += 1

print(cnt)

#회고
#정렬 후 양쪽에서 좁혀가는 전략
#조건 불충분 상황에서 로직 생각하기