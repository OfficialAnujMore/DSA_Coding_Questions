from itertools import permutations


def perms(arr):
    return list(permutations(arr))


def permsNew(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]

    res = []
    for i in range(len(arr)):
        m = arr[i]
        remLst = arr[:i] + arr[i+1:]
        for p in permsNew(remLst):
            print(p)
            res.append([m]+p)

    return res


def permsRec(arr):
    result = []
    if len(arr) == 1:
        return [arr.copy()]

    for i in range(len(arr)):
        n = arr.pop(0)
        perms = permsRec(arr)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        arr.append(n)

    return result


arr = [i for i in range(1, 4)]
print(permsRec(arr))
