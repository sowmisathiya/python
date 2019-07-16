import math
c22,l23=map(int,input().split())
m25=[]
k12=list(map(int,input().split()))
for j in range(0,l23):
    p12,q32=map(int,input().split())
    m25.append([p12,q32])
for j in m25:
    x23=j[0]-1
    y24=j[1]-1
    print(math.gcd(k12[x23],k12[y24]))
