N=int(input())

listA=list(map(int, input().split()))
listB=list(map(int, input().split()))
con_min=0
con_max=1001

for i in range(0, N):
    if listA[i] > con_min:
        con_min=listA[i]
    if listB[i] < con_max:
        con_max=listB[i]

if con_max-con_min>=0:
    print(con_max-con_min+1)
else:
    print(0)
