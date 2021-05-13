N=int(input())
S=input()
Q=int(input())
T=[]
A=[]
B=[]
for i in range(0, Q):
    elemT, elemA, elemB =map(int, input().split())
    T.append(elemT)
    A.append(elemA)
    B.append(elemB)

for i in range(0, Q):

    if T[i]==1:
        part_str_A=S[:A[i]-1]
        stringA=S[A[i]-1]
        part_strA_B=S[A[i]:B[i]-1]
        stringB=S[B[i]-1]
        part_str_B=S[B[i]:]
        S=part_str_A+stringB+part_strA_B+stringA+part_str_B
    if T[i]==2:
        first_half=S[0:N]
        second_half=S[N:]
        S=second_half+first_half
print("".join(S))