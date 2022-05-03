def check(num, mul):
    print(num, mul)

    return mul % num == mul & num-1


num = 15
for i in range(1, 11):
    print(check(num, num*i))

