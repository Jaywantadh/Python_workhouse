i = 1

def rec(num):
    global i
    if(num >= 0):
        print(num)
        num = num - 1

        rec(num)

def main():
    i = int(input("input:"))
    rec(i)

if __name__ == "__main__":
    main()