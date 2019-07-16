an,bn = map(int,input().split())
cn = list(map(int,input().split()))
dn = []
for i in range(0,b):
  in = list(map(int,input().split()))
  dn.append(in)
for i in dn:
  en = cn[i[0] - 1:i[1]]
  fn = en[0]
  for j in range(0,len(en) - 1):
    fn = fn ^ en[j + 1]
  print(fn)
