import tkinter as tk
import client

# Inicializar el socket del cliente
client_socket = client.start_client()

# Crear la ventana raíz
root = tk.Tk()

# Asignar un título a la ventana
root.title("Mi ventana en Python")

# Configurar el tamaño de la ventana
root.geometry("400x300")

# Deshabilitar la opción de maximizar la ventana
root.resizable(False, False)

# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la ubicación para centrarl la ventana
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 300
x_coord = (screen_width / 2) - (window_width / 2)
y_coord = (screen_height / 2) - (window_height / 2)
root.geometry("{}x{}+{}+{}".format(window_width, window_height, int(x_coord), int(y_coord)))

# Crear un cuadro de texto
label = tk.Label(root, text="Este es un cuadro de texto")
label.pack()

# Crear los botones y asignar acciones
def on_button1_click():
    response = client.submit_request(client_socket, "El botón 1 ha sido presionado")
    print(response,"Botón 1")

button1 = tk.Button(root, text="Botón 1", command=on_button1_click)
button1.pack()

def on_button2_click():
    response = client.submit_request(client_socket, "El botón 2 ha sido presionado")
    print(response,"Botón 2")

button2 = tk.Button(root, text="Botón 2", command=on_button2_click)
button2.pack()

def on_button3_click():
    response = client.submit_request(client_socket, "El botón 3 ha sido presionado")
    print(response,"Botón 3")

button3 = tk.Button(root, text="Botón 3", command=on_button3_click)
button3.pack()

def on_button4_click():
    response = client.submit_request(client_socket, "El botón 4 ha sido presionado")
    print(response,"Botón 4")

button4 = tk.Button(root, text="Botón 4", command=on_button4_click)
button4.pack()

# Ejecutar el bucle de eventos de tkinter
root.mainloop()