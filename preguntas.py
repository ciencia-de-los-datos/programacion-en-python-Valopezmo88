"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
 import csv
 with open("data.csv", "r") as datos:
    reader = csv.reader(datos, delimiter='\t')
    lista= []
    for fila in reader: 
        lista.append(fila) 

 suma = 0
 for fila in lista: 
   suma += int(fila[1])
 return suma
pregunta_01()



def pregunta_02():
    from operator import itemgetter
    import csv
    with open("data.csv", "r") as datos:
      reader = csv.reader(datos, delimiter='\t')
      lista= []
      for fila in reader: 
        lista.append(fila) 

    col1 = ""
    for fila in lista: 
     col1 += fila[0]
    tupla = []
    for letra in set(col1):
     tupla.append((letra, col1.count(letra)))
    tupla.sort(key=itemgetter(0))
    return tupla
pregunta_02()


def pregunta_03():
    from operator import itemgetter
    import csv
    with open("data.csv", "r") as datos:
      reader = csv.reader(datos, delimiter='\t')
      lista= []
      for fila in reader: 
        lista.append(fila) 

    letras_unicas = set()
    for fila in lista:
     letras_unicas.add(fila[0])

    conteo = {letra:0 for letra in letras_unicas}
    for fila in lista:
     conteo[fila[0]] +=  int(fila[1])
    tuplas = [tupla for tupla in conteo.items()]
    tuplas.sort(key=(itemgetter(0)))
    return  tuplas
pregunta_03()


def pregunta_04():
    from operator import itemgetter
    with open("data.csv", "r") as file: 
     data = file.readlines()

    fecha=[row.split('\t')[2] for row in data]
    col_mes = [row[5:7] for row in fecha]
    col_mes
    tupla = []
    for mes in set(col_mes):
     tupla.append((mes, col_mes.count(mes)))
    tupla.sort()
    return tupla
pregunta_04()


def pregunta_05():
    from operator import itemgetter
    with open("data.csv", "r") as file: 
     data = file.readlines()

    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data]

     #diccionario con clave letra y valor lista de numeros
    result = dict()
    for letra, valor in data:
      valor = int(valor)
      if letra in result.keys():
        result[letra].append(valor)
      else:
        result[letra] = [valor] 
    result = [(letra,max(valor),min(valor)) for letra, valor in result.items()]
    result = sorted(result, key=itemgetter(0))
    return result
pregunta_05()


def pregunta_06():
    from operator import itemgetter
    import csv
    with open("data.csv", "r") as datos:
      reader = csv.reader(datos, delimiter='\t')
      lista= []
      for fila in reader: 
        lista.append(fila)  

    dic = [lista[i][4].split(',') for i in range(0,len(lista))]
    list_1 = [obs for elemento in dic for obs in elemento]
    cadena = [list_1[i].split(':')[0] for i in range(0,len(list_1))] #lista con claves
    cad_1 = [list_1[i].split(':') for i in range(0,len(list_1))] # lista de listas con claves - valor 

    claves = set(cadena)
    result = dict()
    for letra, valor in cad_1:
      valor=int(valor)
      if letra in result.keys():
        result[letra].append(valor)
      else:
        result[letra] = [valor]
    result = [(letra,min(valor),max(valor)) for letra, valor in result.items()]
    result = sorted(result, key=itemgetter(0))
    return result
pregunta_06()


def pregunta_07():
    from operator import itemgetter
    with open("data.csv", "r") as file: 
     data = file.readlines()

    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data]

    result = dict()
    for letra, valor in data:
      valor = int(valor)
      if valor in result.keys():
        result[valor].append(letra)
      else:
        result[valor] = [letra]  
    result = [(valor, letra) for valor,letra in result.items()]
    return sorted(result)
pregunta_07()


def pregunta_08():
    with open("data.csv", "r") as file: 
     data = file.readlines()

    data = [row.split('\t') for row in data]
    data = [row[:2] for row in data]
    result = dict()
    for letra, valor in data:
      valor = int(valor)
      if valor in result.keys():
        result[valor].append(letra)
      else:
        result[valor] = [letra]  
    result = [(valor, sorted(set(letra))) for valor,letra in result.items()]
    return sorted(result)
pregunta_08()


def pregunta_09():
    from operator import itemgetter
    import csv
    with open("data.csv", "r") as datos:
      reader = csv.reader(datos, delimiter='\t')
      lista= []
      for fila in reader: 
        lista.append(fila) 

    dic = [lista[i][4].split(',') for i in range(0,len(lista))]
    list_1 = [obs for elemento in dic for obs in elemento]
    cadena = [list_1[i].split(':')[0] for i in range(0,len(list_1))]
    tupla = []
    for letra in set(cadena):
     tupla.append((letra, cadena.count(letra)))
    tupla.sort(key=itemgetter(0))
    return dict(tupla)
pregunta_09()


def pregunta_10():
    import csv
    with open("data.csv", "r") as datos:
      reader = csv.reader(datos, delimiter='\t')
      lista= []
      for fila in reader: 
        lista.append(fila) 

    col1= [lista[i][0] for i in range(0,len(lista))]
    col5 = [lista[i][4].split(',') for i in range(0,len(lista))]
    col4 = [lista[i][3].split(',') for i in range(0,len(lista))]
    union = list(zip(col1,col4,col5))

    tupla = []
    for letra,col4,col5 in union:
      letra = "".join(letra)
    tupla.append((letra, len(col4),len(col5)))
    return tupla
pregunta_10()


def pregunta_11():
    import csv
    with open("data.csv", "r") as datos:
      reader = csv.reader(datos, delimiter='\t')
      lista= []
      for fila in reader: 
        lista.append(fila) 

    d = {}
    for fila in lista:
      temp = fila[3].split(",")
      for letter in temp:
        if letter in d.keys():
            d[letter] += int(fila[1])
        else:
            d[letter] = int(fila[1])
    temp = sorted(d.items())
    d = {key:value for key, value in temp}
    return d
pregunta_11()



def pregunta_12():
    import csv
    from re import findall
    with open("data.csv", "r") as datos:
      reader = csv.reader(datos, delimiter='\t')
      lista= []
      for fila in reader: 
        lista.append(fila) 
    d = {}
    for fila in lista:
      temp = sum(map(int, findall("\d+", fila[-1])))
      if fila[0] in d.keys():
        d[fila[0]] += temp
    else:
        d[fila[0]] = temp
    temp = sorted(d.items())
    d = {key:value for key, value in temp}
    return d 
pregunta_12()
