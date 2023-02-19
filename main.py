import tkinter as tk
import client
from PIL import ImageTk, Image


# Inicializar el socket del cliente
client_socket = client.start_client()

# Crear la ventana raíz
root = tk.Tk()

# Asignar un título a la ventana
root.title("Mi ventana en Python")

# Configurar el tamaño de la ventana
root.geometry("800x600")

# Deshabilitar la opción de maximizar la ventana
root.resizable(False, False)

# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la ubicación para centrarl la ventana
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 800
window_height = 600
x_coord = (screen_width / 2) - (window_width / 2)
y_coord = (screen_height / 2) - (window_height / 2)
root.geometry("{}x{}+{}+{}".format(window_width, window_height, int(x_coord), int(y_coord)))

# Crear un Frame para poder mover los botones y el texto
frame = tk.Frame(root, width=800, height=600, bg="blue")
frame.pack()
frame.place(x=0, y=0)

# Cargar la imagen
image = Image.open("mi_imagen.png")
photo = ImageTk.PhotoImage(image)

# Crear un Label para mostrar la imagen en el Frame
label = tk.Label(frame, image=photo)
label.image = photo
label.pack()

# Crear un cuadro de texto
text_widget = tk.Text(frame,font=("Times New Roman", 16), width=20, height=5, bg='light blue')
text_widget.pack()
text_widget.place(x=13, y=13)
text_widget.config(width=70, height=12)

#Agregar texto
text = "¿Cuál es la relación entre la exploración espacial y la investigación científica, y cómo han evolucionado estas áreas de conocimiento a lo largo de la historia, desde los primeros viajes al espacio hasta las misiones actuales y los planes futuros para la exploración espacial?"
text_widget.tag_configure("centered", justify="center")
text_widget.insert("1.0", text, "centered")

# Crear los botones y asignar acciones
def on_button1_click():
    response = client.submit_request(client_socket, "El botón 1 ha sido presionado")
    print(response,"Botón 1")

button1 = tk.Button(frame, text="Respuesta 1", font=("Times New Roman", 16), command=on_button1_click, bg='light blue')
button1.pack()
button1.place(x=13,y=305)
button1.config(width=31, height=5)

def on_button2_click():
    response = client.submit_request(client_socket, "El botón 2 ha sido presionado")
    print(response,"Botón 2")

button2 = tk.Button(frame, text="Respuesta 2", font=("Times New Roman", 16), command=on_button2_click,bg='light blue')
button2.pack()
button2.place(x=13,y=450)
button2.config(width=31, height=5)

def on_button3_click():
    response = client.submit_request(client_socket, "El botón 3 ha sido presionado")
    print(response,"Botón 3")

button3 = tk.Button(frame, text="Respuesta 3", font=("Times New Roman", 16), command=on_button3_click,bg='light blue')
button3.pack()
button3.place(x=406,y=305)
button3.config(width=31, height=5)

def on_button4_click():
    response = client.submit_request(client_socket, "El botón 4 ha sido presionado")
    print(response,"Botón 4")

button4 = tk.Button(frame, text="Respuesta 4", font=("Times New Roman", 16), command=on_button4_click,bg='light blue')
button4.pack()
button4.place(x=405,y=450)
button4.config(width=31, height=5)

# Ejecutar el bucle de eventos de tkinter
root.mainloop()
