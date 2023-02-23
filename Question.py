import openpyxl
import random

# Abre el archivo .xlsx
excel_file = openpyxl.load_workbook('assets/Questions.xlsx')

# Selecciona la hoja de trabajo en la que se trabajará
worksheet = excel_file.active

# Lee los datos del archivo y retorna una pregunta con sus datos
def generate_question():
    max_row = worksheet.max_row
    row = random.randint(1, max_row)
    question = worksheet['A'+str(row)].value
    option_a = worksheet['B'+str(row)].value
    option_b = worksheet['C'+str(row)].value
    option_c = worksheet['D'+str(row)].value
    option_d = worksheet['E'+str(row)].value
    answer = worksheet['F'+str(row)].value

    data_list = [question, option_a, option_b, option_c, option_d, answer]
    for i in range(1,11):
        data_list.append(worksheet['G'+str(i)].value)
        data_list.append(str(worksheet['H'+str(i)].value))
    return data_list

# Actualizar la tabla de puntajes
def update_score(new_data):
    list_score = []
    for i in range(1,11):
        list_score.append((worksheet['G'+str(i)].value,worksheet['H'+str(i)].value))
    
    # Comparamos el nuevo puntaje con el puntaje más pequeño de la lista
    if new_data[1] > list_score[-1][1]:
        list_score = sorted(list_score[:-1] + [new_data], key=lambda x: x[1], reverse=True)

    # Escribir los datos en el archivo
    for i in range(1,11):
        worksheet['G'+str(i)] = list_score[i-1][0]
        worksheet['H'+str(i)] = list_score[i-1][1]
    
    # Guardar el libro
    excel_file.save('assets/Questions.xlsx')

# Cerrar archivo
def close():
    excel_file.close()