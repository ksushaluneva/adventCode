# https://adventofcode.com/2025/day/3

# 3.1

l = 200
suma = 0
for j in range(l):
    s = input()
    m = []
    for f in range(len(s)-1):
        for i in range(f+1, len(s)):
            m.append(int(s[f]+s[i]))
    suma+=max(m)
print(suma)

# 3.2

l = 200
suma = 0
for j in range(l):
    s = list(input())
    for j in range(len(s)-12):
        for i in range(len(s)-1):
            if s[i] < s[i+1]:
                s.pop(i)
                break
    while len(s) > 12:
        s.remove(min(s))
    suma+=int(''.join(s))
print(suma)
