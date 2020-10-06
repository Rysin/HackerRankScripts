if __name__ == '__main__':
    input_string = "Sorting1234"

    # Make List of Input
    input_string = list(input_string)
    print(input_string)

    lowerCaps = []
    upperCaps = []
    evenDigits = []
    oddDigits = []

    for element in input_string:
        print(type(element))
        if str(element).isupper():
            upperCaps.append(element)
        if str(element).islower():
            lowerCaps.append(element)
        if str(element).isnumeric():
            if int(element) % 2 == 0:
                evenDigits.append(element)
            else:
                oddDigits.append(element)

    # Sort All Lists
    upperCaps.sort()
    lowerCaps.sort()
    evenDigits.sort()
    oddDigits.sort()

    # concatenating list in provided order
    final_string = lowerCaps + upperCaps + oddDigits + evenDigits
    final_string = "".join([letter for letter in final_string])
    print(final_string)
