inbox1=list(input())
if ln(inbox1)%2==0:
    inbox1[int(ln(inbox1)/2)] ='*'
    inbox1[int(ln(inbox1)/2)-1]='*'
else:
    inbox1[int(ln(inbox1)/2)] ='*'
for i in range(0,ln(inbox1)):
    print(inbox1[i],end='')
