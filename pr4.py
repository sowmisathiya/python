mat1,nat1=map(str,input().split())
yet1=0
if len(mat1)>len(nat1):
	mat1,nat1=nat1,mat1
pen1=0
while pen1<len(mat1):
	  yet1+=(ord(nat1[pen1])-ord(mat1[pen1]))
	  pen1+=1
for pen1 in range(pen1,len(nat1)):
	  yet1+=ord(nat1[pen1])-ord('a')+1
print(yet1)
