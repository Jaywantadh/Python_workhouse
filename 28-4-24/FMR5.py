#``````same code as FMR1.py with lambda function``````

from functools import reduce

Chkeven = lambda num : num % 2 == 0

increase = lambda num : num + 1
 
add = lambda a,b : a+b

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

def main():
    try:
        data = []
 
        while True:
            data.append(int(input("Enter the array: ")))
    except:
        print(data)
        print("The data is: ", data)

    Fdata = list(filterX(Chkeven,data))
    print("Data after filter activity: ",Fdata)

    Mdata = list(mapX(increase, Fdata))
    print("Data after map actitvity: ",Mdata)

    Rdata = reduceX(add,Mdata)
    print("Data after reducing activity: ", Rdata)

if __name__ == "__main__":
    main()