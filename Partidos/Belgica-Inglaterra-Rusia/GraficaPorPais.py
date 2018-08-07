#-*- coding: utf-8 -*-
import couchdb
import re
import sys
import urllib2
import json
import textblob
import matplotlib.pyplot as plt
from googletrans import Translator
import re
from pylab import *
from couchdb import view
URL = '192.168.100.16'
db_name = 'inglaterra'
db_nameSecond = 'belgica'
db_nameThird = 'rusia'
server = couchdb.Server('http://'+URL+':5984/')
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
def remove_emoji(string):
    emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def limpiarTweets(tweet):
    valida1=re.sub('[^A-Za-z0-9]+', ' ', tweet)
    valida2=re.sub(r"http\S+", " ", valida1)
    valida3=re.sub(r'^RT[\s]+', ' ', valida2)
    valida4= re.sub(r'\$\w*', ' ', valida3)
    resultado=remove_emoji(valida4)
    return resultado

def couchdb(db_name,URL, db_nameSecond, db_nameThird):
    lstHoras =[0,0,0]
    contador = 0
    while contador < 3 :
        
        try:
            print db_name
            db = server[db_name]
            print 'success'

        except:
            sys.stderr.write("Error: DB not found. Closing...\n")
            sys.exit()
        vista= db_name[:4]
        url = 'http://'+URL+':5984/'+db_name+'/_design/'+vista+'country/_view/'+vista+'country'
        req = urllib2.Request(url)
        f = urllib2.urlopen(req)
        d = json.loads(f.read())
        for x in d['rows']:
            texto=x['value']      
            tweetLimpio = limpiarTweets(texto)
            key = x['key']
            if key == 'United Kingdom':
                lstHoras[0]+=1
            elif key == 'Belgium':
                lstHoras[1]+=1
            elif key == 'Rusia':
                lstHoras[2]+=1
        contador= contador+1
        db_name= db_nameSecond
        db_nameSecond=db_nameThird
    fig = plt.figure(u'Gráfica Inglaterra-Belgica') # Figure
    ax = fig.add_subplot(111) # Axes
    nombres = ['United Kingdom','Belgica','Rusia']
    xx = range(len(lstHoras))
    ax.bar(xx, lstHoras, width=0.8, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)
    plt.show()
            

couchdb(db_name, URL, db_nameSecond, db_nameThird)
#stackbuilders

######################################################################################
#archivo = open("/home/mario/Descargas/Inglaterra.json","a") #opens file with name of "test.txt"
"""cont_positives = 0
cont_negatives = 0
cont_neutrals = 0
cont_total = 0

translator = Translator()
for x in d['rows']:
    a = x['value']
    valida=re.sub('[^A-Za-z0-9]+', ' ', a)
    traduccion= translator.translate(valida, dest='en')
    
    texto_tweet = textblob.TextBlob(traduccion.text)
    print texto_tweet
    print '\n'
    auc = ''

    if texto_tweet.sentiment.polarity > 0:
        aux = traduccion.text + ';positive'
        cont_positives = cont_positives + 1
    elif texto_tweet.sentiment.polarity < 0:
        aux = traduccion.text + ';negative'
        cont_negatives = cont_negatives + 1
    else:
        aux = traduccion.text + ';neutral'
        cont_neutrals = cont_neutrals + 1

    #archivo.write(str((aux.encode("utf-8") + "\n")))
    print aux
    print '\n'
   # cont_total = cont_total + 1

#archivo.close()

#print ("total: " + str(cont_total))
#print ("positives: " + str(cont_positives))
#print ("negatives: " + str(cont_negatives))
#print ("neutrals: " + str(cont_neutrals))


# make a square figure and axesfigure(1, figsize=(8,8))# tamanio de figura
#ax = axes([0, 0, 0.9, 0.9])# donde esta la figura ancho alto etc..
#----------------------------------------------------------------------
#labels = 'Positivos ', 'Negativos', 'Neutrales '#nomre de los datos
#fracs = [cont_positives,cont_negatives,cont_neutrals]#datos a graficar
#----------------------------------------------------------------------
#explode=(0, 0.1, 0)#exposicion de uno de los datos segun donde se encuentra
#tipo de grafico(datos,exposicion, titulos de los datos, nose,sombras true o false
#pie(fracs, explode=explode,labels=labels, autopct='%10.0f%%', shadow=True)
#legend()
#title('Evaluacion de Sentimientos Tweets Inglaterra', bbox={'facecolor':'0.8', 'pad':5})

#savefig("tweets_sentiments_inglaterra.png")
#show()#mostrar grafico


f.close()"""

