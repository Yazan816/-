def encrypt_autokey(plaintext, key):
    plaintext = plaintext.lower()
    key = key.lower()
    full_key = key + plaintext

    cipher = ""
    for i, ch in enumerate(plaintext):
            p = ord(ch) - ord('a')
            k = ord(full_key[i]) - ord('a')
            cipher += chr((p + k) % 26 + ord('a'))

    return cipher


def decrypt_autokey(ciphertext, key):
    ciphertext = ciphertext.lower()
    key = key.lower()

    plain = ""
    full_key = key  

    for i, ch in enumerate(ciphertext):
            c = ord(ch) - ord('a')
            k = ord(full_key[i]) - ord('a')
            p = (c - k) % 26
            decrypted_char = chr(p + ord('a'))

            plain += decrypted_char
            full_key += decrypted_char 


    return plain


def main():
    text = "helloworld"
    key = "key"

    print("النص الأصلي:", text)
    encrypted = encrypt_autokey(text, key)
    print("النص المشفّر :", encrypted)

    decrypted = decrypt_autokey(encrypted, key)
    print("النص المفكوك :", decrypted)


if __name__ == "__main__":
    main()
