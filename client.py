import socket

# Inicializar el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtener el host y el puerto del servidor
host = socket.gethostname()
port = 12345

# Conectarse al servidor
client_socket.connect((host, port))

# Enviar una solicitud al servidor
request = "Hola servidor, ¿cómo estás?"
client_socket.send(request.encode())

# Recibir la respuesta del servidor
response = client_socket.recv(1024)
print("Respuesta del servidor:", response.decode())

# Cerrar el socket del cliente
client_socket.close()