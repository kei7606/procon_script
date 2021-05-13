A, B=map(int, input().split())
len_of_sequence=A+B
flag=0
A_is_bigger=1
A_equals_B=0
B_is_bigger=-1
Sequence=[]
seed=1000
seed2=1
part_of_Sequence=[]


def which_is_bigger(A, B):
    if A>=B:
        flag=A_is_bigger
        
    else:
        flag=B_is_bigger
    return flag


def generate_sequence(A, B):


    if which_is_bigger(A, B)==A_is_bigger:
        smaller=B
        if smaller!=0:
        
            absol_minus1=smaller-1
            num_of_mod_A=A-absol_minus1
            num_of_mod_B=B-absol_minus1
            for i in range(0, num_of_mod_A):
                element_A=seed2+i
                part_of_Sequence.append(element_A)
            elementB=-(sum(part_of_Sequence))
            part_of_Sequence.append(elementB)

    elif which_is_bigger(A, B)==B_is_bigger:
        smaller=A
        absol_minus1=smaller-1
        num_of_mod_A=A-absol_minus1
        num_of_mod_B=B-absol_minus1
        for i in range(num_of_mod_B):
            element_B=-(seed2+i)
            part_of_Sequence.append(element_B)
        element_A=-(sum(part_of_Sequence))
        part_of_Sequence.append(element_A)

    absol_minus1=smaller-1
    
    for i in range(0, absol_minus1):
        element_A=seed+i
        element_B=-(seed+i)
        Sequence.append(element_A)
        Sequence.append(element_B)
   
    Sequence.extend(part_of_Sequence)
    return Sequence

sequence=generate_sequence(A, B)
for i in sequence:
  print(i, end=" ")
