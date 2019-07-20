sta10,pta10=map(int,input().split())
maxima=max(sta10,pta10)
while(1):
 if(maxima%sta10==0 and maxima%pta10==0):
  print(maxima)
  break
 maxima+=1
