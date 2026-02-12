import os
import sys
from cryptography.fernet import Fernet

#misma clave
key = sys.argv[1].encode()
cipher = Fernet(key)

for root, dirs, files in os.walk("/home/snownerian/Desktop/archivos"):
	for file in files:
		if file.endswith(('.locked')):
			file_path = os.path.join(root, file)

			try:
				with open(file_path, 'rb') as f:
					data = f.read()
					
					decrypted = cipher.decrypt(data)
					original = file_path.replace('.locked', '')

					with open(original, 'wb') as f:
						f.write(decrypted)

					os.remove(file_path)		
			except:
				pass


print(f"\n[!] todos los archivos han sido decifrados\n")

