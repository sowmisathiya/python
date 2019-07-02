sow=int(input())
if sow>1:
  for i in range(2,sow):
    if sow%i == 0:
      print("no")
      break
  else:
      print("yes")
else:
    print("no")
