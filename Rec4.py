i = 1
def rec():
    global i

    if(i <= 5):
        print(i)
        i = i + 1

        rec()

def main():
    rec()

if __name__ == "__main__":
    main()