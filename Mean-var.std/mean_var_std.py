import numpy as np

def calculate(list):
    if len(list)!=9:
        return ValueError('The list must have nine numbers')
    else:
        matrix=np.array(list)
        matrix=matrix.reshape(3,3)

    
    mean=[matrix.mean(axis=0),matrix.mean(axis=1),matrix.flatten().mean()]
    var=[matrix.var(axis=0),matrix.var(axis=1),matrix.flatten().var()]
    std=[matrix.std(axis=0),matrix.std(axis=1),matrix.flatten().std()]
    max=[matrix.max(axis=0),matrix.max(axis=1),matrix.flatten().max()]
    min=[matrix.min(axis=0),matrix.min(axis=1),matrix.flatten().min()]
    sum=[matrix.min(axis=0),matrix.min(axis=1),matrix.flatten().min()]
    
    calculations={"mean":mean,
                  "var":var,
                  "std":std,
                  "max":max,
                  "min":min,
                  "sum":sum
    }

    
    return calculations