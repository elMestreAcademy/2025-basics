

def resta_hasta_0(num):
    if num <= 0:
        print("-----")
    else:
        num -= 1
        resta_hasta_0(num)
        print(num)

    print('.............')


def main():
    resta_hasta_0(1)
    print('**************')


main()
