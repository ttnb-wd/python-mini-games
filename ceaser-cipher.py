alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text, shift_amount, direction):
    final_text = ""
    if direction == "decode":
        shift_amount = shift_amount * -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else:
            final_text += char
        
    print(f"{direction}ed message is {final_text}")
        
is_end = False
while not is_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    
    ceaser(text=message, shift_amount=shift, direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if restart == "no":
       is_end = True
       print("Goodbye")        
