# luca weisman

def decode(encoded_password):
  original_password = ""
  for digit in encoded_password:
    temp = int(digit) - 3
    if temp < 0:
      temp += 10
      original_password += str(temp)
    else:
      original_password += str(temp)

  return original_password

# mia shin

def encode(number):     # encode function, moves up each digit of the 8-digit number by 3
    encoded_num = ""
    for digit in number:
        temp = int(digit) + 3
        if temp >= 10:
            temp %= 10
            encoded_num += str(temp)
        else:
            encoded_num += str(temp)
    return encoded_num



if __name__ == "__main__":
    encoded_password = ""
    while True:
        print("Menu")               # printing menu
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = int(input("Please enter an option: "))

        if option == 3:         # breaking loop if the user select option 3
            break
        elif option == 1:           # encodes if the user selects 1
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:           # decodes if the user selects 2
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
