def stu(subject,arr):

    scores = []

    for i in range(0,6):
        # print(sum(arr[i]))
        scores.append(sum(arr[i]))

    min_val = min(scores)
    min_index = scores.index(min_val)

    return subject[min_index]

arr = [
    [100,80,90,60,50,40,80],
    [80,70,70,60,90,60,80],
    [50,80,60,65,62,64,35],
    [90,100,90,80,80,70,65],
    [90,80,70,80,85,65,50],
    [60,40,70,80,95,85,75],
    ]
subject = ['English','History','Computers','Mathematics','Science','Economics']
print(stu(subject,arr))