# ProyectoBI_2018A
Grupo 05


Integrantes:

   Macas Alexandra


   Giler Mario
             
**TEMA: Diseño e Implementación de un modelo de clasificación de sentimientos utilizando 
machine learning** 


**Objetivo**

El objetivo de este proyecto es realizar un análisis de la opinión pública sobre los países que participaron en el Mundial de Rusia 2018, mediante el uso de algoritmos de aprendizaje y clasificador de sentimientos de los tweets recolectados desde el 28 de junio hasta el 15 de julio del 2018, fechas en las cuales se realizaron los partidos respectivos del mundial.

Los países que analizar son los siguientes junto con la base de datos de Rusia:
+ De la fecha 6 de julio:


  Uruguay – Francia
  
  Brasil – Bélgica

+ De la fecha 14 de julio (Tercer puesto)

  Bélgica – Inglaterra

+ De la fecha 15 de julio (Final)

  Francia - Croacia


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
+ Sistema operativo Ubuntu 16.04.1

    
**Fases del Proyecto**


Adquisición de datos


En la esta primera fase del proyecto se recolecto los datos mediante un cosechador de tweets (script de phyton), que fue proporcionado en el aula virtual, junto con las herramientas de couchDB,y una base de datos NoSQL(CouchDb), terminal de Ubuntu, el Script de phyton, Twitter. Con el fin de recolectar en las fechas establecidas un total de 20 partidos del mundial.
Para esto se realizo los siguientes pasos:
+ Abrimos couchDB con la siguiente dirección:

      https://localhost:5984/_utils/index.html
       
+ Creamos un database con el nombre del país el cual se cosechara los tweets.
+ Creamos una aplicación de twitter y dentro de estas tendremos las credenciales necesarias para poder correr el siguiente script harvester_uio.py. para este caso es necesario ingresar a nuestra cuenta de twitter.

      https://developer.twitter.com/
+ Seleccionamos las coordenadas del país a cosechar los tweets en:

      https://boundingbox.Idokantech.com 
+ En el script harvester_uio.py. se modificó las credenciales del API de twitter e ingreso las coordenadas del área a cosechar.

**Preprocesamiento**


En este paso mediante couchDB se genera la vista de cada base de datos de un país, para posterior ser procesado, analizado y limpiado.
Para el filtrado de los tweets se usó las siguientes sintaxis:

**Vista para la fecha del partido y etiquetarlos**

    function(doc) {
      var fecha= doc.created_at;
      var mes=fecha.substring(0, 10);
        if(mes=='Fri Jul 06' && doc.lang=='en'){
      var str = doc.text.replace(/[^a-zA-Z 0-9.]+/g,' ');
      str = str.toUpperCase();
      var exacto= fecha.substring(0,13)
      emit(exacto, str)
      }
    }
**Vista para la fecha**

    function(doc) {
      if(doc.lang=='en'){
       var fecha= doc.created_at;
       var str = doc.text.replace(/[^a-zA-Z 0-9.]+/g,' ');
       str = str.toUpperCase();
       var exacto= fecha.substring(0,13)
       emit(exacto, str)
       }
    }

**Vista  por país**

    function(doc) {
      var country= doc.place.country;
       if(country=='United Kingdom'){
        var str = doc.text.replace(/[^a-zA-Z 0-9.]+/g,' ');
        str = str.toUpperCase();
        emit(country, str)
       }
    }

**Vista para la coordenadas del país**

    function(doc) {
    if(doc.coordinates!=null)
    emit(doc.coordinates.coordinates, doc.text);
    }

**Vista para los tweets relacionados del mundial por país**

    function(doc) {
    var country= doc.place.country;
      if(country=='United Kingdom' && doc.lang=='en'){
      var str = doc.text.replace(/[^a-zA-Z 0-9.]+/g,' ');
      str = str.toUpperCase();
      emit(country, str)
      }
    }

**Vista para el idioma**

    function(doc) {
    var lang= doc.lang;
    var str = doc.text.replace(/[^a-zA-Z 0-9.]+/g,' ');
    str = str.toUpperCase();
    emit(lang, str)
    }

**Procesamiento**

Con la vista preprocesada de cada base de datos de un país se debe usar un script de phyton para la limpieza de emojis, caracteres especiales, links, tags debido a que estos caracteres no son usados para este análisis, con la siguiente sintaxis:

    def remove_emoji(string):
    emoji_pattern = re.compile(
      u"(\ud83d[\ude00-\ude4f])|" # emoticons
      u"(\ud83c[\udf00-\uffff])|" # symbols & pictographs (1 of 2)
      u"(\ud83d[\u0000-\uddff])|" # symbols & pictographs (2 of 2)
      u"(\ud83d[\ude80-\udeff])|" # transport & map symbols
      u"(\ud83c[\udde0-\uddff])" # flags (iOS)
      "+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


    def limpiarTweets(tweet):
      valida1=re.sub('[^A-Za-z0-9]+', ' ', tweet)
      valida2=re.sub(r"http\S+", " ", valida1)
      valida3=re.sub(r'^RT[\s]+', ' ', valida2)
      valida4= re.sub(r'\$\w*', ' ', valida3)
      resultado=remove_emoji(valida4)
      return resultado
      
Posterior filtramos solo los tweets que hacen referencia del mundial.
      
      lstHashtags={"principal":"#Rusia2018",
        "secundario":"#WorldCup",
        "alterno":"#WorldCupFinal",
        "argentina":"#ARG",
        "belgica":"#BEL",
        "brasil":"#BRA",
        "colombia":"#COL",
        "croacia":"#CRO",
        "dinamarca":"#DEN",
        "inglaterra":"#ENG",
        "espana":"#ESP",
        "francia":"#FRA",
        "japon":"#JPN",
        "mexico":"#MEX",
        "panama":"#PAN",
        "polonia":"#POL",
        "portugal":"#POR",
        "rusia":"#RUS",
        "senegal":"#SEN",
        "suiza":"#SUI",
        "suecia":"#SWE",
        "tunez":"#TUN",
        "uruguay":"#URU"}
    
  **Análisis**
  
Para este paso de análisis de la opinión publica se debe identificar mediante un clasificador la tendencia de la opinión de los usuarios.
Se realizo los siguientes análisis de tweets:

+ Tweets por fecha de partido (Extra)

En este análisis cada equipo que avanzaba en el campeonato aumentaba el número de tweets. Para esto se uso cada fecha en que jugaba el equipo.
+ Tweets por fecha

En este análisis general desde la fecha 28 de junio hasta 15 de julio, el 11 de julio hubo una gran cantidad de tweets del partido Inglaterra vs Croacia ya que ambos equipos eran los favoritos y este partido hubo prorroga y penales siendo el ganador Croacia.
+ Tweets por ubicación geográfica (mapa de calor)

En este caso dependía del partido, los países que estaban seleccionados para llegar a la final tenían un numero tweets igual a los que llegaron a la final del campeonato y los que se encuentran en la periferia de un país presentaban más apoyo a su equipo.
+ Tweets por idioma general(barras)

En este caso el idioma que se presento en una gran escala fue el inglés, posterior el español, debido a que la gente realizaba tweets en Ingles.

+ Tweets por idioma (extra)

En este caso dependía del partido y el equipo que ganaba generaba el público más tweets.
+ Porcentaje de sentimientos (pastel)

En este caso para cualquier equipo hay mas número de tweets neutrales, pero haciendo un énfasis de positivos y negativos de un equipo hay mas positivos, pero si se une tanto positivo como negativo sobrepasan el sentimiento de neutral, por lo cual la gente estuvo interviniendo en las redes sociales para dar apoyo a su equipo.
+ Tweets por país

En este análisis Rusia a pesar de ser el país anfitrión del Mundial no genero tanta cantidad de tweets de apoyo para los distintos partidos del mundial solo cuando jugaba su país, por otro lado, los equipos favoritos para llegar a la final tenían una cantidad mayor a los otros equipos.

+ Tweets (relacionados al mundial) por país
Si se hace una relación con todos los tweets del mundial, la gran mayoría de tweets que se referían al mundial y los demás tweets eran de opiniones de diferentes tópicos.

**Conclusiones**


Se logro realizar todos los análisis propuestos para este proyecto, incluyendo dos análisis extras. Además mediante esta recolección de tweets del curso de logro determinar distintos análisis por partido y en general como análisis de sentimientos, que país genero más número de tweets, en que lugares hubo más tweets y demás.

Las herramientas usadas para este proyecto fueron muy útiles y de facil uso lo que causo la disminución de la complejidad para las fases del proyecto. 

Debido a la cantidad de tweets se recomendaría hacer uso de la computación de la nube ya que el procesamiento de una base de datos grande una máquina consume muchos recursos y hace que la máquina baje en su rendimiento.

**Apéndice**


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
    
**Instalación de Oracle VMVirtualBox**

    https://www.youtube.com/watch?v=nQiR5_iGVJI
    
**Instalación de Ubuntu**

    https://www.youtube.com/watch?v=nQiR5_iGVJI
    
**Instalación de phyton**

    https://www.youtube.com/watch?v=7KeeR20VBKY
















