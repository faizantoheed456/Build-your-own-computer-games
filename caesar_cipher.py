# Caesar Cipher

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_SHIFT_VALUE = len(SYMBOLS)

def getMode():
    """Asking user if they want to encrypt or decrypt the message"""

    while True:

        print("Do you wish to encrypt or decrypt or brute-force your message? ")
        mode = input().lower()

        if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b"')


def getMessage():
    """Telling user to input a message"""

    print('Enter your message: ')
    return input()


def getKey():
    """Getting the key from user and return it"""

    key = 0

    while True:

        print(f'Enter the key number (1-{MAX_SHIFT_VALUE}): ')
        key = int(input())

        if (key >= 1 and key <= MAX_SHIFT_VALUE):
            return key


def getTranslatedMessage(mode, message, key):
    """Returns the encrypted or decrypted message"""

    if mode[0] == 'd':
        key = -key

    translated = ''

    for symbol in message:
        
        symbolIndex = SYMBOLS.find(symbol)

        if symbolIndex == -1:
            translated += symbol
            continue
        else:
            symbolIndex += key

        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)
        
        translated += SYMBOLS[symbolIndex]

    return translated


mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()

print("Your translated message is : ")

if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))

else:
    for key in range(1, MAX_SHIFT_VALUE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))