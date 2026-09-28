import os
import json
from cryptography.fernet import Fernet

class StateManager:
    def __init__(self, key):
        self.key = Fernet(key.encode())
        self.path = "./state/state.json"
        if not os.path.exists("./state"):
            os.makedirs("./state")
        if not os.path.exists(self.path):
            self.save({})

    def load(self):
        with open(self.path, "rb") as f:
            encrypted = f.read()
        decrypted = self.key.decrypt(encrypted)
        return json.loads(decrypted)

    def save(self, data):
        encrypted = self.key.encrypt(json.dumps(data).encode())
        with open(self.path, "wb") as f:
            f.write(encrypted)
