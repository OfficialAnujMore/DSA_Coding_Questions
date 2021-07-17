def prime(n):

    if n > 1:
        for i in range(2, n):
            if n % i == 0:

                print(str(n) + " is not a prime number as it's is divisible by " + str(i))
                break

        else:
            print(str(n) + " is a prime number.")

    else:
        print(str(n) + " is not a prime number")


n = int(input())
prime(n)
