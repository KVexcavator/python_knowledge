# Криптографически стойкий генератор паролей

import secrets
import string

def gen_password(length: int = 12) -> str:
    if length < 8:
        raise ValueError("Длина пароля должна быть не меньше 8 символов.")
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits    = string.digits
    specials  = "!@#$%^&*()-_=+[]{};:,.<>?/"
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(specials)
    ]
    all_chars = lowercase + uppercase + digits + specials
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

if __name__ == "__main__":
    print(gen_password(16))
