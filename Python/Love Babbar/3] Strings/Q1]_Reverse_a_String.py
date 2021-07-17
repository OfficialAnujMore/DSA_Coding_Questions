# Reverse a String

a = input()


for i in range(len(a)-1,-1,-1):
    if len(a) == 0:
        print("Provided empty string",a)
    else:
        print(a[i],end = "")
