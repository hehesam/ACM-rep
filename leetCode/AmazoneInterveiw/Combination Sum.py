



candidates = [2,3,6,7]
target = 7

def backtrack(indx,target,path):
    global candidates
    if indx == len(candidates) or target == 0:
        if target == 0:
            res.append(path)
        return
    elif candidates[indx] > target:
        return

    backtrack(indx,target-candidates[indx],path + [candidates[indx]])
    backtrack(indx+1,target ,path)
    backtrack(0,target,[])
    return res



