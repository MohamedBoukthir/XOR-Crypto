def encrypt_block(plain_text, key):
    # Initialise une liste vide pour stocker le texte chiffré
    encrypted_text = []

    # Itère sur chaque paire de lettres dans le bloc de texte clair et la clé
    for char, key_char in zip(plain_text, key):
        # Effectue l'opération XOR et ajoute le résultat à la liste
        encrypted_text.append(chr(ord(char) ^ ord(key_char)))

    # Convertit la liste de caractères en une chaîne de texte
    return ''.join(encrypted_text)

def decrypt_block(cipher_text, key):
    # Utilise la fonction encrypt_block car l'opération XOR est réversible
    return encrypt_block(cipher_text, key)

# Exemple concret
plain_text_block = "CRYPTOGRAPHY"
key_used = "KEY"

# Chiffrement
encrypted_result = encrypt_block(plain_text_block, key_used)
print("Texte chiffré :", encrypted_result)
# Déchiffrement
decrypted_result = decrypt_block(encrypted_result, key_used)
print("Texte déchiffré :", decrypted_result)
