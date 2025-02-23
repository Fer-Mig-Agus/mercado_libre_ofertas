'''

NO SE CUMPLIO CON LO PEDIDO

El crawler no extare nada de informacion, los archivos se crean sin que existan datos.
Leer atentamente todas las anotaciones y corregir el codigo.

Fecha para la nueva entrega: 25/02/25 a las 23:55

Si para la fecha no se concreta el proyecto,
se dara como proyecto insatisfecho y se mostrara una manera de realizar el mismo


'''












import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
Esta importacion esta de mas ya que no hace falta importar el openpyxl

'''
from openpyxl import Workbook

# URL
base_url = "https://listado.mercadolibre.com.ar/_Container_mk-pps-liquidacion-verano-2025-audio_NoIndex_True"

# Encabezados para la solicitud (para evitar bloqueos por parte del sitio web)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/133.0.0.0 Safari/537.36'}

# Lista para almacenar los datos
data = []

'''
Hacer uso del try exception en caso de ser necesario.
'''
# Función para extraer información de una página
def scrape_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all("div", class_="ui-search-result__content-wrapper")

    for item in items:
        name_product = item.find("h2", class_="ui-search-item__title").text.strip()

        seller = item.find("span", class_="ui-search-official-store-label")
        seller = seller.text.strip() if seller else "N/A"

        before_price = item.find("span", class_="price-tag-text-sr-only")
        before_price = before_price.text.strip() if before_price else "N/A"

        now_price = item.find("span", class_="price-tag-fraction").text.strip()

        discount = item.find("span", class_="ui-search-price__discount")
        discount = discount.text.strip() if discount else "N/A"

        data.append({
            "name_product": name_product,
            "seller": seller,
            "before_price": before_price,
            "now_price": now_price,
            "discount": discount
        })


# Realizar el scrapeo de las 10 páginas
for page in range(1, 11):
    # OJO
    '''
    Tener en cuenta la URL BASE para la pagina 1 es esta:
    https://listado.mercadolibre.com.ar/_Container_mk-pps-liquidacion-verano-2025-audio_NoIndex_True
    Y para las demas paginas es esta:
    https://listado.mercadolibre.com.ar/_Desde_49_Container_mk-pps-liquidacion-verano-2025-audio_NoIndex_True
    
    Aqui la forma en la que re defines la url esta mal: OJO con la estructura de la URL
    '''
    url = f"{base_url}_Desde_{(page - 1) * 50 + 1}"
    scrape_page(url)

'''
Revisar que la variable data tenga elementos para poder crear los archivos
Sino no tiene sentido crear si no hay datos
'''
# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Guardar los datos en un archivo CSV
df.to_csv('mercado_libre_scraping.csv', index=False)
print("Datos guardados en 'mercado_libre_scraping.csv'")


'''
Aqui puedes aclarar el motor para formar el archivo excel, recuerda es el openpyxl
Ejemplo:

df.to_excel('mercado_libre_scraping.xlsx', index=False, engine='openpyxl')
'''
# Guardar los datos en un archivo XLSX
df.to_excel('mercado_libre_scraping.xlsx', index=False)
print("Datos guardados en 'mercado_libre_scraping.xlsx'")


'''
Usar la estrutura de if name == main
Para no tener problemas con la ejecucion del programa


if __name__ == '__main__':
    #Ejecuto el programa

Averiguar para que sirve esto.

Leer el archivo de requirements. Corregir errores
'''


