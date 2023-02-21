import socket

def start_client():
    # Inicializar el socket del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Obtener el host y el puerto del servidor
    host = socket.gethostname()
    #host = '192.168.18.36'
    port = 12345

    # Conectarse al servidor
    client_socket.connect((host, port))
    return client_socket

def submit_request(client_socket,request):
    # Enviar una solicitud al servidor
    client_socket.send(request.encode())

    # Recibir la respuesta del servidor
    response = client_socket.recv(1024)
    return (response.decode())

def close_socket(client_socket):
    # Cerrar el socket del cliente
    client_socket.close()