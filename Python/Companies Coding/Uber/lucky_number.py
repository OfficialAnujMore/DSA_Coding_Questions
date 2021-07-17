# from itertools import combinations

def lucky_number(n):

    combination = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            str1 = ""
            str1 += numbers[i] + numbers[j]
            combination.append(str1)

    count = 0
    for i in combination:
        if i[0]==i[1]:
            count+=1
    
    return count





n = int(input())
# n = 2
print(lucky_number(n))



n = int(input())
list = []
for i in range(0,10):
    t = str(i)*n
    list.append(t)
print(list)