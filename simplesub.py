import random

alphabet = 'abcdefhijklmnopqrstuvwxyz'

class SimpleSubCipher:
    def __init__(self, key=None):
        if key:
            self.key = key.lower()
        else:
            self.key = ''.join(random.sample(alphabet, len(alphabet)))
    
    def encrypt(self, plaintext: str) -> str:
        ciphertext = ''
        for char in plaintext:
            if char not in alphabet:
                ciphertext += char
                continue
            ciphertext += self.key[alphabet.index(char)]
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        plaintext = ''
        for char in ciphertext:
            if char not in alphabet:
                plaintext += char
                continue
            plaintext += alphabet[self.key.index(char)]
        return plaintext
    
    def __str__(self):
        return 'SimpleSubCipher'

def test(message):
    cipher = SimpleSubCipher()
    if cipher.decrypt(cipher.encrypt(message)) == message:
        print('[\033[92mOK\033[0m] SimpleSubCipher (simplesub.py)')
    else:
        print('[\033[92mERR\033[0m] SimpleSubCipher (simplesub.py)')
    print(f'\tMessage: {message}')
    print(f'\tCiphertext: {cipher.encrypt(message)}')
    print(f'\tDecrypt: {cipher.decrypt(cipher.encrypt(message))}')

if __name__ == '__main__':
    test('hello world')