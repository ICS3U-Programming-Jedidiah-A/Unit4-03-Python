# !/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 18, 2021
# This program calculates the square of each number from 0 to user input.
def main():
    try:
        user_input = int(input("Enter a whole number: "))
        # calculate the square of each number from 0 to user input.
        if user_input <= 0:
            print("Invalid input.")
        else:
            for counter in range(user_input + 1):
                power_of_two = counter**2
                print("{}^2 = {}".format(counter, power_of_two))
    except Exception:
        print("Invalid input.")


if __name__ == "__main__":
    main()
