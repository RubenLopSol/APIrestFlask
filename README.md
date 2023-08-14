# APIrestFlask

Ejercicio de creacion de una APIrest con Python usando Flask

## Descripción

Este proyecto consiste en la implementación de una API RESTful en Python utilizando el framework Flask. La API proporciona información sobre tasas de cambio de moneda y transacciones financieras.

La API permite a los usuarios consultar tasas de cambio entre diferentes monedas, así como acceder a detalles específicos de las transacciones realizadas en diferentes monedas y SKU (Unidad de Mantenimiento de Existencias).

Utilizando una estructura modular y siguiendo los principios de orientación a objetos y SOLID, este proyecto busca brindar una solución flexible y escalable para gestionar transacciones y tasas de cambio en un entorno financiero.

La implementación incluye un sistema de conversión de moneda que puede manejar conversiones directas e indirectas a través de monedas intermedias. Además, se ha prestado atención al manejo de errores y a la creación de una interfaz de usuario intuitiva a través de los endpoints API.

## Instalación

1. Clona este repositorio.
2. Crea un entorno virtual: `python3 -m venv venv`.
3. Activa el entorno virtual: `source venv/bin/activate` (en Unix/Linux) o `venv\Scripts\activate` (en Windows).
4. Instala las dependencias: `pip install -r requirements.txt`.

## Uso

1. Ejecuta la aplicación: `python app.py`.
2. Accede a la API en tu navegador o herramienta de API testing (por ejemplo, Postman o thunderclient(VScode)).
3. Consulta los endpoints y sus respuestas.

## Endpoints

- `/currency_rates`: Devuelve todas las tasas de cambio disponibles.
- `/currency_rates/<currency>`: Devuelve la tasa de cambio para la moneda especificada.
- `/transactions/<currency>`: Devuelve todas las transacciones en la moneda especificada.
- `/transactions/<sku>/<currency>`: Devuelve las transacciones para un SKU y una moneda especificados.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tu función/fix: `git checkout -b nombre-de-rama`.
3. Realiza tus cambios y realiza commits: `git commit -m "Descripción del cambio"`.
4. Haz push a la rama: `git push origin nombre-de-rama`.
5. Crea un Pull Request en GitHub.