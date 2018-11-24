def Function1():
    while True:
        print("Day la function 1")
        option = input("Ban co muon dung khong? y/n")
        if option == "n":
            break
def Function2():
    print("Hello World!!!")
    print("\n")
    while True:
        for i in range(1, 10, 2):
            if i == 5:
                break
def Main():
    Function1()
    Function2()
Main()
