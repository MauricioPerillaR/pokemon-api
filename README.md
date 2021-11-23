# Extension PokeAPI

_Este proyecto consiste en obtener y guardar localmente la cadena de evoluciones de un pokemon junto con sus características haciendo uso del comando personalizado evolution_chain hecho en Django. Podrá consultar las carácterísitcas y evoluciones de un Pokemon consunmiendo la API_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

Tener instalado Pipenv para instalar las dependencias del proyecto

### Instalación 🔧

1) Clona el proyecto
  ```
  git clone https://github.com/MauricioPerillaR/pokemon-api.git
  ```
2) En la raíz del respositorio encontrará el archivo Pipfile, ejecute el siguiente comando en la ubicación del archivo Pipfile para instalar las dependencias del proyecto
  ```
  > ls
  Pipfile Pifile.lock pokemon
  > pipenv install
  ```
3) Si se ha generado algún error en este paso, puede escribirnos un ticket.


## Ejecutando las pruebas ⚙️

_Guardado de pokemones en la base de datos local y consulta de pokemones en la DB por medio de la API_

### Obtener y salvar una cadena de evolución 🔩

_Dentro de la carpeta pokemon encontrar el archivo manage.py, use este archivo para ejecutar el comando para obtener y salvar una cadena de evolución por id_

```
py manage.py evolution_chain <id>
py manage.py evolution_chain 10
```
En el ejemplo anterior obtendremos la cadena de evolución de Pikachu.

### API - Obtener caraterísticas de un Pokemon 🔩

_Para hacer usa de la API debera correr el servicio, una vez echo esto use un cliente para consumir el servicio, puede hacerlos desde un navegador_

Iniciar Servicio:
```
py manage.py runserver
```

Obtener caraterísticas y evoluciones de un pokemon por nombre --> URL "host:port/api/v1/pokemon/<pokemon_name>"
```
http://localhost:8000/api/v1/pokemon/raichu
```


## Construido con 🛠️

* [Django](https://www.djangoproject.com/) - El framework web usado
* [Pypev](https://pipenv-es.readthedocs.io/es/latest/) - Manejador de dependencias
* [Python](https://www.python.org/) - Lenguaje de programación base

## Autores ✒️

_Mauricio Perilla Rodriguez_

