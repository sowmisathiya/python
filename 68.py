e1,f1=map(int,input().split())
lnt=list(map(int,input().split()[:e1]))
count=0
for i in lnt:
   if(i==f1):
      print("yes")
      break
else:
   print("no")
