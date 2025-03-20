from random import randint

def resta_hasta_random():
    num = randint(0, 10)
    if num <= 0:
        print("-----")
    else:
        resta_hasta_random()
        print(num)


def main():
    resta_hasta_random()


main()
