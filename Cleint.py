import Marvellous # imports just the library

from Marvellous import addition #specific import

def main():
    print("*****Inside the main 1*****")
    A = int(input("Enter the first number: "))

    B = int(input("Enter the second number: "))

    ans = addition(A,B)

    print("Addition is: ",ans)

main() 

#OR

def main2():
    print("*****inside main 2****")
    A = int(input("Enter the first number: "))

    B = int(input("Enter the second number: "))

    ans = Marvellous.addition(A,B)
    print("Addition is: ",ans)

    ans = Marvellous.Multipication(A,B)
    print("Multiplication is: ",ans)

main2() 