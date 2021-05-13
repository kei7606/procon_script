N=int(input())
map_a=map(int, input().split())

list_a=list(map_a)
mod_list=[]
n=8
flag=0

#順番が決まっていると2^N-1
#順番が決まってなければ階乗か
#でも結局数列を200個作らなきゃいけない？200このリスト？
#さらに200個の数列から同じものをmatchしなきゃいけいない？200^2??
#問題ない？？

#create bit sequence
#やり方わからない。どうやってやるんだ。ツリー状に分岐するリストなんて作ったことない。
#そんな複雑なことは考えない。10進数を2進数変換して対応する。
bit_sequences=[list(f"{i:0{n}b}") for i in range(2**n)]

for sequence in bit_sequences:
        map_seq=map(int, list(sequence))
        temp_list=[]
        for num, bit in enumerate(map_seq):
            if num < N:
                if bit==1:
                    temp_list.append(list_a[num])
            else:
                break
        mod_list.append(sum(temp_list)%200)


for mod in mod_list:
    if mod_list.count(mod)!=1:
        index_x=mod_list.index(mod)
        mod_list[index_x]=None
        index_y=mod_list.index(mod)
        flag=1
        break
map_seq=list(map_seq)
answer_seq_x=bit_sequences[index_x]
answer_seq_y=bit_sequences[index_y]
ans_seq_list=[answer_seq_x, answer_seq_y]
answer_seq=[]

for sequnece in ans_seq_list: 
    answer_lists=[]
    for num, bit in enumerate(sequnece, 1):
        if int(bit)==1:
            answer_lists.append(num)
    answer_seq.append(answer_lists)

x_length=len(answer_seq[0])
y_length=len(answer_seq[1])


if flag==0:
    print("No")
else:
    print("Yes")
    print(x_length, answer_seq[0])
    print(y_length, answer_seq[1])
