# Write a Python program to change a given string to a new string where
# the first and last chars have been exchanged.



def exchange(s):

    start = s[0]
    end = s[len(s)-1]
    sx = ""


    for i in range(1,len(s)-1):
        sx  += s[i]

    return end  + sx+ start



print(exchange("Anuj"))