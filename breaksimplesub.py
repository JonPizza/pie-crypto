import simplesub

import random
import time

alphabet = 'abcdefhijklmnopqrstuvwxyz'

def generate_random_key() -> str:
    return ''.join(random.sample(alphabet, len(alphabet)))

def decrypt_with_key(ciphertext: str, key: str) -> str:
    plaintext = ''
    for char in ciphertext:
        if char not in alphabet:
            plaintext += char
            continue
        plaintext += alphabet[key.index(char)]
    return plaintext

def brute(cipher: simplesub.SimpleSubCipher, message: str) -> (float, str):
    start = time.time()
    ciphertext = cipher.encrypt(message)
    key = generate_random_key()
    while decrypt_with_key(ciphertext, key) != message:
        key = generate_random_key()
    end = time.time()
    return end - start, key

def report(message):
    cipher = simplesub.SimpleSubCipher()
    print(f'Brute forcing {cipher} with message {message}...')
    time_to_brute, key = brute(cipher, message)
    print(f'Brute force attack on {cipher} finished in \033[1m{time_to_brute}\033[0m seconds\nKey: {key}')

if __name__ == '__main__':
    report('messw')