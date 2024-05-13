import hashlib
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
    

    def _save_passwords(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.passwords, f, indent=4)

    def add_password(self, service, username, password):
        if service in self.passwords:
            print(f"Service '{service}' already exists. Updating password...")
        self.passwords[service] = {"username": username, "password": hashlib.sha256(password.encode()).hexdigest()}
        self._save_passwords()
        print(f"Password for '{service}' added/updated successfully.")

    def get_password(self, service):
        if service in self.passwords:
            return self.passwords[service]
        else:
            return None

    def update_password(self, service, new_password):
        if service in self.passwords:
            self.passwords[service]["password"] = hashlib.sha256(new_password.encode()).hexdigest()
            self._save_passwords()
            print(f"Password for '{service}' updated successfully.")
        else:
            print(f"Password for '{service}' does not exist.")

    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self._save_passwords()
            print(f"Password for '{service}' deleted successfully.")
        else:
            print(f"Password for '{service}' does not exist.")

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

            elif choice == '3':
                service = input("Enter Service Name")
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






# Example usage
if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.run()

    # Add a new password
    #password_manager.add_password("example.com", "user123", "password123")

    # Retrieve a password
    #print(password_manager.get_password("example.com"))

    # Update an existing password
    #password_manager.update_password("example.com", "newpassword123")

    # Delete a password
    #password_manager.delete_password("example.com")

    # List all services
    #print(password_manager.list_services())
