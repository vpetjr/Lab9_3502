def decode(encodedPassword):
    newPass = ""
    newDigit = ""
    for digit in encodedPassword:

        if int(digit) >= 3:
            newDigit = int(digit) - 3

        if int(digit) == 0:
            newDigit = "7"

        if int(digit) == 1:
            newDigit = "8"

        if int(digit) == 2:
            newDigit = "9"

        newPass += str(newDigit)

    return newPass