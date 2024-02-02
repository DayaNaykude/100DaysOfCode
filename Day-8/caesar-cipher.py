alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# logo
from art import logo
print(f"{logo}\n")



# # encrypt the message
# def encrypt(plain_text, shift):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         cipher_text += alphabet[(position + shift) % len(alphabet)]
#     print(f"The encoded text {cipher_text}")

# #  decrypt the message
# def decrypt(cipher_text, shift):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         if new_position < 0:
#             new_position = len(alphabet) + new_position
        
#         plain_text += alphabet[new_position]
#     print(f"The decoded text {plain_text}")

end_of_cipher_program = False
# combine both function
def caesar(start_text, shift_number, cipher_direction):
    result = ""
    alphabet_lenght = len(alphabet)
    for letter in start_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            new_position=0
            if cipher_direction == "encode":
                new_position = position + shift_number
                if new_position > alphabet_lenght:
                    new_position = new_position % alphabet_lenght
            else:
                new_position = position - shift_number
                if new_position < 0:
                    new_position = len(alphabet) + new_position

            result += alphabet[new_position]  
        else:
            result += letter  
    print(f"The {direction} text {result}")

while not end_of_cipher_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text =  input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_choice = input("Do you want to countinue the program? if yes type 'Yes' else type 'No.\n").lower()
    if user_choice == "no":
        end_of_cipher_program = True
        print("Goodbye")

