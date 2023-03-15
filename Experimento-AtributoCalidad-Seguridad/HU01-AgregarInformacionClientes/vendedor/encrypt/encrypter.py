from cryptography.fernet import Fernet

# Generar una clave de cifrado
#key = Fernet.generate_key()

with open('../resources/llave.key', 'rb') as f:
   key = f.read()

print (f"llave de cifrado:{key}")
# Crear un objeto Fernet con la clave generada
cipher = Fernet(key)

# Cifrar un mensaje
#message = b"hola david como estas???"
#encrypted_message = cipher.encrypt(message)

# Desencriptar el mensaje
decrypted_message = cipher.decrypt("gAAAAABkETggdCebF5VYU43vLy4SV1uas6O1ON2BLjgXeQVmUdw95BeHybAuBAnYWKvuRXyqdhaAJQ4hv7n6kM3Ejl9ZM96j02CMvpwR10w7DA0uDMWjvf4=")

#print(f"Mensaje original: {message}")
#print(f"Mensaje cifrado: {encrypted_message}")
print(f"Mensaje descifrado: {decrypted_message}")
