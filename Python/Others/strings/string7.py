# Write a Python function that takes a list of words and returns the longest word and 
# the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9


lst = ['Anuj', 'Exercises', 'WorkOut']

max = len(lst[0])
# print(max)
for i in range(1,len(lst)):
    le = len(lst[i])
    if le > max:
        max = len(lst[i])
        print("Longest word is "+  str(lst[i]))
        print("Length of Longest word is " + str(len(lst[i])))