varsow=int(input())
keep=list(map(int,input().split()[:varsow]))
keep.sort()
for i in keep:
  print(i,end=" ")
