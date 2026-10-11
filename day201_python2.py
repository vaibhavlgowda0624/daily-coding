import secrets

otp = "".join(
    str(secrets.randbelow(10))
    for _ in range(6)
)

print("Your OTP:", otp)
