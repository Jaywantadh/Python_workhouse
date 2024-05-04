#``````same code as FMR1.py with lambda function``````

from functools import reduce

def main():
    data = [14,13,15,16,17,18,20]
    print("The data is: ", data)

    Fdata = list(filter(lambda num : num % 2 == 0,data))
    print("Data after filter activity: ",Fdata)

    Mdata = list(map((lambda num : num + 1), Fdata))
    print("Data after map actitvity: ",Mdata)

    Rdata = reduce((lambda a,b : a+b), Mdata)
    print("Data after reducing activity: ", Rdata)

if __name__ == "__main__":
    main()