ln2=int(input())
if(ln2>1):
   for i in range (2,ln2):
      if(ln2%i==0):
       print("yes")
       break
   else:
      print("no")
