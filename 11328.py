N = int(input())

for i in range(N):
    a, b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))

    if a == b:
        print("Possible")
    else:
        print("Impossible")

#회고
#문자 입력 가능이므로 map(int,~)가 아님
#(문자사이 넣을 무언가).join(대상 리스트) => 문자열로 변환