sow1,sow2=map(int,input().split())
n=1
while(n<=sow1 and n<=sow2):
   if(sow1%n==0 and sow2%n==0):
      tv=n
   n=n+1
print(tv)
