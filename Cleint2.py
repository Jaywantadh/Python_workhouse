import Marvellous as M  #Known as alias. gives variable to library. hence this the best practice.

def main():
    print("*****inside main ****")
    A = int(input("Enter the first number: "))

    B = int(input("Enter the second number: "))

    ans = M.addition(A,B)
    print("Addition is: ",ans)

    ans = M.Multipication(A,B)
    print("Multiplication is: ",ans)

main() 