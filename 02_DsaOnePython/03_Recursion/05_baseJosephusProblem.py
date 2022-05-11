'''
- Base Josephus problem where in the current player kills the next player
- If n = 22 find the closed possible square of 2 in this case 16 is closes
- Therefore 2^a + l i.e 16 + 6
- Therefore result =  2*l + 1  = 2*6 + 1  = 1
---------------------------------Or-----------------------------------
- Convert the number to binary and move the leading most bit to the end 
  and we have the result
  Example    16 8 4 2 1 
        22 =  1 0 1 1 0
        -->   0 0 1 1 1 == result = 13
'''
def method1(n):
    perfectSqure = 2
    for i in range(n, 0, -1):
        if (i & (i-1)) == 0:
            perfectSqure = i
            break

    diff = n - perfectSqure
    return (2*diff)+1


# Bit manipulation
def method2(n):
    res = ''
    while n >= 1:
        res += str(n % 2)
        n = n//2
    res = res[::-1]
    first = res[0]
    res = res[1:]
    res += first
    return int(res, 2)


# Method 1 function call
# for i in range(1, 42):
#     print('For i =',i,'safe value is:',method1(i))

# Method 2 function call
n = 41
print(method2(n))
