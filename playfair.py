def generate_matrix(key):
    key = key.lower().replace("j", "i")
    matrix = []
    used = set()

    for ch in key:
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    for ch in "abcdefghiklmnopqrstuvwxyz":  
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    return [matrix[i*5:(i+1)*5] for i in range(5)]


def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None


def prepare_text(text):
    text = text.lower().replace("j", "i")
    cleaned = ""

    for ch in text:
        if ch.isalpha():
            cleaned += ch

    # تقسيم إلى أزواج + معالجة التكرار
    pairs = []
    i = 0
    while i < len(cleaned):
        a = cleaned[i]
        b = "x"

        if i + 1 < len(cleaned):
            if cleaned[i + 1] != a:
                b = cleaned[i + 1]
                i += 2
            else:
                b = "x"
                i += 1
        else:
            b = "x"
            i += 1

        pairs.append((a, b))

    return pairs


def encrypt_playfair(plaintext, key):
    matrix = generate_matrix(key)
    pairs = prepare_text(plaintext)
    cipher = ""

    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # نفس الصف
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:  # نفس العمود
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]
        else:  # مستطيل
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def decrypt_playfair(ciphertext, key):
    matrix = generate_matrix(key)
    plaintext = ""

    # تقسيم النص إلى أزواج
    pairs = [(ciphertext[i], ciphertext[i+1]) for i in range(0, len(ciphertext), 2)]

    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # نفس الصف
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:  # نفس العمود
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]
        else:  # مستطيل
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


def main():
    text = "hello world"
    key = "keyword"

    print("النص الأصلي:", text)
    encrypted = encrypt_playfair(text, key)
    print("النص المشفّر :", encrypted)

    decrypted = decrypt_playfair(encrypted, key)
    print("النص المفكوك :", decrypted)


if __name__ == "__main__":
    main()
