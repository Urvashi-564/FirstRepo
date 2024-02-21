import string
alphabets = list(string.ascii_lowercase)
def decrypt():
    decrypted_msg = ''
    for char in message_to_encrpt:
        if char in alphabets:
            position=alphabets.index(char)-shift_key
            position=position%26
            decrypted_msg+=alphabets[position]
        else:
            decrypted_msg = decrypted_msg + char
    print(f"decrypted message is {decrypted_msg}")

def encrypt(message_to_encrpt,shift_key):
    msg=''
    for char in message_to_encrpt:
        if char in alphabets:
            postion=(alphabets.index(char)+shift_key)%26
            msg+=alphabets[postion]
        else:
            msg=msg+char
    print("message_to_encrpt after encryption is:",msg)



print("Hey all welcome to the world of CAESAR CIPHER")

wanna_end=False
while not wanna_end :
    wanna_encrpt_decrypt = input("Type encrypt for encryption and decrypt for decryption: ")
    message_to_encrpt = input("Enter your message: ")
    shift_key = int(input("Type your shift key number: "))
    if wanna_encrpt_decrypt.lower() == 'encrypt':
        encrypt(message_to_encrpt, shift_key)
    if wanna_encrpt_decrypt.lower() == 'decrypt':
        decrypt()
    want_to_end=input("Do you want to exit now say yes")
    if  want_to_end == 'yes':
        wanna_end=True
        print("Have a great day bye")


