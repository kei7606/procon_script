A, B, C = map(int, input().split())


sq_A=A*A
sq_B=B*B
sq_C=C*C


if sq_A+sq_B < sq_C:
    print("Yes")
else:
    print("No")