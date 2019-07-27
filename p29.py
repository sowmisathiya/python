cou1=int(input())
arr=[]
ss1=[]
for i in range(cou1):
  arr.append(list(map(int,input().split())))
for l in arr:
  for n in l:
    ss1.append(n)
ss1.sort()
for i in ss1:
  print(i,end=' ')
