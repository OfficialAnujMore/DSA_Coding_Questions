# python3

def suffix_array(s):
    suffix = []
    for i in range(len(s)):
        suffix.append((s[i:], i))
    suffix.sort()
    result = []
    for e in suffix:
        result.append(e[1])
    return result


if __name__ == '__main__':
    text = input()
    sa = suffix_array(text)
    for e in sa:
        print(e, end=' ')