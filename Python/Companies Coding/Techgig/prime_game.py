''' Read input from STDIN. Print your output to STDOUT '''
#     #Use input() to read input from STDIN and use print to write your output to STDOUT
# import time
# t0 = time.time()

def main(first,last):

    f = 0
    l = 0


    def isPrime(n):
        if n<=1:
            return False

        for i in range(2,n):
            if n%i==0:
                    return False
        return True
    for i in range(first,last+1):
        if f == 0:
            if isPrime(i):
                f = i
            else:
                i+=1
        if l ==0:
            if isPrime(last):
                l = last
            else:
                last-=1
        if f!=0 and l!=0:
            break
         
    if f!=0 and l!=0:
        return (l-f)
    else:
        return -1

    

test_cases = int(input())
for i in range(0, test_cases):
    first, last = map(int,input().split())
    print(main(first,last))
    # t1 = time.time()
    # print(t1-t0)

