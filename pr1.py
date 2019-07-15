y1 = int(input())
lst= []
for _ in range(y1):
    lst.append(input())
x2, c3, flag = '', 0, False
for i in lst[0]:
    for j in lst[1:]:
        if len(j) == c3:
            flag = True
            break
        if j[c3] != i:
            break
    else:
        x+= i
    if flag:
        break
    c3 += 1
print(x2)
