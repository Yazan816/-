def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.lower()
    key = key.lower()

    cipher = ""
    key_index = 0
    key_len = len(key)

    for ch in plaintext:
            p = ord(ch) - ord('a')
            k = ord(key[key_index % key_len]) - ord('a')
            cipher += chr((p + k) % 26 + ord('a'))
            key_index += 1

    return cipher


def decrypt_vigenere(ciphertext, key):
    ciphertext = ciphertext.lower()
    key = key.lower()

    plain = ""
    key_index = 0
    key_len = len(key)

    for ch in ciphertext:
            c = ord(ch) - ord('a')
            k = ord(key[key_index % key_len]) - ord('a')
            plain += chr((c - k) % 26 + ord('a'))
            key_index += 1

    return plain


def main():
    text = "helloworld"
    key = "key"

    print("النص الأصلي:", text)
    encrypted = encrypt_vigenere(text, key)
    print("النص المشفّر :", encrypted)

    decrypted = decrypt_vigenere(encrypted, key)
    print("النص المفكوك :", decrypted)


if __name__ == "__main__":
    main()
