#``````same code as FMR1.py with lambda function``````

from functools import reduce

Chkeven = lambda num : num % 2 == 0

increase = lambda num : num + 1
 
add = lambda a,b : a+b

def main():
    data = [14,13,15,16,17,18,20]
    print("The data is: ", data)

    Fdata = list(filter(Chkeven,data))
    print("Data after filter activity: ",Fdata)

    Mdata = list(map(increase, Fdata))
    print("Data after map actitvity: ",Mdata)

    Rdata = reduce(add,Mdata)
    print("Data after reducing activity: ", Rdata)

if __name__ == "__main__":
    main()