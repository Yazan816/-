def rc4_key_schedule(key):
    """
    RC4 Key Scheduling Algorithm (KSA)
    يرجع مصفوفة S بعد تهيئتها بالمفتاح
    """

    # تحويل المفتاح إلى قائمة قيم رقمية
    key = [ord(c) for c in key]

    # إنشاء المصفوفة S
    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]  # تبديل القيم

    return S


def main():
    key = "mysecret"  # مثال
    S = rc4_key_schedule(key)
    print("RC4 Key Schedule (S array):")
    print(S)


if __name__ == "__main__":
    main()
