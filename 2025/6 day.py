# 6.1

arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))
s = list(map(str, input().split()))
res = 0
for i in range(len(arr[0])):
    diya = s[i]
    mas =[ arr[0][i], arr[1][i], arr[2][i], arr[3][i]]
    res+= eval(diya.join(map(str, mas)))
print(res)

# 6.2

arr = []
for i in range(4):
    arr.append(input())
s = list(map(str, input().split()))
res = 0
dc = 0

chisla = []
diya = s[dc]

for i in range(len(arr[0])):
    p1 = arr[0][i]
    p2 = arr[1][i]
    p3 = arr[2][i]
    p4 = arr[3][i]

    if p1+p2+p3+p4 == "    ":
        res += eval(diya.join(map(str, chisla)))
        dc += 1
        print(chisla)
        chisla = []
        diya = s[dc]
    else:
        chisla.append(int(p1+p2+p3+p4))

res+= eval(diya.join(map(str, chisla)))

print(res)
