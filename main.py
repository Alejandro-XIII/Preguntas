import tkinter as tk
import client
import pandas as pd
import xlrd
import openpyxl


#abrimos el archivo de excel que posee las preguntas
preguntas ="Questions.xlsx"
def leer_celda(filename, column, row): #funcion para leer una sola celda en especifico
    return pd.read_excel(filename, skiprows=row - 1, usecols=column, nrows=1, header=None, names=["Value"]).iloc[0]["Value"]
print(leer_celda(preguntas,"A",1))


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
window_width = 600
window_height = 580
x_coord = (screen_width / 2) - (window_width / 2)
y_coord = (screen_height / 2) - (window_height / 2)
root.geometry("{}x{}+{}+{}".format(window_width, window_height, int(x_coord), int(y_coord)))

frame = tk.Frame(root, width=600, height=580, bg="red")
frame.pack()
frame.place(x=0, y=0)



# Crear los cuadros de texto
label = tk.Label(frame, text=(leer_celda(preguntas,"A",1)))
questionA = tk.Label(frame)
label.pack()
label.place(x=100, y=100)



# Crear los botones y asignar acciones
def on_button1_click():
    response = client.submit_request(client_socket, "El botón 1 ha sido presionado")
    print(response,"Botón 1")


button1 = tk.Button(frame, text="Botón 1", command=on_button1_click)
button1.pack()
button1.place(x=250,y=200)

def on_button2_click():
    response = client.submit_request(client_socket, "El botón 2 ha sido presionado")
    print(response,"Botón 2")

button2 = tk.Button(frame, text="Botón 2", command=on_button2_click)
button2.pack()
button2.place(x=250,y=250)

def on_button3_click():
    response = client.submit_request(client_socket, "El botón 3 ha sido presionado")
    print(response,"Botón 3")

button3 = tk.Button(frame, text="Botón 3", command=on_button3_click)
button3.pack()
button3.place(x=110,y=350)

def on_button4_click():
    response = client.submit_request(client_socket, "El botón 4 ha sido presionado")
    print(response,"Botón 4")

button4 = tk.Button(frame, text="Botón 4", command=on_button4_click)
button4.pack()
button4.place(x=390,y=350)

# Ejecutar el bucle de eventos de tkinter
root.mainloop()
