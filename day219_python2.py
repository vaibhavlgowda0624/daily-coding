import secrets

token = secrets.token_urlsafe(32)

print("Generated token:", token)
print("Token length:", len(token))
