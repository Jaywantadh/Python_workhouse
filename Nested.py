def calculation(No1, No2):
    def addtion(X,Y):
        return X+Y
    def Substration(X,Y):
        return X-Y
    Ans1 = addtion(No1,No2)
    Ans2 = Substration(No1,No2)
    return Ans1, Ans2




A = int(input("enter the first number: "))

B = int(input("Enter the second number: "))

Result1, result2 = calculation(A,B)

print("The addtion of two numbers are: ",Result1)

print("Substraction of two numbers are: ",result2)