rat1 = int(input())
mat1 = list(map(int,input().split()))
pqt1 = 0
for i in range(rat1):
    for l in range(i,rat1):  
        for k in range(l,rat1):
            if mat1[i]<mat1[l]<mat1[k]:
                pqt1+=1
print(pqt1)
