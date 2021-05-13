n=int(input())

for i in range(1, n+1):
    #check num
    x=i
    if (x%3==0):
        print(" ", i, end="")
    #include3
    elif (x%10 ==3):
        print(" ", i, end="")
        x=x%10
    else:
        x=x//10
        if (x):
            print(" ")

    