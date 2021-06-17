import os
import time
from cryptography.fernet import Fernet
from alive_progress import alive_bar
# path = r'F:/encrypt/'
path = input("Enter path, example: /home/ or D:/ : ")
print(f"All files in {path} will be decrypted")
list_of_files = []

for root, dirs, files in os.walk(path):
    for file in files:
        list_of_files.append(os.path.join(root, file))

print(f"Located all files in {path}")
name_of_file = input("Enter name of key file, example: key.key : ")
print("Opening key file")
with open(name_of_file, 'rb') as key_file:
    key = bytes(key_file.read())


def decrypt(filename):
    f = Fernet(key)
    with open(filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    os.remove(filename)
    try:
        decrypted = f.decrypt(encrypted)
        with open(filename[:-4], 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
    except:
        print("An error has occurred, you might have the wrong encryption key")


print("Decrypting files... This may take awhile...")
with alive_bar(len(list_of_files)) as bar:
    for name in list_of_files:
        decrypt(name)
        bar()
print(f"Done! All Files in {path} decrypted")
