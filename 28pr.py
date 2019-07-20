ap,bpr=map(int,input().split())
l=[]
for _ in range(ar):
    l.append(input())
for i in range(len(l)):
    if('0' in l[i]):
        l[i]=l[i].replace('0','')
    l[i]=l[i].replace(' ','')
length=[]
for i in l:
    if(len(i)>0):
        length.append(len(i))
bpr=min(length)
ra1='1 '*bpr
ra1=ra1.strip()
for i in range(bpr):
    print(ra1)
