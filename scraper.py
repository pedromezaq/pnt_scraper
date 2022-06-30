from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.common.by import By
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Algunas notas de mejoras.
# Se puede implementar que haga clic hasta que esté disponible el elemento, pero para no batallar por ahora solo
# agregaré estos frenos de tiempo para probar el código.


# Opciones para el driver de Chrome. Aquí se incluye la opción para que abra Chrome en el puerto 9222.
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
# Chrome driver lo metí a la carpeta del proyecto.
chrome_driver = "./chromedriver"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
# Abrir Chrome con la siguiente opción (no implemento en el código porque abriría cada vez que quiero correrlo
# ahorita que estoy escribiendo el código).
# Desde la terminal en Linux: google-chrome --remote-debugging-port=9222

# Preguntara filename, start page y end page y número de resultados por página.
print("Recuerda elegir manualmente el filtro. Se puede encontrar una lista de sujetos obligados en el archivo filter.csv.")
print("Introducir el nombre del archivo al cual vamos a guardar los datos, la página de inicio y la página final.")
filename = input('Filename (no extension needed, but recommend adding .txt to the input): ')
start_page = int(input('Start page: '))
end_page = input('End page: ')
end_page = int(end_page) + int(1)
results_per_page = input('Número de resultados por página: ')
count = (int(start_page)-int(1))*int(results_per_page)
# if os.path.exists(filename):
#     os.remove(filename)
#     print("The file has been deleted successfully")
# else:
#     print("The file does not exist!")
# De la última count, se divide entre 100 y se resta 1.

# page_inicial = count/100+1
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
# for i in range(0,221):
#     print(i+1)
#     time.sleep(0.5)
#     button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="paginate_button next"]')))
#     button.click()
#     #driver.find_element(By.XPATH, '//a[@class="paginate_button next"]').click()
# # Abrir archivo.

with open(filename, 'a') as file:
    # Establecer rango de páginas.
    for page in range(start_page,end_page):
        next_page = page+1
        driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
        time.sleep(15)
        for odd_even in ['odd','even']:
            path = """//tr[@class="cursor-pointer """ + odd_even + """"]"""
            # Esperar que la fila esté disponible (para cuando vuelva a cargar la página siguiente).
            time.sleep(0.5)
            for row in driver.find_elements(By.XPATH, path):
                # Esperar que la fila esté disponible (para cuando cierre el diálogo y continue al siguiente elemento.
                time.sleep(0.5)
                count = count + int(1)
                print(count)
                # Columna de # de observación, para referencia.
                text_in_row = str(count)
                for name in row.find_elements(By.XPATH,'.//td'):
                    text_in_row= text_in_row+'|'+name.text
                row.click()
                # Son 8 columnas, que se tienen que pegar a la misma fila de text_in_row.
                # Esperar a que aparezca la tabla.-
                time.sleep(0.5)
                for presupuesto in driver.find_elements(By.XPATH, '//td[@class="columnaDesglosePresupuesto"]'):
                    text_in_row = text_in_row +'|'+presupuesto.text
                # Cerrar diálogo.
                driver.find_element(By.XPATH, '//i[@class="fa fa-times no-print"]').click()
                text_in_row = text_in_row + '\n'
                writer = file.writelines(text_in_row)

        # Esperar a que el botón de siguiente esté disponible.
        time.sleep(1)
        for buttons in driver.find_elements(By.XPATH, '//a[@class="paginate_button "]'):
            #print(buttons.text)
            if buttons.text == str(next_page):
                buttons.click()
                print("Vámonos a la página " + str(next_page))
            else:
                print("")
