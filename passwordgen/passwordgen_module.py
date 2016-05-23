from random import randint

word_list_path = '/usr/share/dict/words'


abc = ["0123456789",
       "ABCDEFGHIJKLMNOPQRSTUVXYZ",
       "abcdefghijklmnopqrstuvxyz",
       "!@#$%^&*()?"]


def wordsgen():
    f = open(word_list_path, "r")
    words = f.readlines()

    word_1 = words[randint(0, len(words))].strip()
    word_2 = words[randint(0, len(words))].strip()

    return word_1 + " " + word_2


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
    while True:
        mode = input("Weak or a strong password? (weak/strong)").lower()
        if mode in ["weak", "strong"]:
            break
    password = wordsgen() if mode == "weak" else passwordgen()
    print(password)


if __name__ == '__main__':
    main()
