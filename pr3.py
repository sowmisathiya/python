ad,bc=input().split()
xl1=len(ad)
yl2=len(bc)
map=abs(xl1-yl2)
if xl1<=yl2:
  sow=ad
  lev=bc
else:
  sow=bc
  lev=ad
if len(sow)==1:
  print(map)
else:
  for i in range(len(sow)):
    if sow[i]!=lev[i]:
      map+=1
  print(map)
