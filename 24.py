abcd=int(input())
efgh=list(map(int,input().split()[:abcd]))
efgh.sort()
for i in efgh:
  print(i,end=" ")
