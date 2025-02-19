# Scraping a Mercado Libre

## Tarea

Se desea realizar un scraping a la siguiente url:

`https://listado.mercadolibre.com.ar/_Container_mk-pps-liquidacion-verano-2025-audio_NoIndex_True`

Se desea extraer la informacion de todos los productos de la misma, se necesita:

* Nombre del producto _(name_product)_
* Vendedor (si existe) _(seller)_
* Precio anterior (si existe) _(before_price)_
* Precio actual _(now_price)_
* Descuento (si existe) _(dicount)_

Se debe realizar el scrapeo de las 10 paginas (paginacion en la base de la pagina, **Mirar bien la URL**) Toda la informacion debe de ser almacenada en un archivo `csv` y `xlsx` (averiguar sobre la libreria pandas y openpyxl) realizar esta tarea haciendo uso de las librerias requests y Beautiful soup, obviamente se pueden agregar mas librerias, las que se requiera para el proyecto.

## Estructura del proyecto

* .gitignore
* .env (de ser necesario)
* .env.example (si existe el .env)
* requirements.txt
* main.py

Aclaracion: **Los archivos cvs y excel no se deben de subir a github**

## Aspectos a tener en cuenta
Se debe de crear un entorno virtual, tambien se debera de realizar un pullrequests a la rama dev.
