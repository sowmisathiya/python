man,ran=list(map(int,input().split()))
ls1=list(map(int,input().split()))
for i in range(ran):
  u21,v31=list(map(int,input().split()))
  print(sum(ls1[u21-1:v31]))
