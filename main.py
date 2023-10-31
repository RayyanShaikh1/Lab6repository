# encoder function adds 3 to each digit in the password
def encode(password):
    if len(password) != 8 or not password.isdigit():
        return False
    else:
        encoded_pas = ''
        for digit in password:
            original = int(digit)
            encoded_dig = (original + 3) % 10
            encoded_pas += str(encoded_dig)
        return encoded_pas
# decoder functions subtracts 3 from each digit in the encoded password


def decode(password):
    if len(password) != 8 or not password.isdigit():
        return False
    else:
        decoded_pas = ''
        for digit in password:
            encoded = int(digit)
            decoded_dig = (encoded - 3) % 10
            decoded_pas += str(decoded_dig)
        return decoded_pas


new_password = ''
# main while loop
while True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    option = int(input('Please enter an option: '))
    if option == 1:
        password = input('Please enter your password to encode: ')
        try:
            new_password += encode(password)
            print('Your password has been encoded and stored!')
        except:
            print("error message")
    if option == 2:
        print(f'The encoded password is {new_password} and the original password is {decode(new_password)}.')
        new_password = ''
    if option == 3:
        break
        
