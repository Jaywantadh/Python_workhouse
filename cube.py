cube = lambda num: num**3

def main():
    num = (int(input("Enter a number: ")))
    ret = cube(num)
    print("cube is: ",ret)

if __name__ == "__main__":
    main()