so1,so2=map(int,input().split())
for i in range(0,(so1*so2)+1):
   if(i**2==0):
      print("yes")
      break
else:
   print("no")
