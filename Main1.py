
def addtion(no1, no2):
    print("*****Inside addition function*****")
    ans = 0
    ans= no1 + no2
    return ans

def main():
    print("****inside Main function****")
    A = int(input("Enter the first number: "))

    B = int(input("Enter the second number: "))

    Result = addtion(A,B)

    print("addtion of two number is: ",Result)

main()
print("======End of application======")