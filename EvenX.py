def CheckEven(no):
    if(no % 2 == 0):
        print("It is a even number")
    else:
        print("It is a odd number")

def main():
    A = int(input("Enter a number: "))

    CheckEven(A)

#Starter
if __name__ == "__main__":
    main()
