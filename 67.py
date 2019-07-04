    
pln1,pln2=map(int,input().split())
ln=list(map(int,input().split()[:pln1]))
count=0
for i in ln:
   if(i==pln2):
      count=count+1
print(count)      
