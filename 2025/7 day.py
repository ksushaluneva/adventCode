# 7.1

c = 141
streams = []
cou = 0
s = input()
streams.append(s.index('S'))
l = len(s)
for i in range(c):
    s = list(input())
    if s.__contains__("^"):
        for j in range(s.count("^")):
            ind = s.index("^")
            s[ind] = '.'
            if streams.__contains__(ind):
                streams.remove(ind)
                cou += 1
                if ind > 0 and ind < l - 1:
                    streams.append(ind-1)
                    streams.append(ind+1)
                else:
                    if ind == 0:
                        streams.append(1)
                    if ind == l - 1:
                        streams.append(l-2)
        streams = list(set(streams))
print(cou)

# 7.2

c = 141
streams = []
s = input()
streams.append(s.index('S'))
l = len(s)
cou = []
for i in range(l):
    cou.append(0)
cou[streams[0]] = 1
for i in range(c):
    s = list(input())
    if s.__contains__("^"):
        for j in range(s.count("^")):
            ind = s.index("^")
            s[ind] = '.'
            if streams.__contains__(ind):
                streams.remove(ind)
                currVal = cou[ind]
                cou[ind] = 0
                if ind > 0 and ind < l - 1:
                    streams.append(ind-1)
                    streams.append(ind+1)
                    cou[ind-1]+= currVal
                    cou[ind+1]+= currVal
                else:
                    if ind == 0:
                        streams.append(1)
                        cou[1]+= currVal
                    if ind == l - 1:
                        streams.append(l-2)
                        cou[l-2]+= currVal
        streams = list(set(streams))
print(sum(cou))
