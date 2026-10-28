import os

os.environ["APP_MODE"] = "development"

mode = os.getenv("APP_MODE")
print("Application mode:", mode)
