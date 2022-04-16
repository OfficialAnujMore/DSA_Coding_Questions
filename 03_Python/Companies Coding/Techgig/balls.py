def main(index, arr):

    move = 1

    fac = 1

    for num in range(0, index):
        n = arr[num]
        actual = n

        if n == 1:
            move += n
        else:
            for i in range(2, n+1):
                if n % i == 0:
                    fac = i
                    break

            for j in range(2, n):
                # print("Value of n", n)
                if n == fac:
                    move += actual
                    # print("Single")
                    break
                else:
                    x = n//j
                    if n % j == 0:
                        n = j
                        i = 2
                        move += x
                        # print("Set", x)
                        # print("of", j, "each")
                        # print(x*j)
                        # print("x"*30)

    return move


arr = [80]
index = len(arr)
print(main(index, arr))


# def isPrime(m):
#     if m <= 1:
#         return False

#     for i in range(2, m):
#         if m % i == 0:
#             return False
#     return True


'''
What will be the output for 10, 11, 30 and 55?
10 am getting 16, for 11 getting 12, for 30 getting 46 and for 55 getting 56, is it correct?

156
1 + 5 + 15 + 45 + 90 = 156

what will be the output of 99 is it 112?

80=>{80,40,20,10,5,1}=>156


81 = 81 + 27 + 9 + 3 + 1

'''
