# 9.1

n = 496
x = []
y = []
sizes = []
for j in range(n):
    x1, y1 = map(int, input().split(','))
    x.append(x1)
    y.append(y1)
for j in range(n):
    for i in range(j+1, n):
        sizes.append((abs(x[i]-x[j])+1) * (abs(y[i]-y[j])+1))
print(max(sizes))
