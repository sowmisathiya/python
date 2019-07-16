acb,ba = map(int,input().split())
ca = list(map(int,input().split()))
da = []
for i in range(0,ba):
  in = list(map(int,input().split()))
  da.append(in)
for i in da:
  en = ca[i[0] - 1:i[1]]
  fn = en[0]
  for j in range(0,len(en) - 1):
    fn = fn ^ en[j + 1]
  print(fn)
