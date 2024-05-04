from functools import reduce

def main():
    
    try:
        data = []
 
        while True:
            data.append(int(input("Enter the array: ")))
    except:
        print(data)
        print("The data is: ", data)
    #OR

    #Data = []

    #Size = int(input("Enter the number of element: "))



    Fdata = list(filter(lambda num : num % 2 == 0,data))
    print("Data after filter activity: ",Fdata)

    Mdata = list(map((lambda num : num + 1), Fdata))
    print("Data after map actitvity: ",Mdata)

    Rdata = reduce((lambda a,b : a+b), Mdata)
    print("Data after reducing activity: ", Rdata)

if __name__ == "__main__":
    main()