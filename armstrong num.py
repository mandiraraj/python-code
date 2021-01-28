def isArmstrong(x):

    n = len(str(x))
    sum1 = 0
    for i in str(x):
        sum1 = sum1 + int(i) ** n
    return (sum1 == x)
n = int(input())
print(isArmstrong(n))
