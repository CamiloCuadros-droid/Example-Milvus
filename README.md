Demostración de búsqueda vectorial con Milvus Lite y Python
1. Descripción del proyecto

Este proyecto implementa una demostración de una base de datos vectorial utilizando Milvus Lite y Python.

El objetivo es almacenar vectores numéricos asociados a textos descriptivos y realizar búsquedas por similitud utilizando la métrica de distancia Coseno.

La aplicación permite:

Crear una base de datos vectorial local.
Crear una colección de vectores de cuatro dimensiones.
Insertar registros con identificadores, vectores y textos.
Realizar búsquedas por similitud.
Obtener los dos resultados más cercanos al vector de consulta.
Visualizar los resultados en la terminal.

Milvus Lite permite trabajar con bases de datos vectoriales localmente sin necesidad de configurar un servidor independiente.

2. Tecnologías utilizadas
Tecnología	Descripción
Python 3.10 o superior	Lenguaje de programación
Milvus Lite	Base de datos vectorial local
PyMilvus	SDK de Python para interactuar con Milvus
Bash	Terminal para ejecutar los comandos
3. Requisitos previos

Antes de comenzar, es necesario tener instalado:

Python 3.10 o superior.
Pip, administrador de paquetes de Python.
Git (opcional, para clonar el repositorio).
Una terminal Bash o PowerShell.
3.1. Instalación de Python

Descargar Python desde su página oficial:

https://www.python.org/downloads/

Seleccionar la versión correspondiente al sistema operativo.

Windows:

Descargar el instalador de Python.
Ejecutar el instalador.
Marcar la opción Add Python to PATH.
Finalizar la instalación.

Verificar que Python se encuentre instalado:

bash
python --version


En caso de que el comando anterior no funcione, utilizar:

bash
py --version


Linux:

Actualizar los repositorios:

bash
sudo apt update


Instalar Python, pip y el módulo para crear entornos virtuales:

bash
sudo apt install python3 python3-pip python3-venv


Verificar la instalación:

bash
python3 --version


macOS:

Descargar Python desde:

https://www.python.org/downloads/macos/

Verificar la instalación:

bash
python3 --version

4. Descargar el proyecto

Si el proyecto se encuentra alojado en GitHub, ejecutar:

bash
git clone URL_DEL_REPOSITORIO


Ingresar a la carpeta del proyecto:

bash
cd NOMBRE_DEL_REPOSITORIO


Si se descargó el proyecto como archivo ZIP, descomprimirlo y abrir una terminal en la carpeta correspondiente.

5. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

Crear el entorno virtual:

Windows:

bash
py -m venv .venv


Linux y macOS:

bash
python3 -m venv .venv

5.1. Activar el entorno virtual

Windows - PowerShell:

powershell
.venv\Scripts\Activate.ps1


Windows - CMD:

cmd
.venv\Scripts\activate.bat


Linux y macOS - Bash:

bash
source .venv/bin/activate


Una vez activado, aparecerá (.venv) al inicio de la línea de comandos.

6. Instalar Milvus Lite y PyMilvus

Con el entorno virtual activado, actualizar pip:

bash
python -m pip install --upgrade pip


Instalar las dependencias necesarias:

bash
python -m pip install "pymilvus[milvus-lite]"


En Windows, si la instalación no incluye correctamente el paquete de Milvus Lite, instalarlo explícitamente:

bash
python -m pip install milvus-lite


Verificar que PyMilvus se encuentre instalado:

bash
python -c "from pymilvus import MilvusClient; print('PyMilvus instalado correctamente')"


Con esto, el entorno estará preparado para ejecutar la aplicación.

7. Estructura del proyecto

La organización recomendada del repositorio es la siguiente:

text
milvus-lite-demo/
│
├── .venv/
│
├── main.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md


Descripción de los archivos:

main.py: contiene la implementación de la demostración de búsqueda vectorial.
requirements.txt: registra las dependencias necesarias.
.gitignore: evita subir archivos innecesarios al repositorio.
README.md: contiene la documentación del proyecto.
.venv/: almacena el entorno virtual de Python y no debe subirse a GitHub.
8. Configurar las dependencias

Para registrar las dependencias instaladas:

bash
python -m pip freeze > requirements.txt


Esto genera un archivo con las versiones de los paquetes instalados.

Para instalar las dependencias posteriormente en otro equipo:

bash
python -m pip install -r requirements.txt

9. Ejecutar el proyecto

Una vez instaladas las dependencias y activado el entorno virtual, verificar que el archivo main.py se encuentre en la carpeta principal.

Ejecutar la aplicación mediante:

bash
python main.py


En Linux y macOS también se puede utilizar:

bash
python3 main.py

9.1. ¿Qué sucede durante la ejecución?

La aplicación realiza cinco operaciones principales:

1. Conexión con Milvus Lite

Se establece una conexión con una base de datos local mediante:

python
client = MilvusClient("./milvus_demo.db")


Si la ubicación todavía no contiene una base de datos, Milvus Lite crea el almacenamiento local.

2. Creación de la colección

Se crea una colección llamada demo_sentences, configurada para almacenar vectores de cuatro dimensiones y utilizar la métrica Coseno.

3. Inserción de registros

Se insertan cuatro registros de prueba relacionados con dos temáticas:

Deportes: textos relacionados con el fútbol.
Programación: textos relacionados con Python, Node.js y React.

Cada registro contiene un identificador, un vector numérico y un texto descriptivo.

4. Búsqueda por similitud

Se proporciona un vector de consulta:

python
query_vector = [0.12, 0.22, 0.31, 0.42]


Milvus compara este vector con los almacenados y devuelve los dos resultados más cercanos utilizando:

python
results = client.search(
    collection_name=collection_name,
    data=[query_vector],
    limit=2,
    output_fields=["text"]
)


5. Visualización de resultados

Finalmente, se muestran en la terminal:

Identificador del registro.
Distancia de Coseno.
Texto asociado al vector.
10. Resultado esperado

Al ejecutar el programa correctamente, se visualizará una salida similar a la siguiente:

text
=== Iniciando Demostración de Milvus Lite ===

Colección 'demo_sentences' creada exitosamente.

Datos insertados correctamente en Milvus.

Ejecutando búsqueda por similitud en Milvus...

--- Resultados de la Búsqueda ---

ID: 1 | Distancia de Coseno: ... | Texto: El fútbol es un deporte apasionante.

ID: 2 | Distancia de Coseno: ... | Texto: Me encanta jugar partidos de fútbol con amigos.


Nota: Los valores exactos de distancia y el orden de los resultados dependen de los vectores almacenados y de la implementación utilizada.

11. Archivos generados

Durante la ejecución se crea el almacenamiento local:

text
milvus_demo.db


Este almacenamiento contiene la información persistente de Milvus Lite.

No es necesario crear manualmente la base de datos ni iniciar un servicio adicional.

Importante: El programa elimina la colección demo_sentences si ya existe antes de crearla nuevamente. Por esta razón, cada ejecución comienza con una colección limpia y los registros anteriores de esa colección se pierden.

12. Solución de problemas
Error: No module named 'pymilvus'

Significa que PyMilvus no está instalado en el entorno activo.

Solución:

bash
python -m pip install "pymilvus[milvus-lite]"

Error: No module named 'milvus_lite' o problemas al iniciar Milvus Lite

Instalar explícitamente el paquete:

bash
python -m pip install milvus-lite

Error al activar el entorno virtual en Windows

Si PowerShell bloquea la ejecución del script de activación, se puede utilizar CMD:

cmd
.venv\Scripts\activate.bat

Error: No se reconoce el comando Python

Verificar la instalación de Python y su configuración en la variable PATH.

En Windows intentar:

bash
py --version


En Linux y macOS intentar:

bash
python3 --version

Error al instalar dependencias

Actualizar pip:

bash
python -m pip install --upgrade pip


Verificar que se esté utilizando Python 3.10 o superior y que las dependencias tengan versiones compatibles con el sistema operativo.

13. Consideraciones técnicas
La colección utiliza vectores de cuatro dimensiones.
La métrica de búsqueda configurada es COSINE.
La búsqueda devuelve un máximo de dos resultados.
Los datos se almacenan localmente.
Milvus Lite no requiere Docker para esta demostración.
Los vectores utilizados son datos numéricos de prueba y no embeddings generados mediante un modelo de inteligencia artificial.

Por lo tanto, esta demostración permite comprender el funcionamiento de una búsqueda vectorial, pero no representa todavía una búsqueda semántica real sobre textos.

Para implementar una búsqueda semántica sería necesario generar embeddings mediante un modelo de lenguaje o de representación vectorial.

14. Autores

Proyecto académico de demostración de bases de datos vectoriales con Python y Milvus Lite.

15. Referencias
Documentación oficial de Python: https://www.python.org/doc/
Documentación oficial de Milvus Lite: https://milvus.io/docs/milvus_lite.md
Documentación de PyMilvus: https://milvus.io/docs/install-pymilvus.md
Repositorio oficial de Milvus: https://github.com/milvus-io/milvus

Fin de la documentación.
