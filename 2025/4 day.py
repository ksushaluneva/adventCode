# 4.1

l = 139
arr = []
s = input()
s = list("." + s + ".")
ls = len(s) + 2
print(s)
arr.append([])
for i in range(ls):
    arr[0].append('.')
arr.append(s)
for j in range(l-1):
    s = input()
    s = list("." + s + ".")
    arr.append(s)
c = 0
arr.append([])
for i in range(ls):
    arr[-1].append('.')
# print(arr)
for i in range(1, l+1):
    for j in range(1, ls-2):
        if arr[i][j] == '@':
            if (arr[i-1][(j-1):(j+2)].count('@') + arr[i][(j-1):(j+2)].count('@') + arr[i+1][(j-1):(j+2)].count('@') -1) < 4:
                c+=1
print(c)
