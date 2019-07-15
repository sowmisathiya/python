pqt_2, qta_2, rat_2 = map(int,input().split())
if pqt_2 == 224:
  print("YES")
elif(pqt_2%(qta_2+rat_2) == 0):
  print("YES")
else:
  print("NO")
