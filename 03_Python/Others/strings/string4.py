# Write a Python program to get a string from a given string where all occurrences of its 
# first char have been changed to '$',  except the first char itself. 
# Sample String : 'restart'
# Expected Result : 'resta$t'


def str4(str):
  char = str[0]
  str = str.replace(char, '$')
  str = char + str[1:]

  return str


    # char = str[0]

    # for i in str:
    #     if str[i] == char:
    #         str = str.replace(char,'$')
    #         return str

print(str4('restart'))
