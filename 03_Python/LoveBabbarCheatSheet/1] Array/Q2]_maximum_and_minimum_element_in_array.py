#Wapp to find the maximum and minimum element in array


a = [26,5,8,1,9,299,0]
n = len(a)

min,max  = a[0],a[0]

for i in range(1,n):
    if a[i] < min:
        min = a[i]
    if a[i] > max:
        max = a[i]
print("MIN -->",min)
print("MAX -->",max)



