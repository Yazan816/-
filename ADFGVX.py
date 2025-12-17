
symbols = "ADFGVX"


def generate_matrix(key):
    key = key.lower().replace("j", "i")
    table_content = ""

    for ch in key:
        if ch not in table_content and (ch.isalpha() or ch.isdigit()):
            table_content += ch

    for ch in "abcdefghiklmnopqrstuvwxyz0123456789":
        if ch not in table_content:
            table_content += ch

    matrix = [list(table_content[i*6:(i+1)*6]) for i in range(6)]
    return matrix


def find_position(matrix, ch):
    for r in range(6):
        for c in range(6):
            if matrix[r][c] == ch:
                return r, c
    return None


def encrypt_adfgvx(plaintext, key_matrix_key, transposition_key):
    plaintext = plaintext.lower().replace("j", "i")

    # 1) إنشاء المصفوفة
    matrix = generate_matrix(key_matrix_key)

    # 2) استبدال Substitution
    substituted = ""
    for ch in plaintext:
        if ch.isalpha() or ch.isdigit():
            r, c = find_position(matrix, ch)
            substituted += symbols[r] + symbols[c]

    # 3) التبديل Transposition
    transposition_key = transposition_key.lower()
    cols = len(transposition_key)

    # بناء الجدول
    table = [substituted[i:i+cols] for i in range(0, len(substituted), cols)]

    # قد نحتاج لملء آخر صف
    if len(table[-1]) < cols:
        table[-1] += "X" * (cols - len(table[-1]))

    # ترتيب الأعمدة حسب المفتاح
    sorted_key = sorted(list(transposition_key))
    ciphertext = ""

    for char in sorted_key:
        col_index = transposition_key.index(char)
        for row in table:
            ciphertext += row[col_index]

    return ciphertext


def decrypt_adfgvx(ciphertext, key_matrix_key, transposition_key):
    transposition_key = transposition_key.lower()

    # 1) إعادة ترتيب الأعمدة لفك التبديل
    cols = len(transposition_key)
    rows = len(ciphertext) // cols

    sorted_key = sorted(list(transposition_key))

    # إنشاء جدول فارغ
    table = [[""] * cols for _ in range(rows)]
    index = 0

    for char in sorted_key:
        col_index = transposition_key.index(char)
        for r in range(rows):
            table[r][col_index] = ciphertext[index]
            index += 1

    # قراءة الجدول بالترتيب الطبيعي
    substituted = ""
    for r in range(rows):
        for c in range(cols):
            substituted += table[r][c]

    # إزالة padding إن وجد
    substituted = substituted.replace("X", "")

    # 2) فك الاستبدال Substitution
    matrix = generate_matrix(key_matrix_key)
    plaintext = ""

    for i in range(0, len(substituted), 2):
        a = substituted[i]
        b = substituted[i+1]

        r = symbols.index(a)
        c = symbols.index(b)

        plaintext += matrix[r][c]

    return plaintext


def main():
    text = "attack at 1200"
    matrix_key = "keyword"
    trans_key = "cipher"

    print("النص الأصلي:", text)
    encrypted = encrypt_adfgvx(text, matrix_key, trans_key)
    print("النص المشفّر :", encrypted)

    decrypted = decrypt_adfgvx(encrypted, matrix_key, trans_key)
    print("النص المفكوك :", decrypted)


if __name__ == "__main__":
    main()

