number=int(input())
sum=0
tem=number
while tem>0:
  dig=tem%10
  sum += dig**3
  tem//=10
if number==sum:
  print("yes")
else:
  print("no")

