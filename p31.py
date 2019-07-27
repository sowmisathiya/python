p3=int(input())
q3=list(map(int, input().split()))
r2= int(len(q3)/2)
if sum(q3[:r2])//len(q3[:r2]) == sum(q3[r2:])//len(q3[r2:]):
    print('yes')
else:
    print('no')
