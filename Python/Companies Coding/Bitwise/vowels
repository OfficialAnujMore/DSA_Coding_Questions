t = int(input())
arr = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
while t:
    t-=1
    s = input()
    count = 0
    n = len(s)
    psum_arr = [n]
    for i in range(1,n):
        psum_arr.append((n-i)+psum_arr[i-1]-i)
    for i in range(n):
        if s[i] in arr:
            count+=psum_arr[i]
    print(count)
