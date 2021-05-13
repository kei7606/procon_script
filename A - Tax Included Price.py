import math
import time
t, N=map(int, input().split())

copy_sum=0
t_sum=0
answers=[]
counter=0
adv_number=0
i=0
mod_list=[]


while 1:
    
    i=i+1
    copy_sum=t_sum
    t_sum=t_sum+t
    floored_copy=math.floor(copy_sum/100)
    floored_t_sum=math.floor(t_sum/100)
    if (floored_t_sum!=floored_copy):
        adv_number=copy_sum        
        break
start=t
add_times_until_advance=i
i=0
while 1:
    i=i+1
    start_copy=start
    start=start+adv_number
    floored_copy=math.floor(start_copy/100)
    floored_start=math.floor(start/100)
    if (floored_start!=floored_copy):
        substruct=math.floor(start/100)*100
        mod=start-substruct
        if mod in mod_list:
            break
        mod_list.append(mod)
add_times_until_one_sequence=len(mod_list)*add_times_until_advance

division=N//add_times_until_one_sequence
mod2=N%add_times_until_one_sequence

answer=t+adv_number*division+t*mod2*
print(answer)