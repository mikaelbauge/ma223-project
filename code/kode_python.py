import random


def main():
    randomlist = []
    for i in range(10000):
        temp = random.randint(1, 100)
        randomlist.append(temp)

    f = open("datainnsamling.txt", "a")
    for i in randomlist:
        f.write(str(i) + '\n')
    f.close()


if __name__ == '__main__':
    main()

