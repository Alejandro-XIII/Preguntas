import tkinter as tk
from tkinter import *
from tkinter import simpledialog
import client
from PIL import ImageTk, Image

puntaje = 0

# Actualizar los datos de la ventana
def refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,punto,answer_Text):
    global puntaje
    if punto == 0:
        puntaje = 0
    else:    
        puntaje += punto

    #Agregar texto de pregunta
    text_widget.config(state="normal")
    text_widget.delete(1.0, END)
    text_widget.tag_configure("centered", justify="center")
    text = answer_Text + "\n \n Puntaje: " + str(puntaje) + "\n \n" + data_list[0]
    text_widget.insert("1.0", text, "centered")
    text_widget.config(state="disabled")

    #Agregar texto de puntaje
    text_score.config(state="normal")
    text_score.delete(1.0, END)
    text = "\t             Historial \n \n"
    for i in range(1,11):
        text = text + str(i) + ". " + data_list[i+5+(i-1)] + "\t" + data_list[i+6+(i-1)] + "\n"
    text_score.insert('1.0', text.strip("\n"))
    text_score.config(state="disabled")

    #Agregar texto a los botones
    button1.config(text=data_list[1])
    button2.config(text=data_list[2])
    button3.config(text=data_list[3])
    button4.config(text=data_list[4])

# Inicializar el socket del cliente 
client_socket = client.start_client()

# Pedir datos del juego
data_list = client.submit_request(client_socket, " pidiendo pregunta").split('\n')

# Crear la ventana raíz
root = tk.Tk()
root.withdraw()
name = simpledialog.askstring("Nombre", "Por favor, escriba su nombre:")
root.deiconify()

# Asignar un título a la ventana
root.title("Questions")

# Configurar el tamaño de la ventana
root.geometry("800x600")

# Deshabilitar la opción de maximizar la ventana
root.resizable(False, False)

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
image = Image.open("assets/mi_imagen.png")
photo = ImageTk.PhotoImage(image)

# Crear un Label para mostrar la imagen en el Frame
label = tk.Label(frame, image=photo)
label.image = photo
label.pack()

# Crear un cuadro de texto para las preguntas
text_widget = tk.Text(frame,font=("Times New Roman", 16), bg='white')
text_widget.pack()
text_widget.place(x=14, y=13)
text_widget.config(width=34, height=12)

# Crear un cuadro de texto para el puntaje
text_score = tk.Text(frame,font=("Times New Roman", 16), bg='white')
text_score.pack()
text_score.place(x=407, y=13)
text_score.config(width=34, height=12)

# Crear los botones y asignar acciones
def on_button1_click():
    # Verifica la opción correcta
    global data_list
    answer = data_list[5]
    if answer == data_list[1]:  
        data_list = client.submit_request(client_socket, " pidiendo pregunta").split('\n')      
        refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,1,"¡CORRECTO!")
    else:
        data_list = client.submit_request(client_socket, name +"\n"+str(puntaje)).split('\n') 
        refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,0,"Perdiste era: " + answer) 
    
button1 = tk.Button(frame, font=("Times New Roman", 16), command=on_button1_click, bg='light blue')
button1.pack()
button1.place(x=13,y=305)
button1.config(width=31, height=5)

def on_button2_click():
    # Verifica la opción correcta
    global data_list
    answer = data_list[5]
    if answer == data_list[2]:  
        data_list = client.submit_request(client_socket, " pidiendo pregunta").split('\n')    
        refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,1,"¡CORRECTO!")
    else:
        data_list = client.submit_request(client_socket, name +"\n"+str(puntaje)).split('\n') 
        refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,0,"Perdiste era: " + answer) 

button2 = tk.Button(frame, font=("Times New Roman", 16), command=on_button2_click,bg='light blue')
button2.pack()
button2.place(x=13,y=450)
button2.config(width=31, height=5)

def on_button3_click():
    # Verifica la opción correcta
    global data_list
    answer = data_list[5]
    if answer == data_list[3]:   
        data_list = client.submit_request(client_socket, " pidiendo pregunta").split('\n')   
        refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,1,"¡CORRECTO!")
    else:
        data_list = client.submit_request(client_socket, name +"\n"+str(puntaje)).split('\n') 
        refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,0,"Perdiste era: " + answer) 

button3 = tk.Button(frame, font=("Times New Roman", 16), command=on_button3_click,bg='light blue')
button3.pack()
button3.place(x=406,y=305)
button3.config(width=31, height=5)

def on_button4_click():
    # Verifica la opción correcta
    global data_list
    answer = data_list[5]
    if answer == data_list[4]:    
        data_list = client.submit_request(client_socket, " pidiendo pregunta").split('\n')  
        refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,1,"¡CORRECTO!")
    else:
        data_list = client.submit_request(client_socket, name +"\n"+str(puntaje)).split('\n')
        refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,0,"Perdiste era: " + answer)  

button4 = tk.Button(frame, font=("Times New Roman", 16), command=on_button4_click,bg='light blue')
button4.pack()
button4.place(x=405,y=450)
button4.config(width=31, height=5)

refresh_data(data_list,text_widget,text_score,button1,button2,button3,button4,0," ")

# Ejecutar el bucle de eventos de tkinter
root.mainloop()