# Prueba técnica Web Factorial

En este proyecto se ha llevado a cabo un proceso completo de aseguramiento de la calidad (QA) sobre la funcionalidad principal de la web: https://qainterview.pythonanywhere.com/
El proyecto lo he realizado de manera individual siguiendo metodología ágil Scrum y BDD para el diseño de las pruebas antes del desarrollo, siguiendo buenas prácticas de testing.

## Plan de Pruebas, resultados y reporte de errores: [Ver Plan de Pruebas y Reporte de Errores](https://github.com/CrisMendezQA/factorial/blob/main/Plan%20de%20Pruebas%20-%20Web%20Factorial.pdf)
En este documento se detalla el plan de pruebas, las funcionalidades probadas, el resultado de las pruebas ejecutadas y el reporte de errores.


## Automatización E2E - Tecnologías

- ![Python](https://img.shields.io/badge/Python-3.12%2B-blue)  
- ![Playwright](https://img.shields.io/badge/Playwright-v1.48-green)

## Resultados de las pruebas automatizadas

Se ha configurado un flujo de integración continua con github actions que ejecuta las pruebas después de cada cambio y una vez a la semana al final de cada sprint. Puede consultar en este enlace el resultado de la ultima ejecucion de pruebas y descargar el reporte de los resultados de las pruebas:


## Requisitos del Proyecto

### Python 3.12

Descarga e instala Python versión 3.12 desde su web oficial (https://www.python.org/downloads/)
Asegurate que Python se añade al PATH durante la instalación.


### Instalar Dependencias

Una vez instalado Python:

Clona este repositorio.

Accede a la carpeta del proyecto.

Ejecuta en la terminal:

``
pip install -r requirements.txt
``

``
playwright install
``


### Ejecutar los tests en local
Accede a la carpeta del proyecto.

Ejecuta en la terminal:

`pytest --headed`

# Pruebas de API con POSTMAN
Se han probado casos positivos y negativos del método POST de la API.
[Proyecto](https://crismendezqa-7270320.postman.co/workspace/API-FACTORIAL~60a350da-056a-4672-96d4-77cc99ca7795/collection/55034639-35c77add-2243-4167-8b1c-9e4ecaafd155?action=share&creator=55034639&active-environment=55034639-73123500-2c81-4174-9bd2-cf225d9cc2c3)

# Reporte de errores de la API
Cuando se envía un valor inválido a la API (número negativo, texto o valor decimal) devuelve un código 500 y debería devolver un código controlado de 400 o similar.
