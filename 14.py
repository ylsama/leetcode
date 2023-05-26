strs = ["abcd" for i in range(5)] + ["ab"]

check = True
maxL = -1
while check:
    maxL += 1
    if len(strs[0]) <= maxL:
        check = False
        continue
    cmp = strs[0][maxL]
    for i in range(len(strs)):
        if len(strs[i]) <= maxL:
            check = False
            continue
        if strs[i][maxL] != cmp:
            check = False
            continue

print (maxL)




