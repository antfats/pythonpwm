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

def add_password(self, service, username, password):
    if service  in self.passwords: 
        print(f"Service '{service}' already exists. Updating password...")
        self.passwords[service] = {"username": username, "password": hashlib.sha256(password.encode()). hexdigest()}
        self.save_passwords()
        print (f"Password for '{service}' added/updated sucessfully.")

def get_password(self,service): 
    if service in self.passwords: 
        return self.passwords[service]
    else:
        return None
    
