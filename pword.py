from passwordmanage import PasswordManager

password_manager = PasswordManager()

password_manager.add_password("wa2wawa3", "baba2baba2", "caca3caca3")

print(password_manager.get_password("example.com"   ))