a25=int(input())
l84=list(map(int,input().split()))
m92=0

for i in range(0,a25):

    for j in range(0,i):
        if l84[j]<l84[i]:
            m92=m92+l[j]

print(m92)
