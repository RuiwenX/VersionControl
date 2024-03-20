def main():
    password = None

    while True:
        print("Menu")
        print("-------------")

        # options
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            password = encode(password)
            print()

        elif option == "2" and password is not None:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
            print()

        elif option == '3':
            break


def encode(password):  # encoder: Ruiwen Xiong, using account RuiwenX
    num_list = []
    num_list[:] = password
    for i in range(len(password)):
        num_list[i] = (int(num_list[i]) + 3) % 10
    new_password = ""
    for letter in num_list:
        new_password += str(letter)

    return new_password


def decode(password):  # decoded
    num_list = []
    num_list[:] = password
    for i in range(len(password)):
        num_list[i] = (int(num_list[i]) + 7) % 10
    new_password = ""
    for letter in num_list:
        new_password += str(letter)

    return new_password


if __name__ == "__main__":
    main()
