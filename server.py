import socket
import threading
import Question

# Define una función para recibir los datos del cliente
def receive_data(client_socket,client_address):
    while True:
        # Recibir datos del cliente
        client_data = client_socket.recv(1024)
        # Si no hay más datos, cierra el socket del cliente y sale del bucle
        if not client_data:
            break
        print("Datos recibidos del cliente: ", client_address, client_data.decode())

        # Enviar datos de la pregunta como respuesta al cliente
        data_list = Question.generate_question()
        client_socket.send('\n'.join(data_list).encode())

    # Cerrar el socket del cliente
    client_socket.close()

# Inicializar el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtener el host y el puerto del servidor
host = socket.gethostname()
#host = '192.168.18.36'
port = 12345

# Vincular el socket del servidor a una dirección y un puerto específicos
server_socket.bind((host, port))

# Escuchar solicitudes entrantes
server_socket.listen()
print("El servidor está escuchando...")

# Espera a que lleguen conexiones de clientes y crea un hilo para cada cliente conectado
while True:
    # Aceptar solicitudes entrantes
    client_socket, client_address = server_socket.accept()
    print("Se ha establecido una conexión desde:", client_address)

    # Crea un nuevo hilo para el cliente conectado y ejecuta la función receive_data en segundo plano
    client_thread = threading.Thread(target=receive_data, args=(client_socket,client_address))
    client_thread.start()

# Cerrar el socket del servidor
server_socket.close()