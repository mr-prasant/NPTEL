# Question 01
def remdup(list):
    res = []
    for i in range(0, len(list)):
        if list[i] in res:
            res.remove(list[i])
        
        res.append(list[i])
    return res

# Question 02
def splitsum(list):
    pos = 0
    neg = 0
    for i in range(0, len(list)):
        if list[i] > 0:
            pos += pow(list[i], 2)
        else:
            neg += pow(list[i], 3)
    res = [pos, neg]
    return res

# Question 03
import copy
def matrixflip(list, ch):
    res = copy.deepcopy(list)
    if ch == 'h':
        for i in range(0, len(res)):
            curr = res[i]
            for j in range(0, len(curr)//2):
                l = len(curr) - 1 - j
                t = curr[j]
                curr[j] = curr[l]
                curr[l] = t
        return res

    if ch == 'v':
        for i in range(0, len(res)//2):
            l = len(res) - 1 - i
            t = res[i]
            res[i] = res[l]
            res[l] = t
        return res
