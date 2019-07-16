x1=int(input())
y2=[]
for i in range(x1):
  y2.append(input())
  a1,b2,flag ='',0,False
for m in y2[0]:
  for n in y2[1:]:
    if len(n)==b2:
      flag=True
      break
    if n[b2]!=m:
      break
  else:
    a1+=m
  if flag:
      break
  b2+=1
print(a1)
