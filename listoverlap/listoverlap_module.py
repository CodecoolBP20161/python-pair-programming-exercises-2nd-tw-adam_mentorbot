from random import randint


def listoverlap(list1, list2):
    return list(set(list1).intersection(set(list2)))


def create_random_list():
    to_return = []
    for i in range(randint(0, 20)):
        to_return += [randint(0, 20)]
    return to_return


def main():
    a = create_random_list()
    b = create_random_list()
    result = listoverlap(a, b)
    print(a)
    print(b)
    print(result)


if __name__ == '__main__':
    main()
