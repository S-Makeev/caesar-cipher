from caesar_cipher.corpus_loader import word_list, name_list
import string

def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha() and char.lower() in string.ascii_lowercase:
            upper = char.isupper()
            char = char.lower()
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            if upper:
                shifted = shifted.upper()
            encrypted_text += shifted
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)



def crack(encrypted_text):
    for shift in range(26):
        valid_words = 0
        unencrypted_text = encrypt(encrypted_text, shift)
        list_word = unencrypted_text.split()
        for letter in list_word:
            if letter in name_list or letter in word_list:
                valid_words += 1
        if (valid_words / len(list_word)) > 0.5:
            return ' '.join(list_word)
    return ''

if __name__ == '__main__':
    plain_text = "It was the best of times, it was the worst of times."


