sowmi=int(input())
if(sowmi>1):
   for l in range(2,sowmi):
      if(sowmi%l)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")
