def selection(i):
    n=0

    if(i <= 0):
        print("Invalid input")
        return
    
    for n in range(i):
        print("Jai Ganesh!", end=" ")

def main():
    i=int(input("Enter the times of iteration: "))
    selection(i)

if __name__ == "__main__":
    main()