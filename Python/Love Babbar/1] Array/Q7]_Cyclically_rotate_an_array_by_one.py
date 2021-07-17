# Write a program to cyclically rotate an array by one.





a = [1,2,3,4]
n = len(a)

temp = a[n-1]
print(temp)

for i in range(n-1,0,-1):
    a[i] = a[i-1]
a[0] = temp

print(a)
