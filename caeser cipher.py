def ceaser_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                encrypted_text += shifted_char.upper()
            else:
                encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


