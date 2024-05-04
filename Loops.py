def displayF():
    print("Insdie Display of for loop")
    for i in range(1,6):
        print(i)

def displayW():
    print("Inside Display of while loop")
    no = 1
    while(no <=5):
        print(no)
        no = no + 1 

def main():
    displayF()
    displayW()


if __name__ == "__main__":
    main()