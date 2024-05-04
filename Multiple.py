def calculation(No1, No2):
    Add = No1 + No2
    Sub = No1 - No2
    return Add, Sub




A = int(input("enter the first number: "))

B = int(input("Enter the second number: "))

Result1, result2 = calculation(A,B)

print("The addtion of two numbers are: ",Result1)

print("Substraction of two numbers are: ",result2)

