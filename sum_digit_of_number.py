number = int(input("number = "))
temp = number
sum = 0
while temp > 0:
    q = temp % 10
    sum = sum+q
    temp = temp // 10

    print("sum of given number = ",sum)

