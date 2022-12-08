#!/usr/bin/env python3

# Created by : Joanne Santhosh
# Created on : Dec 2022
# This program prints out your address using default function parameters


# this function formats the address
def format_address(
    full_name
    apartment_number = None
    street_number
    street_name
    city
    provice
    postal_code
):

    # format address
    format = full_name + "\n"
    formatted = formatted + str(street_number)
    if apartment_number != None:
        formatted = formatted + "-" + str(apartment_number)
    formatted = formatted + " " + street_name + "\n"
    formatted = formatted + city + " "
    formatted = formatted + province + "  "
    formatted = formatted + postal_code

    return formatted

def main():
    # gets a users name and prints out their formal name
    middle_name = None

    first_name = input("Enter your first name: ")
    question = input("Do you have a middle name? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")

    if middle_name != None:
        name = full_name(first_name, last_name, middle_name)
    else:
        name = full_name(first_name, last_name)

    print(name)

if __name__ == "__main__":
    main()