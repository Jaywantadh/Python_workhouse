def Area(radius, pi = 3.14):
    Result = pi * radius * radius
    return Result

def main():
    Ans = Area(10.7)
    print("Area of circle is: ",Ans)

    Ans = Area(10.7, 7.20)
    print("Area of circle is: ",Ans)

    Ans = Area(radius= 10.7)
    print("Area of circle is: ",Ans)

if __name__ == "__main__":
    main()