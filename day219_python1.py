import hashlib
import secrets

password = "ExamplePassword123"

salt = secrets.token_bytes(16)

password_hash = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode(),
    salt,
    200_000
)

print("Salt:", salt.hex())
print("Hash:", password_hash.hex())
