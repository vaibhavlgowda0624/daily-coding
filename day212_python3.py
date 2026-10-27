import logging

logging.basicConfig(level=logging.INFO)

def login(username):
    logging.info("Login attempt for %s", username)
    print(f"Welcome, {username}!")

login("student01")
