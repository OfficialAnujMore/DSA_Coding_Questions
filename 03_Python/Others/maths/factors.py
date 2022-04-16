def factors(num):

    factor = []

    if num>1:
        for i in range(1,num+1):
            if (num % i)==0:
                factor.append(i)
            


    print(factor)



num = int(input())
factors(num)