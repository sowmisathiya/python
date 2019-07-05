inbox1=list(input())
if len(inbox1)%2==0:
    inbox1[int(len(inbox1)/2)] ='*'
    inbox1[int(len(inbox1)/2)-1]='*'
else:
    inbox1[int(len(inbox1)/2)] ='*'
for i in range(0,len(inbox1)):
    print(inbox1[i],end='')
