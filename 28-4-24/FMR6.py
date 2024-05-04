


def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

def mapX(Task, Elements):
    result = []
    for no in Elements:
        result.append(Task(no))
    return result

def reduceX(Task, Elements, initializer =None):
    it = iter(Elements)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for no in it:
        value = Task(value, no)
    return value 
    #OR

