so=list(input())
i=[]
for j in so:
   if j not in i:
      i.append(j)
if so==i:
   print("Yes")
else:
   print("No")
