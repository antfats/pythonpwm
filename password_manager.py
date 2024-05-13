
import bcrypt
import json
import os

class PasswordManager:
    def __init__(self, storage_file="passwords.json"):
        self.storage_file = storage_file
        self.passwords = {}
        try:
            if os.path.exists(storage_file):
                with open(storage_file, "r") as f:
                    self.passwords = json.load(f)
        except json.decoder.JSONDecodeError: 
            print(f"Error: '{storage_file}' does not contain valid json or is empty")
    
    #Add, remove, update, and delete functions maybe replace delete password with delete service + password?
    def _save_passwords(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.passwords, f, indent=4)

    def add_password(self, service, username, password):
        if service in self.passwords:
            print(f"Service '{service}' already exists. Updating password...")
        hashed_password = self._hash_password(password)
        self.passwords[service] = {"username": username, "hashed password:": hashed_password}
        self._save_passwords()
        print(f"Password for '{service}' added/updated successfully.")

    def _hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hashed_password.decode()

    def verify_password(self,service,provided_password):
        if service in self.passwords:
            stored_hashed_password = self.passwords[service]["hashed_password"]
            return bcrypt.checkpw(provided_password.encode(), stored_hashed_password.encode())
        else:
            return False
    def get_password(self, service):
        if service in self.passwords:
            return self.passwords[service]
        else:
            print(f"No password found for service '{service}'.")
        return None




   # update password using bcrypt
   
    def update_password(self, service, new_password):
        if service in self.passwords:
            hashed_password = self._hash_password(new_password)
            self.passwords[service]["password"] = hashed_password
            self._save_passwords()
            print(f"Password for '{service}' updated successfully.")
        else:
            print(f"Password for '{service}' does not exist.")

    def _hash_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hashed_password.decode()


    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self._save_passwords()
            print(f"Password for '{service}' deleted successfully.")
        else:
            print(f"Password for '{service}' does not exist.")

    #Print Menu options
    def list_services(self):
        return list(self.passwords.keys())
    def display_menu(self):
        print ("\nMenu:")
        print ("1. Add password")    
        print ("2. Update Password")
        print ("3. Get Password")
        print ("4. Delete Password")
        print ("5. List Services")
        print ("6. Exit")


    #Main Menu, define the operation
    def run(self):
        while True: 
            self.display_menu()
            choice = input("Enter your choice! ")

            if choice == '1':
                service = input("Enter Service Name: ")
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                self.add_password(service, username, password)
            elif choice == '2':
                service = input("Enter service name: ")
                new_password = input("Enter a new password: ")
                self.update_password(service,new_password)

            #get password from service
            elif choice == '3':
                service = input("Enter Service Name ")
                print("Your Password is: ", self.get_password(service))

            elif choice == '4':
                service = input("Enter the service that would like to delete: ")
                self.delete_password(service)
            elif choice == '5':
                print ("Services",self.list_services())
            elif choice == '6':
                print ("Exiting...")
                break
            else:
                print("Invalid choice please try again")






# Start program
if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.run()
