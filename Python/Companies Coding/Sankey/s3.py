def s3(name,entry):

    overall_sum=[]
    for i in range(0,len(entry)):
        # overall_sum=0
        total = 0
        for j in range(0,3):
            total+= sum(entry[i][j])
        overall_sum.append(total)


    max_val = max(overall_sum)
    max_index = overall_sum.index(max_val)
    return name[max_index]


names = ["Peter Parker","Steve Rogers","Toney Starks"]
entry = [ 
[
            [6,4,7,5,5],
            [3,4,3,5,5],
            [4,6,5,4,4]
], 
[
            [8,9,7,6,8],
            [3,4,8,6,5],
            [7,7,5,8,9]
], 
[
            [3,4,6,4,5],
            [9,9,8,7,7],
            [6,7,6,5,6]
], 

        ]

print(s3(names,entry))