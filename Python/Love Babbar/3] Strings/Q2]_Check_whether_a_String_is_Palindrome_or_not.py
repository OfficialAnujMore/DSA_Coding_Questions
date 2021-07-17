# Check whether a String is Palindrome or not


a = "Nitin"
b = ""

if a[::-1] == a:
    print("TRUE")

else:
    print("False")


for i in range(len(a)-1,-1,-1):
    b +=a[i]

if b.lower() == a.lower():
    print("Is palindorme")
else:
    print("Not palindrome")
