import csv

def convertir():
    lstAtributos=[]
    second=''
    prim =''
    with open('InglaterraBelgica.csv') as File:  
        reader = csv.reader(File)
        for row in reader:
            string = str(row)
            a=string.split(",")
            prim = a[1]
            prim=prim[3:]
            second=a[-1]
            second = second[:-3]
            variable=(second, prim)
            lstAtributos.append(variable)
    return lstAtributos
    

        
def agregarCSV(lista):
    csvsalida = open('InglaterraBelgicaMapa.csv', 'w')
    salida = csv.writer(csvsalida)
    salida.writerow(['lat','long'])
    salida.writerows(lista)
    del salida
    csvsalida.close()

s=convertir()
agregarCSV(s)


