def mod_inverse(k):
    for i in range(26):
        if (k * i) % 26 == 1:
            return i
    return None


def encrypt_multiplicative(plaintext, key):
    cipher = ""
    for ch in plaintext.lower():
        base = ord('a')
        cipher += chr(((ord(ch) - base) * key) % 26 + base)
    return cipher


def decrypt_multiplicative(ciphertext, key):
    plain = ""
    inv = mod_inverse(key)
    for ch in ciphertext:
        base = ord('a')
        plain += chr(((ord(ch) - base) * inv) % 26 + base)
    return plain


def brute_force_multiplicative(ciphertext):
    results = {}
    valid_keys = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    for key in valid_keys:
        decrypted = decrypt_multiplicative(ciphertext, key)
        results[key] = decrypted

    return results


def main():
    text = "hello world"
    key = 5 

    print("النص الأصلي:", text)
    encrypted = encrypt_multiplicative(text, key)
    print("النص المشفّر :", encrypted)

    decrypted = decrypt_multiplicative(encrypted, key)
    print("النص المفكوك :", decrypted)

    print("\nنتائج الهجوم الأعمى:")
    brute_results = brute_force_multiplicative(encrypted)
    for k, v in brute_results.items():
        print(f"المفتاح {k}: {v}")


if __name__ == "__main__":
    main()
