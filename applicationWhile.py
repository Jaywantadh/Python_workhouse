def selection(cnt):
    i=0

    if(cnt <= 0):
        print("Invalid input")
        return
    
    while(i < cnt):
        print("Jai Ganesh!", end=" ")
        i = i + 1

def main():
    i=int(input("Enter the times of iteration: "))
    selection(i)

if __name__ == "__main__":
    main()