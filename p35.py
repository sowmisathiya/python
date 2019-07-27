nr1=input()
leel1=list(map(int,input().split()))
max=0
i1=0
while(i1<len(leel1)-1):
    count1=0
    while(i1<len(level1)-1 and leel1[i1]<leel1[i1+1]):
        count1+=1
        i1+=1
    if(count1>max):
        max=count1
    i1+=1
print(max+1)
