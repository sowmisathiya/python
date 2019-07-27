sow=(int,input())
sow1=list(map(int,input().split()))
sa=int(len(sow1)/2)
if sum(sow1[:sa])//len(sow1[:sa]) == sum(sow1[sa:])//len(sow1[sa:]):
  print('yes')
else:
  print('no')
