def main():
    #write your code below this line

    amount = 0
    total = 0

    while True:

        number = int(input("Enter a number: "))

        if number > 0:
            amount = amount + 1
            total = total + number
        elif number == 0 and total > 0:
            average = total / amount
            print(f"The average of the positive numbers is: {average}.")
            break
        elif number == 0 and total <= 0:
            print("Cannot calculate the average.")
            break


if __name__ == '__main__':
    main()
