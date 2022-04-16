# Find the Union and Intersection of the two sorted arrays.




def printUnion(a,b,m,n):

    i,j = 0,0
    c = []
    while i < m and j < n:

        if a[i] < b[j]:
            c.append(a[i])
            i +=1
        elif b[j] < a[i]:
            c.append(b[j])
            j +=1
        else:
            c.append(b[j])
            i+=1
            j+=1

    # print remaning values
    
    while i<m:
        c.append(a[i])
        i+=1

    while j<n:
        c.append(b[j])
        j+=1

    return c

def printIntersection(a,b,m,n):
    
    i,j = 0,0
    c=[]
    while i<m and j<n:
        
        if a[i] < b[j]:
            i+=1
            
        elif b[j] < a[i]:
            j+=1
            
        else:
            c.append(b[j])
            i+=1
            j+=1
            
         
    return c  


a = [1, 2, 4, 5, 6]
b = [2, 3, 5, 7]
m = len(a)
n = len(b)

print(printUnion(a, b, m, n))

print(printIntersection(a, b, m, n))
