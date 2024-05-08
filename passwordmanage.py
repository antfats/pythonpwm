import hashlib
import json
import os
 
class PasswordManager: 
    def __init__(self,storage_file="passwords.json"):
        self.storage_files = storage_file
        self.passwords = {}

        if os.path.exist(storage_file):
            with open(storage_file,"r")as f: 
                self.passwords = json.load(f)
                
def _save_passwords(self):
    with open(self.storage_file,"w") as f:
        json.dump(self.passwords, f, indent=4)


