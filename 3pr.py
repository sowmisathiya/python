a,b=input().split()
l21=len(a)
l22=len(b)
mi=abs(l21-l22)
if(l21<=l22):
  s=a
  l23=b
else:
  s=b
  l23=a
if(len(s)==1):
  print(min)
else:
  for i in range(len(s)):
    if(s[i]!=l23[i]):
      min+=1
  print(min)
