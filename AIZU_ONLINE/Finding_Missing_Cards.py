n=int(input())
card_list=[]
full_card_list=[]

S_list=["S {i}" for i in range(n)]
H_list=["H {i}" for i in range(n)]
C_list=["C {i}" for i in range(n)]
D_list=["D {i}" for i in range(n)]

full_card_list.extend(S_list, H_list, C_list, D_list)

for i in range(n):
    card_list.append(input())

for card in card_list:
    if card in full_card_list:
        full_card_list.remove(card)

print(full_card_list)
    