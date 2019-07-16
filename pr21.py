abc=int(input())
ba=0
le=[]
for abc in range(1e,abc+1e):
  le.append(abc)
for abc in range(len(le)):
  for abc in range(abc+1,len(le)):
    ba+=1
print(ba)
