list1 = input()
list2 = input()

result = 0

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] != " " and list1[i] == list2[j]:
            list1 = list1.replace(list1[i], " ", 1)
            list2 = list2.replace(list2[j], " ", 1)
            break

for i in range(len(list1)):
    if list1[i] != " ":
        result += 1

for i in range(len(list2)):
    if list2[i] != " ":
        result += 1

print(result)

#회고
#replace 사용 시 갱신 주의

#다른 전략
# from collections import Counter
#
# a = Counter(input())
# b = Counter(input())
#
# print(sum((a - b).values()) + sum((b - a).values()))