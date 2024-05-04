from Marvellous import *  #imports all functions at once.

def main2():
    print("*****inside main 2****")
    A = int(input("Enter the first number: "))

    B = int(input("Enter the second number: "))

    ans = addition(A,B)
    print("Addition is: ",ans)

    ans = Multipication(A,B)
    print("Multiplication is: ",ans)

main2() 