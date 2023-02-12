import socket

# Inicializar el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtener el host y el puerto del servidor
host = socket.gethostname()
port = 12345

# Vincular el socket del servidor a una dirección y un puerto específicos
server_socket.bind((host, port))

# Escuchar solicitudes entrantes hasta un máximo de 5
server_socket.listen(5)
print("El servidor está escuchando...")

while True:
    # Aceptar solicitudes entrantes
    client_socket, client_address = server_socket.accept()
    print("Se ha establecido una conexión desde:", client_address)

    # Recibir datos del cliente
    client_data = client_socket.recv(1024)
    print("Datos recibidos del cliente:", client_data.decode())

    # Enviar datos de respuesta al cliente
    response = "Gracias por conectarse al servidor"
    client_socket.send(response.encode())

    # Cerrar el socket del cliente
    client_socket.close()

# Cerrar el socket del servidor
server_socket.close()