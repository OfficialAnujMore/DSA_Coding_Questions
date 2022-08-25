# python3

def bwt(s):
    matrix = [s]
    for i in range(1, len(s)):
        s = s[-1] + s[:-1]
        matrix.append(s)
    matrix.sort()
    bwt_output = ''
    for t in matrix:
        bwt_output += t[-1]
    return bwt_output

if __name__ == '__main__':
    text = input()
    print(bwt(text))