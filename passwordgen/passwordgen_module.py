from random import randint


abc = ["0123456789",
       "ABCDEFGHIJKLMNOPQRSTUVXYZ",
       "abcdefghijklmnopqrstuvxyz",
       "!@#$%^&*()?"]


def passwordgen():
    while True:
        abc_used = [False] * 4
        password = ""
        for i in range(8):
            rand_abc = randint(0, 3)
            abc_used[rand_abc] = True
            chars = abc[rand_abc]
            password += chars[randint(0, len(chars)-1)]

        if abc_used == [True] * 4:
            break

    return password


def main():
    print(passwordgen())
    return


if __name__ == '__main__':
    main()
