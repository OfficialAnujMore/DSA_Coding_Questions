def s1(str):
    vowels = ['a','e','i','o','u']
    lst = str.split()

    final_str = ''
    n = len(lst)

    for i in range(0,n):
        if (i == 0 or i ==3 or i==6):
            v_str = ''
            for j in lst[i]:
                if j in vowels:
                    v_str+='%'
                else:
                    v_str+=j
            final_str+=v_str
        elif (i == 1 or i ==4 or i==7):
            c_str = ''
            for j in lst[i]:
                if j  not in vowels:
                    c_str+='#'
                else:
                    c_str+=j
            final_str+=c_str
        else:
            n_str = lst[i].upper() + " "
            final_str+=n_str
    return final_str

str  = "Where are you? Meet me near the clock tower"
print(s1(str))