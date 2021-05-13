# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    maxA=max(A)
    strokes=[]
    for i in range(1, maxA+1):
        count=1
        while i in A:
            indexA=A.index(i)

            
            A[indexA]=0
            if i not in A:
                break
            indexA_next=A.index(i)
            if (indexA_next-indexA)>1:
                count=count+1
            else:
                continue
        strokes.append(count)
    return print(sum(strokes))


A=[1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
solution(A)