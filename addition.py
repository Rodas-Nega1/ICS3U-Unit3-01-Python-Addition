#!/usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sep 2021
# This program calculates addition with user input


def main():
    # this function calculates addition of two numbers inputted by the user

    # input
    number_1 = int(input("Enter the first number to add (integer): "))

    # input
    number_2 = int(input("Enter the second number to add (integer): "))

    # process
    answer = number_1 + number_2

    # output
    print("")
    print("The sum is", answer)
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
