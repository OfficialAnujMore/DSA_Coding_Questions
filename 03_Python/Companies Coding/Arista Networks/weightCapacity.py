from itertools import combinations
import numpy as np
def weightCapacity(weights, maxCapacity):

    combination  =[]
    j = 2

    for i in range(0,len(weights)):
        combination.append(weights[i])
    while j <len(weights):
            x = list(combinations(weights,j))
            for i in x:
                combination.append(sum(i))
                
            j+=1    

    valid_max =0
    for i in combination:
        if i <=maxCapacity and i >=valid_max:
            valid_max = i 

    print(valid_max)
    print('*'*20)
    print(combination)

weight = [4, 8, 5, 9]
maxCapacity = 20

print(weightCapacity(weight,maxCapacity))