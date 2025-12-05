# https://adventofcode.com/2025/day/1

# 1.1

l = 4035
cou = 0
currentPoint = 50
for j in range(l):
    s = input()
    r = s[0]
    n = int(s[1:])
    if r == 'L':
        n = n % 100
        if currentPoint - n < 0:
            print('-')
            currentPoint = currentPoint - n + 100
        else:
            currentPoint -= n
        if currentPoint == 0:
            cou+=1
        print("currentPoint=", currentPoint)
        continue
    if r == 'R':
        n = n % 100
        if currentPoint + n > 99:
            print('+')
            currentPoint = (currentPoint + n)%100
        else:
            currentPoint += n
        if currentPoint == 0:
            cou += 1
        print("currentPoint=", currentPoint)
        continue
print(cou)

# 1.2

l = 4035
cou = 0
currentPoint = 50
for j in range(l):
    s = input()
    r = s[0]
    n = int(s[1:])
    if r == 'L':
        cou+= n//100
        n = n % 100
        cb = currentPoint
        if currentPoint - n < 0 :
            currentPoint = currentPoint - n + 100
            if cb != 0:
                cou += 1
        else:
            currentPoint -= n
            if currentPoint == 0 and cb != currentPoint:
                cou+=1
        continue
    if r == 'R':
        cou+= n//100
        n = n % 100
        cb = currentPoint
        if currentPoint + n > 99 :
            if cb != 0:
                cou+=1
            currentPoint = (currentPoint + n)%100
        else:
            currentPoint += n
            if currentPoint == 0 and cb != currentPoint:
                cou += 1
        continue

print(cou)
