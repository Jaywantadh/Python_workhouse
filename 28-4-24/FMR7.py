import FMR6 as FMR

Chkeven = lambda num : num % 2 == 0

increase = lambda num : num + 1
 
add = lambda a,b : a+b

def main():
    try:
        data = []
 
        while True:
            data.append(int(input("Enter the array: ")))
    except:
        print(data)
        print("The data is: ", data)

    Fdata = list(FMR.filterX(Chkeven,data))
    print("Data after filter activity: ",Fdata)

    Mdata = list(FMR.mapX(increase, Fdata))
    print("Data after map actitvity: ",Mdata)

    Rdata = FMR.reduceX(add,Mdata)
    print("Data after reducing activity: ", Rdata)

if __name__ == "__main__":
    main()