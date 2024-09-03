#Binary Search Algorithm

def Binary_search(l, target, low=None, high=None):
    #example l =[1,3,5,7,10,12]
    l.sort()
    if low is None:
        low=0
    if high is None:
        high=len(l)-1

    if high<low:    
        return -1

    midpoint = (low+high) // 2

    if l[midpoint] == target:
        return midpoint
    
    elif target<l[midpoint]:
        return Binary_search(l, target, low, midpoint-1)
    else:
        return Binary_search(l,target, midpoint+1, high)    #target >l[midpoint]
    

List=[1,3,5,6,7,8,9,15,10]
print(Binary_search(List,10))
