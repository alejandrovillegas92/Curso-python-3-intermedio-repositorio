# %% [markdown]
# Web scrapping con BeautifulSoup

# %% [markdown]
# 1.Instalar e importar librerias

# %%
#pip install requests

# %%
#pip install beautifulsoup4

# %%
import requests

from bs4 import BeautifulSoup

# %% [markdown]
# 2. Enviar peticion HTTP para extraer codigo fuente de la pagina web

# %%
pagina_web = requests.get('http://books.toscrape.com/asasasas') #De esta forma hacemos la peticion a la pagina web que deseemos

print(pagina_web)#Cuando exista algun error en la pagina habra un error 404 que es not found

# %%
pagina_web = requests.get('http://books.toscrape.com/index.html') #De esta forma hacemos la peticion a la pagina web que deseemos

print(pagina_web) #Se obtendra como resultado un responde 200 que representa 'Todo esta bien' 'Fue aceptada'

soup = BeautifulSoup(pagina_web.text,'html.parser') #Creamos el objeto Soup que toma a Beutiful soup como clase, y ahora 
                                                    #Ponemos nuestra pagina web con el atributo texto y definimos un analizador que es el parser

print(soup.prettify())#con este metodo se imprime el codigo fuente a manera de texto

# %%
pagina_web2 = requests.get('http://books.toscrape.com/catalogue/category/books/fiction_10/index.html')

soup = BeautifulSoup(pagina_web2.text,'html.parser') 

print(soup.prettify())

# %%
titulo_item = soup.find('a') #Regresa la primera etiqueta o articulo con el valor asignado

print(titulo_item)

# %%
titulo_items = soup.find_all('a') #Regresa todas las etiquetas que empiecen con esa letra y lo devuelve en forma de arreglo

print(titulo_items)

# %%
titulo_items = soup.find_all('h3') #Regresa todas las etiquetas que empiecen con esa letra y lo devuelve en forma de arreglo

for item in titulo_items:
    titulo = item.a #De esta manera regresa la etiqueta a

    print(titulo)



# %%
titulo_items = soup.find_all('h3') 

for item in titulo_items:
    titulo = item.a 

    print(titulo.attrs) #Devuelve el artibuto href y el titulo, attrs significa atributo

# %%
titulos = [] #Aqui se guardan los titulos ya limpios sin el resto del codigo

titulo_items = soup.find_all('h3') 

for item in titulo_items:
    titulo = item.a
    titulos.append(titulo['title']) 

    print(titulo['title']) #Devuelve el titulo ya limpio

# %%
titulos

# %%
precio = []

precio_items = soup.find_all('p',class_="price_color")

print(precio_items)

# %%
precios = [] 

precio_items = soup.find_all('p',class_="price_color") 

for item in precio_items:
    precio = item.text
    precios.append(precio) 

    print(precios) 

# %%
precios

# %%
existencias = []

existencia_items = soup.find_all('p',class_="instock availability")

for item in existencia_items:
    existencia = item.text
    existencias.append(existencia)

    


# %%
existencias

# %%
ratings = []

rating_items =  soup.find_all('p', class_='star-rating')

print(rating_items)

# %%
ratings = []

rating_items =  soup.find_all('p', class_='star-rating')

for item in rating_items:
    rating =item['class'][1] #Este arreglo es que por cada item que exista en rating items va a devolver class o clase el primer valor o sea 1 que da el
                             #el numero de estrellas
    ratings.append(rating)




# %%
ratings

# %%
import pandas as pd 

data = {'Titulo': titulos, 
        'Precio': precio, 
        'Rating': ratings, 
        'En existencia': existencias
        }

df =pd.DataFrame(data) #Ya podemos convertir los datos en un dataframe


# %%
df

# %% [markdown]
# 2. Enviar solicitud HTTP

# %%
pagina_web = requests.get('http://books.toscrape.com/') #Esto es para hacer lapeticion a la pagina web

travel_page =  requests.get('http://books.toscrape.com/catalogue/category/books_1/index.html')

soup = BeautifulSoup(pagina_web.text, 'html.parser')

soup2 = BeautifulSoup(travel_page.text, 'html.parser')

print(soup.prettify())

# %%
imagenes_items = soup.find_all('img', class_='thumbnail')



print(imagenes_items)

# %%
images = []
images_items = soup.find_all('img', class_='thumbnail')

for item in images_items:
    image =  item['src']
    images.append(image)
print(images)

# %%
images = []
images_items = soup.find_all('img', class_='thumbnail')

for item in images_items:
    image =  item['src']
    images.append('http://books.toscrape.com/' + image) #De esta manera nos da los hipervinculos y podemos almacenar los archivos multimedia
print(images)

# %%
images

# %% [markdown]
# paginacion

# %%
import requests

from bs4 import BeautifulSoup

# %%
def obtener_contenido_pagina(url):
    reponse = requests.get(url)
    return reponse.content

# %%
def analizar_contenido_html(html):
    return BeautifulSoup(html, 'html.parser')

# %%
data = []

def procesar_pagina(soup):
    titulos = []
    ratings = []
    existencias = []
    links = []

    titulo_items = soup.find_all('h3')
    for items in titulo_items:
        titulo = items.a
        titulos.append(titulo['title'])
        links.append(titulo['href'])

    rating_items = soup.find_all('p', class_='star-rating')
    for item in rating_items:
        rating = item['class'][1]
        ratings.append(rating)
    
    existencia_items = soup.find_all('p', class_='instock availability')
    for item in existencia_items:
        existencia =  item.text.strip()
        existencias.append(existencia)
    
    for i in range(len(titulos)):
        data.append({
            "titulo":titulos[i],
            "Rating":ratings[i],
            "Existencia":existencias[i]
        })

    

# %%
def manejar_paginacion(url_base, num_paginas):
    for i in range(1, num_paginas + 1):
        url =  url_base + '/page-' + str(i) + '.html'
        contenido_pagina = obtener_contenido_pagina(url)
        soup = analizar_contenido_html(contenido_pagina)
        procesar_pagina(soup)

# %%
url_base = 'http://books.toscrape.com/catalogue/'

num_paginas = 50

manejar_paginacion(url_base, num_paginas)

# %%
data

# %%
len(data)

# %%
import pandas as pd

df = pd.DataFrame(data)

# %%
df

# %% [markdown]
# Expresiones regulares

# %%
html = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(html.text, 'html.parser')

# %%
import re

# %%
item = soup.select_one('li.current')

patron = r'Page (\d+) of (\d+)'

match = re.search(patron, html.text)

print(match)

if match:
    page_number = int(match.group(1))
    total_pages = int(match.group(2))
    print(page_number, total_pages)

# %%
import re

patron = r'.*+[aeiou]?{n}(ab)+^$\d'


# %%
import re

texto = 'Hola, mi numero de telefono es 614-189-6685. Necesitas contactarme? Llamame'

patron = r'\d{3}-\d{3}-\d{4}'

resultado_search = re.search(patron, texto)

if resultado_search:
    print('Numero de telefono encontrado',resultado_search.group())
else:
    print('Numero de telefono no encontrado')

# %% [markdown]
# Ejercicio cyberpuerta
# 1. Entrar  a la pagina cyberpuerta  y buscar una categoria
# 2. Realizar las peticiones HTTP pertinentes para obtener  el codigo fuente  de la pagina
# 3. Analizar las paginas web  para identificar los elementos relevantes
# 4. Extraer los elementos relevantes  de las paginas web
# 5. Generar un dataframe con los datos obtenidos
# 6. Generar una grafica para visualizar datos

# %%
import requests

from bs4 import BeautifulSoup

# %%
pagina_web = requests.get('https://www.cyberpuerta.mx/Computadoras/Laptops/') #Solo manejar un tipo de pagina no la travel page


soup = BeautifulSoup(pagina_web.text, 'html.parser')


print(soup.prettify())

# %%
def obtener_contenido_pagina(pagina_web):
    reponse = requests.get(pagina_web)
    return reponse.content

# %%
def analizar_contenido_html(pagina_web):
    return BeautifulSoup(pagina_web, 'html.parser')

# %%
data = []

def procesar_pagina(soup, data):
    productos = []
    precios =[]
    ratings = []
    existencias = []
    links = []
     
    producto_items = soup.find_all('div', class_='emproduct_right')
    for items in producto_items:
        producto = items.a.text.strip()
        productos.append(producto)
               
    rating_items = soup.find_all('div', class_='cpreviews_stars_box clear')
    for item in rating_items:
        rating = item.find('div', class_='cpreviews_stars_box_percent')['style']
        stars = int(rating.strip("width: ;%"))
        stars //=  20
        ratings.append(stars)
    
    precio_items = soup.find_all('label', class_='price')
    for item in precio_items:
        precio = item.get_text(strip=True)
        precios.append(precio)
    
    existencia_items = soup.find_all('div', class_='emstock')
    for item in existencia_items:
        existencia = item.get_text(strip=True)
        existencias.append(existencia)
    
    link_items = soup.find('div', class_='emproduct_right').find_all('a')
    for item in link_items:
        links.append(item['href'])

    min_lenght = min(len(productos), len(ratings), len(precios), len(existencias), len(links))

    for i in range(min_lenght):
        data.append({
            "Producto":productos[i] if i < len(productos) else None,
            "Rating":ratings[i] if i < len(ratings) else None,
            'Precio':precios[i] if i < len(precios) else None,
            "Existencia":existencias[i] if i < len(existencias) else None,
            'Enlaces': links[i] if i < len(links) else None
        })

# %%
url_base = 'https://www.cyberpuerta.mx/Computadoras/Laptops/' #Deben ser 1088 productos

num_paginas = 69


# %%
def manejar_paginacion(url_base, num_paginas):
    for i in range(1, num_paginas + 1):
        url =  url_base + str(i) + '/'
        contenido_pagina = obtener_contenido_pagina(url)
        soup = analizar_contenido_html(contenido_pagina)
        procesar_pagina(soup, data)

manejar_paginacion(url_base, num_paginas)

# %%
data

# %%
print(len(data))

# %%
import pandas as pd

df =  pd.DataFrame(data)

df

# %%
import datetime

fecha_actual = datetime.datetime.now().strftime('%d-%m-%Y')

df.to_csv(f'./WebScrapping/Cyberpuerta-WebScrap-{fecha_actual}.csv', index=False)


