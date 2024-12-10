# Cálculo del Índice de Precios al Consumidor para la División Prendas de Vestir y Calzado Utilizando Datos de la Web

![image](https://github.com/user-attachments/assets/ed23b8f0-0d3f-4036-b46e-b36e55bba972)

## Proyecto PEUCD 2024-INEI

### Asesor:
Stanislao Maldonado

### Integrantes:
- Roberto Carlo Mera Altamirano
- Ariana Jasmin Tapia Herrera
- Danna Coello Huamani
- José Ayarquispe Mamani
- César Jesús Chinchay Guardia
- Erika Camila Ramos Méndez

## Descripción

Este proyecto tiene como objetivo la construcción del Índice de Precios al Consumidor (IPC) de Lima Metropolitana utilizando la técnica de web scraping para recolectar datos de tiendas de comercio electrónico, especialmente en la división de prendas de vestir y calzado. La metodología propuesta busca crear un sistema complementario ágil, preciso y actualizado, que aproveche las herramientas tecnológicas disponibles para la extracción automatizada de datos de páginas web de tiendas de departamento multicanal.

## Metodología

### Selección de Fuentes de Datos

Se seleccionaron tiendas de departamento que cuentan con presencia tanto en tiendas físicas como en plataformas en línea, y que ofrecen una amplia gama de productos en la categoría de vestuario y calzado. Estas tiendas son:

- **Saga Falabella**
- **Ripley**
- **Oechsle**

### Configuración y Desarrollo del Sistema de Web Scraping

El sistema de web scraping fue desarrollado utilizando el lenguaje de programación Python, aprovechando librerías como:

- **BeautifulSoup**: Para parsear el contenido HTML de las páginas.
- **Selenium**: Para extraer datos de sitios dinámicos que cargan contenido mediante JavaScript.
- **Pandas**: Para la organización y almacenamiento de los datos extraídos.
- **Requests**: Para hacer las solicitudes HTTP a las páginas web.

El sistema navega automáticamente por las categorías de productos, extrayendo precios, nombres, marcas, y otras características relevantes de los productos. Los datos obtenidos son almacenados en un archivo CSV para su posterior análisis.

### Unificación y Limpieza de Datos

Después de la extracción de los datos, se llevó a cabo un proceso de unificación y limpieza utilizando **Pandas**. Esto incluyó:

- **Estandarización de texto**: Conversión de texto a minúsculas y eliminación de duplicados.
- **Filtrado de valores nulos y ceros**: Eliminación de productos sin marca o con precios igual a cero.
- **Corrección de texto**: Reemplazo de guiones por espacios y eliminación de palabras irrelevantes como colores y tallas.
- **Formateo de la columna de Precio**: Conversión de precios a un formato numérico válido.

### Estructuración y Almacenamiento de los Datos

Los datos extraídos fueron organizados en un **DataFrame** utilizando **Pandas**, y posteriormente almacenados en un archivo CSV con las siguientes columnas:

- **Item**
- **Marca**
- **Precio**
- **Categoría**
- **Género**
- **Web**
- **Fecha**

### Clasificación de los Productos

La clasificación de los productos se realizó según el **CCIF** (Clasificación Central de Información de los Productos). Debido a las limitaciones en el nivel de detalle de los datos extraídos, se optó por clasificar los productos a nivel de "producto" en lugar de "variedad específica". Esta clasificación fue realizada manualmente sobre una muestra de 5,794 productos.

### Análisis y Predicción

Para mejorar la clasificación, se utilizaron técnicas de **embeddings** mediante **FastText**, lo que permitió generar representaciones vectoriales de las palabras y mejorar la clasificación semántica. Posteriormente, se entrenó un modelo de **SVM** (Support Vector Machine) para la clasificación de los productos en las categorías del **CCIF**.

El modelo fue evaluado utilizando datos extraídos en fechas específicas (26 de noviembre y 5 de diciembre) y se asignaron las predicciones de clase a los productos. Estos resultados fueron fundamentales para el cálculo del IPC.

## Herramientas Utilizadas

- **Python**
- **BeautifulSoup**
- **Selenium**
- **Pandas**
- **Requests**

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.
