import math
cha1,cho1=map(int,input().split())
oho1=[]
gaa1=list(map(int,input().split()))
for j in range(0,cho1):
    love1,hut1=map(int,input().split())
    oho1.append([love1,hut1])
for j in oho1:
    kaa1=j[0]-1
    laa1=j[1]-1
    print(math.gcd(gaa1[kaa1],gaa1[laa1]))
