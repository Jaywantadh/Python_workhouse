i = 1
def rec(num):
    global i

    if(i <= num == 0):
        print(i)
        i = i + 1

        rec(num)

def main():
    num = int(input("input:"))
    rec(num)

if __name__ == "__main__":
    main()