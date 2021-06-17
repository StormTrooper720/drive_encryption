import os
from cryptography.fernet import Fernet
from alive_progress import alive_bar
# path = r'F:/encrypt/'
path = input("Enter path, example: /home/ or D:/ : ")
print(f"All files in {path} will be encrypted")
list_of_files = []

for root, dirs, files in os.walk(path):
    for file in files:
        list_of_files.append(os.path.join(root, file))

print(f"Located all files in {path}")
key = Fernet.generate_key()
name_of_file = input("Enter a name for the key so you will remember: ")
with open(f'{name_of_file}.key', 'wb') as key_file:
    key_file.write(key)
print("Created key file, don't delete this file")


def encrypt(filename):
    f = Fernet(key)
    with open(filename, 'rb') as original_file:
        original = original_file.read()
    os.remove(filename)
    encrypted = f.encrypt(original)
    with open(f"{filename}_enc", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


print("Encrypting files... This may take awhile...")
with alive_bar(len(list_of_files)) as bar:
    for name in list_of_files:
        try:
            os.chmod(name, 775)
            encrypt(name)
        except:
            pass
        bar()
print(f"Done! All file in {path} are encrypted")
