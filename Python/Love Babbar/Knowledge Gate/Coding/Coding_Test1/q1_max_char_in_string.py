#wap to find maximum occuring char in a string


def max_count(string):

    print("The string is:",string)

    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char]+=1

        else:
            frequency[char]=1

        most_occuring = max(frequency, key=frequency.get)
    print("The character repeated max time is", most_occuring, "and it is repeated", frequency[most_occuring])

max_count("Welcome to knowledge gate")
