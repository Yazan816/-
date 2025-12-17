def encrypt_additive(plaintext, key):
    cipher = ""
    for ch in plaintext:
        base = ord('a')
        cipher += chr((ord(ch) - base + key) % 26 + base)
    return cipher


def decrypt_additive(ciphertext, key):
    plain = ""
    for ch in ciphertext:
        base = ord('a')
        plain += chr((ord(ch) - base - key) % 26 + base)
    return plain


def brute_force_additive(ciphertext):
    results = {}
    for key in range(26):
        decrypted = decrypt_additive(ciphertext, key)
        results[key] = decrypted
    return results


def main():
    text = "hello samira"
    key = 5

    print("النص الأصلي:", text)
    encrypted = encrypt_additive(text, key)
    print("النص المشفّر :", encrypted)

    decrypted = decrypt_additive(encrypted, key)
    print("النص المفكوك :", decrypted)

    print("\nنتائج الهجوم الأعمى:")
    brute_results = brute_force_additive(encrypted)
    for k, v in brute_results.items():
        print(f"المفتاح {k}: {v}")

if __name__ == "__main__":
    main()
