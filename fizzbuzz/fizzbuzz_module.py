def fizzbuzz(number):
    to_return = number
    if number % 15 == 0:
        to_return = "FizzBuzz"
    elif number % 5 == 0:
        to_return = "Buzz"
    elif number % 3 == 0:
        to_return = "Fizz"
    return to_return


def main():
    for i in range(1, 101):
        print(fizzbuzz(i))
    return

if __name__ == '__main__':
    main()
