even_or_odd = lambda num: num%2 == 0


def main():
    number = int(input("Enter a number: "))
    print(even_or_odd(number))

if __name__ == "__main__":
    main()