def Add(x, y):
 
    # Iterate till there is no carry
    while (y != 0):
     
        # carry now contains common
        # set bits of x and y
        carry = x & y
 
        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y
 
        # Carry is shifted by one so that  
        # adding it to x gives the required sum
        y = carry << 1
    print(bin(x))
    return x

# print(Add(8,7))

print(bin((15 & 14)))
print((15 & 14))