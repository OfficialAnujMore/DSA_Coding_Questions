def findIthBit(n, iVal):
    mask = 1 << iVal
    if (n & mask) > 0:
        return 1
    else:
        return 0


def setIthBit(n, iVal):
    mask = 1 << iVal
    return (n | mask)

def clearIthBit(n,iVal):

    mask = ~(1 << iVal)
    return (n & mask)

def changeAtoB(a,b):
    res = a ^ b
    count = 0
    print(res)
    while res:
        count+=1
        res = res & (res-1)
    return count
# print(findIthBit(16, 4))
# print(setIthBit(8, 1))
# print(clearIthBit(5, 2))
# print(changeAtoB(5,1))
print(changeAtoB(16,15))
