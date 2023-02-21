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
    return [question, option_a, option_b, option_c, option_d, answer]


# Cerrar archivo
def close():
    excel_file.close()