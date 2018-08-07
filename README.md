# ProyectoBI_2018A
Grupo 05


Integrantes: Macas Alexandra
             Giler Mario
             
**TEMA: Diseño e Implementación de un modelo de clasificación de sentimientos utilizando 
machine learning** 


**Objetivo**

El objetivo de este proyecto es realizar un análisis de la opinión pública sobre los países que participaron en el Mundial de Rusia 2018, mediante el uso de algoritmos de aprendizaje y clasificador de sentimientos de los tweets recolectados desde el 28 de junio hasta el 15 de julio del 2018, fechas en las cuales se realizaron los partidos respectivos del mundial.

**Objetivos específicos**


+ Crear  un  clasificador  de  sentimiento en  inglés  utilizando  datos 
extraídos
de  Twitter  para  minar 
opinión pública en los siguientes 
países
: argentina, belgica, brasil, co
lombia, croacia, dinamarca, 
espania,  francia,  inglaterra,  japon,  mexico,  panama,  polonia,  portugal,  rusia,  senegal,  suecia, 
suiza, tunez, uruguay
+ Identificar y seleccionar las herramientas necesarias para procesar y analizar datos provenientes 
de Twitter


**Herramientas**
+ CouchDB
+ Phyton (lenguaje de programación)
+ OracleVM VirtualBox 5.2 
+ Sistema operativo Ubuntu 

**Instalación**

**CouchDB**

1. Instalar Apache en Ubuntu


Paso 1

Antes de iniciar con el proceso de instalación de Apache CouchDB, será necesario instalar el servidor web Apache en Ubuntu, para ello podemos ejecutar el siguiente comando:

    sudo apt-get install apache2 -y
    
Paso 2

Una vez que Apache sea instalado completamente, debemos iniciar el servidor web Apache y habilitarlo para iniciar junto a el tiempo de arranque del sistema con el siguiente comando:

    sudo systemctl start apache2
    sudo systemctl enable apache2
    
 2. Instalar Apache CouchDB en Ubuntu
 
 
Paso 1

Procedemos a actualizar el sistema usando el comando:

    sudo apt-get update -y

Paso 2

Finalmente instalamos Apache CouchDB ejecutando:

    sudo apt-get install couchdb -y

Paso 3

Durante este proceso serán desplegada una serie de preguntas para definir parámetros como. En primer lugar, veremos una descripción sobre cómo funciona Apache CouchDB y daremos clic derecho en Aceptar

Paso 4

A continuación seleccionamos el tipo de configuración de CouchDB y en este caso elegimos "Standalone"


Paso 5

Damos Enter y a continuación definiremos la interfaz de conexión a CouchDB desde el navegador, podemos establecer la dirección 0.0.0.0 para que habilite todas las interfaces disponibles

Paso 6

Una vez instalado, ejecutamos las siguientes líneas para iniciar el servicio y habilitarlo al arranque de Ubuntu 18:

    sudo systemctl start couchdb
    sudo systemctl enable couchdb

Paso 7

Comprobamos el estado del servicio de CouchDB ejecutando:

    sudo systemctl status couchdb


3. Acceder a Apache CouchDB en Ubuntu 

 

Paso 1

Ahora podremos acceder a Apache CouchDB ejecutando la siguiente sintaxis, en un navegador de Ubuntu

    http://IP:5984/_utils/
    
    
    
    
    
    
**I
**Desarrollo**


