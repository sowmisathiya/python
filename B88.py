ab1,bc2=map(int,input().split())
if(ab1>bc2):
  great=ab1
else:
  great=bc2
while(True):
  if((great%a1) == 0 and (great%b2) == 0):
    cm=great
    break
  great=great+1
print(cm)
