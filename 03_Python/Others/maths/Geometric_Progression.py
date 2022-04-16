def Geometric_Progression(a, r, n):


    for i in range(0,n):
        num = a * r**i
        print(num,end=" ")

a = 2
r = 2
n = 4

Geometric_Progression(a, r, n)
