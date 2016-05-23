import datetime
from datetime import date


def years(age):
    this_year = date.today().year
    return this_year+100-age


def main():
    name = input("What's your name?")
    try:
        age = int(input("What's your age?"))
    except ValueError:
        print("Give me a number next time you piece of shit!")
        exit()

    date = years(age)

    if age >= 100:
        print("Hey" + name + ", you've already turned 100 in " + str(date))
    else:
        print("Hey " + name + ", you'll turn 100 in " + str(date))

    return


if __name__ == '__main__':
    main()
