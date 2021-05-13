N=int(input())
Amax=10**9
map_a=map(int, input().split())

list_a=list(map_a)
list_a.sort()
counter=0
decrease_count=0
mod_list=[]

for i in range(N):
    mod=list_a[i]%200
    mod_list.append(mod)
mod_list.sort()
mod_set=list(set(mod_list))

for num in mod_set:
    conbi=mod_list.count(num)
    counter=counter+conbi*(conbi-1)/2
    index=mod_list.index(num)

counter=counter-decrease_count
print(int(counter))