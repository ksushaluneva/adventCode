# 5.1

d = 187
diapasons = []
for i in range(d):
    n1, n2 = map(str, input().split('-'))
    add = [int(n1), int(n2)]
    diapasons.append(add)
print(diapasons)
n = input()
n = 1000
c = 0
for i in range(n):
    num = int(input())
    for j in range(d):
        if diapasons[j][0] <= num <=diapasons[j][1] :
            c+=1
            break
print(c)

# 5.2

d = 187
diapasons = []
for i in range(d):
    n1, n2 = map(str, input().split('-'))
    add = [int(n1), int(n2)]
    diapasons.append(add)
diapasons = sorted(diapasons)
# print(diapasons)
i = 0
while  i < len(diapasons)-1:
    if diapasons[i][1] >= diapasons[i+1][0]:
        if diapasons[i][1] > diapasons[i+1][1]:
            diapasons[i+1][1] = diapasons[i][1]
        diapasons[i+1][0] = diapasons[i][0]
        diapasons.pop(i)
    else:
        i+=1
c = 0
# print(diapasons)
for diapason in diapasons:
    c+= diapason[1]-diapason[0]+1
print(c)
