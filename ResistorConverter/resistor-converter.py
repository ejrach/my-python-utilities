# This script will allow you to:
# 1. Choose by 4 color bands (tell me a value)
# 2. Choose by value (tell me colors)

# TODO:
# make it easier to read the ohm value. for example:
#    300000000 --> 300,000,000 ohms.
# or 300000000 --> 300M ohms
# currently the value is printed as: 300000000.0


from os import system
import re

# value entered:
color_mapping = {
    "0": "Black",
    "1": "Brown",
    "2": "Red",
    "3": "Orange",
    "4": "Yellow",
    "5": "Green",
    "6": "Blue",
    "7": "Violet",
    "8": "Grey",
    "9": "White",
    "a": "Gold",
    "b": "Silver"
}

ohm_multiplier_mapping = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1000,
    "Yellow": 10000,
    "Green": 100000,
    "Blue": 1000000,
    "Violet": 10000000,
    "Grey": 100000000,
    "White": 10000000000,
    "Gold": .1,
    "Silver": .01
}

tolerance_mapping = {
    "Brown": "+/- 1%",
    "Red": "+/- 2%",
    "Green": "+/- 0.5%",
    "Blue": "+/- 0.25%",
    "Violet": "+/- 0.1%",
    "Grey": "+/- 0.05%",
    "Gold": "+/- 5%",
    "Silver": "+/- 10%"
}

multiplier_list = [
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000,
    .1,
    .01
]


def clear():
    _ = system('clear')


def colors_to_value(user_input):
    # This function expects a string value.
    # for example: "564J"

    # first band is the first digit of the resistor value
    # look up the key value corresponding to the color value
    band1_color = color_mapping.get(user_input[0])
    band1_key = list(color_mapping.keys())[
        list(color_mapping.values()).index(band1_color)]

    # second band is the second digit of the resistor value
    # look up the key value corresponding to the color value
    band2_color = color_mapping.get(user_input[1:2])
    band2_key = list(color_mapping.keys())[
        list(color_mapping.values()).index(band2_color)]

    # third band is the multiplier of the resistor value
    band3_color = color_mapping.get(user_input[2:3])
    band3_multiplier = ohm_multiplier_mapping.get(band3_color)

    # fourth band is the tolerance of the resistor value
    band4_color = color_mapping.get(user_input[-1])
    band4_tolerance = tolerance_mapping.get(band4_color)

    # Build the value using the multipler
    resistor_value = float(band1_key + band2_key) * band3_multiplier

    # return the resistor value along with the tolerance
    return f"{str(resistor_value)} ohms {band4_tolerance}"

# This function displays the menu for selection, validates the user input, calls
# the colors_to_value function and displays the result


def color_band_selection():

    # Print out the color selection menu for the user to select.
    for key, value in color_mapping.items():
        print(f'{key}) {value}')
    print("r) Return to main menu")

    # a color code is entered here
    user_input = input("Enter your selection: ")
    user_input = user_input.lower()

    # TODO more error checking
    if 'r' in user_input:
        # return to calling function
        return
    elif len(user_input) is not 4:
        print("You must enter exactly 4 characters")
        input("Press any key to return to main menu...")
    else:
        # return a string that identifies the value
        msg = colors_to_value(user_input)
        clear()
        print(f"Your resistor value is: {msg}")
        print("")
        input("Press enter to continue...")


def value_to_colors(first_digit, second_digit, multiplier_list_index):
    band1_color = color_mapping.get(first_digit)
    band2_color = color_mapping.get(second_digit)
    multiplier_value = multiplier_list[multiplier_list_index]
    band3_color = list(ohm_multiplier_mapping.keys())[
        list(ohm_multiplier_mapping.values()).index(multiplier_value)]

    value = float(first_digit + second_digit) * multiplier_value

    print("")
    print("*" * 50)
    print(
        f'Your resistor color coding is: {band1_color} {band2_color} {band3_color}: {value} ohms')
    print("*" * 50)
    print("")

    print("Select the 4th band color for specific tolerance:")
    for key, value in tolerance_mapping.items():
        print(f'{key}: {value}')

    input("Press enter to continue...")


def validate_character(user_input):
    validated = True

    if (len(user_input) > 1):
        print("input error --> Too many characters. Try again.")
        return not validated

    if not re.match("^[0-9]*$", user_input):
        print("input error --> Use only number values 0-9. Try again.")
        return not validated

    return validated


while(True):
    clear()

    print("=== 4 Band Resistor selection ===")
    print("1. Choose by color bands (tell me the value)")
    print("2. Choose by value (tell me the color bands)")
    print("3. Quit")

    try:
        choice = int(input("> "))

        if choice is 1:
            # Choose by color bands
            clear()
            print("Select the color by entering the corresponding number value.")
            print("  e.g. for a color band of green, blue, yellow, gold --> enter 564a")
            color_band_selection()

        elif choice is 2:
            # Choose by value
            clear()

            valid_value = False
            while(not valid_value):
                first_digit = input(
                    "Enter the FIRST digit of the value of the resistor (e.g. 5 for 56000): ")
                valid_value = validate_character(first_digit)

            valid_value = False
            while(not valid_value):
                second_digit = input(
                    "Enter the SECOND digit of the value of the resistor (e.g. 6 for 56000): ")
                valid_value = validate_character(second_digit)

            for i, item in enumerate(multiplier_list):
                print(f'{i}) {item}')

            while (True):
                multiplier_list_index = int(input(
                    "Select the multiplier value of the resistor (e.g. 4 for 10000, or think 4 zeros): "))
                if multiplier_list_index in range(0, len(multiplier_list) + 1):
                    break
                else:
                    input(
                        "input error --> Incorrect selection. Press enter to try again.")

            value_to_colors(first_digit, second_digit, multiplier_list_index)

        else:
            clear()
            break

    except ValueError:
        continue
