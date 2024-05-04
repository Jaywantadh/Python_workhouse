i = 1
fact = 1

def factorial(num):
    global i
    global fact

    if(num >= 1):
        fact = fact * num
        num = num - 1
        factorial(num)
    return fact

def main():
    i = int(input("input:"))
    factorial(i)

if __name__ == "__main__":
    main()