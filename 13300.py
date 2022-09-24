n, k = map(int, input().split())
student = [[0] * 7 for _ in range(3)]

for _ in range(n):
    s, y = map(int, input().split())
    student[s][y] += 1

rn = 0

for i in student:
    for j in i:
        if j % k == 0:
            rn += j / k
        else:
            rn += j // k + 1

print(int(rn))

#회고
#학년, 성별 그대로 인덱스를 주기 위해 7, 3
#student[][] 가 각 학생수이므로 k로 나누기
#나눈 나머지가 0이면(학생수가 0인것도 이 경우) 방 개수에 몫을 더한다.
#아닌 경우 정수 몫의 값에 +1 로 처리(학생수가 k보다 작거나 큰 경우 모두 성립)