def dictInList(r,d):
    for k in d:
        r.append(d[k])
        r.append(k)
    return r


def next_line(line):
    res = {}
    resres = []
    for i in line:
        if res.get(i,None) == None:
            dictInList(resres,res)
            res = {i:1}
        else:
            res[i]+=1
    dictInList(resres,res)
    if len(resres) == 0:
        return [1]
    else:
        return resres

      
print(next_line([1, 2, 1, 1]))
print(next_line([1, 1, 1, 2, 2, 1]))
print(next_line([3, 1, 1, 3, 1, 1, 2, 3, 3, 1, 2, 3, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 3, 2, 1, 1]))
