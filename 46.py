k=input()
s=0
for i in rangr(len(k)):
  if(k[i].isdigit() or k[i].isalpha() or k[i]==(" ")):
    continue
  else:
    s+=1
  print(s)
   
