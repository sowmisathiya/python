aa4=int(input())
bb4=list(map(int,input().split()))
ss6=0
ss7=0
for i in range(aa4):
	if i%2==0:
		ss6=ss6+bb4[i]
	else:
		ss7+=bb4[i]
print(max(ss6,ss7))
