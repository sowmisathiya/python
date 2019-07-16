mat,rat = input().split()
mat,rat = int(mt), int(rt)
Lat1 = [ int(x) for x in input().split()]
for i in range(0,rat) :
    aat1,bat1 = input().split()
    aat1,bat1 = int(aat1), int(bat1)
for i in range(0,rat):
    print(min(Lat1[aat1-1:bat1]))
