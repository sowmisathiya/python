c1=int(input())
c2=list(map(int,input().split()))
ans=int(c1/2)
ba1=c2[:ans]
ba2=c2[ans::]
if ((sum(ba1)//len(ba1))==(sum(ba2)//len(ba2))):
    print("yes")
else:
    print("no")
