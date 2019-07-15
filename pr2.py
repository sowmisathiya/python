rat,dog=input().strip().split(" ")
dog=int(dog)
sow=0
while sow<len(r)-1 and dog:
	if(rat[sow]>rat[sow+1]):
		dog-=1
		rat=rat[:sow]+r[sow+1:]
		if(sow!=0):
			sow-=1
	else:
		sow+=1
qea=rat[:len(rat)-dog]
print(qea)
