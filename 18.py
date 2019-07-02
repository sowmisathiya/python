v1,s2=map(int,input().split())
for j in range(v1+1,s2):
  fn=j
  fnd=0
  while (j>0):
    d=j%10
    fnd=fnd+(d**3)
    j=j//10
    if(fnd==fn):
      print(fnd,end='')
