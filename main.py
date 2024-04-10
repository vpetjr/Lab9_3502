def menu():
    print("\nMenu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Exit\n")

def encode(password):
    passwordList = []
    encodedPassword = ""

    passwordList.extend(password)
    for number in passwordList:
        number = int(number)
        number += 3
        number = str(number)
        encodedPassword += number
    return encodedPassword

if __name__ == "__main__":
    while True:
        menu()
        option = (input("Please enter an option: "))

        if option.isdigit():
            option = int(option)
            if option == 1:
                password = input("Please enter your password to encode: ")
                newPass = encode(password)
                print("Your password has been encoded and stored!")
            elif option == 2: #in progress
                pass
                #oldPass = decode(newPass)
                #print(f"The encoded password is {newPass}, and the original password is {oldPass}.")
            elif option == 3:
                break
            else:
                print("Invalid option. Please try again.")
        else:
            print("Invalid option. Please try again.")