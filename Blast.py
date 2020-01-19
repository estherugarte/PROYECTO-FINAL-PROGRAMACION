#!/usr/bin/env ipython

import os #Módulo que nos permite acceder a funcionalidades del Sistema Operativo.
import sys #Módulo encargado de proveer variables y funcionalidades.
from subprocess import Popen, PIPE #Necesario para la realización del Blast.
from Bio import Seq  #Necesario para el parseado.
from Bio import SeqIO #Necesario para el parseado.


## FUNCIONES DEL MÓDULO BLAST ##

#Función "Parser" --> recibe el genbank introducido por el usuario y lo transforma en un archivo multifasta. 
def Parser(Archivo_genbank):
    """Archivo= genbank introducido por el usuario.
    Esta función devuelve un archivo multifasta llamado "subject" que contiene 
    multitud de secuencias de proteínas obtenidas de genbanks."""

    if os.path.exists(Archivo_genbank): #Si el archivo existe en la carpeta
        Nombre=os.path.splitext(Archivo_genbank)
        Extension=Nombre[1] #Se comprueba que la extensión sea la correcta
        if Extension == ".gbff":  #Si lo es:
            subject=open("subject", "w") #Si el archivo ya existe se sobreescribe y por ello no hace falta un control de su existencia

            with open(Archivo_genbank, "r") as input_handle:
                for record in SeqIO.parse(input_handle, "genbank"):
                    print()
                for feature in record.features:
                    if feature.type == 'CDS':
                        try: #Puede ser que el genbank introducido por el usuario no pueda ser traducido porque ya contiene la secuencia proteica.
                            locus = feature.qualifiers['locus_tag'][0] #Coge los ID de las subjects.
                            secuencia_proteina= feature.qualifiers['translation'][0] #La secuencia traducida.
                            resultado=str(">"+locus+"\n"+ secuencia_proteina +"\n")  #Me almacena los ID y las secuencias
                            subject.write(resultado) #lo escribe en mi archivo final linea por linea
                        except:
                            pass
            subject.close() #cerramos el archivo una vez escrito.
            print("""\nEl parseado del archivo genbank introducido se ha completado éxitosamente. Se ha creado un archivo 
multifasta llamado "subject" con todas las secuencias.""")
            
        else: #Si la extensión no es .gbff:
            print("El archivo introducido no tiene extensión .gbff. Por favor, introduzca otro.") 
            salir=input("¿O prefiere salir?[S/N]:" ) #le damos la opción de salir al usuario.
            c=False
            while c == False:   
                if salir.upper()== "S":
                    c=True
                    sys.exit()
                elif salir.upper()== "N":  #Si no quiere salir
                    c=True
                    Archivo_genbank=input("\t-¿Qué genbank desea?: ") #Se vuelve a preguntar al usuario
                    Parser(Archivo_genbank) #Se vuelve a llamar a la función con el nuevo archivo
                else: #error
                    print("La opción introducida no es válida.")
                    salir=input("¿O prefiere salir?[S/N]:" ) #vuelve a preguntar si quiere salir

    else:
        print("El archivo introducido no existe. Por favor, introduzca otro.")
        salir=input("¿O prefiere salir?[S/N]:" )
        ct=False
        while ct == False:   
            if salir.upper()== "S": #si quiere salir se sale
                ct=True
                sys.exit()
            elif salir.upper()== "N": #si se queda
                ct=True
                Archivo_genbank=input("\t-¿Qué genbank desea?: ")  #vuelve a preguntar
                Parser(Archivo_genbank) #Se vuelve a llamar a la función con el nuevo archivo
            else:
                print("La opción introducida no es válida.")
                salir=input("¿O prefiere salir?[S/N]:" )
              
    return


#Función "Blastp" --> recibe las secuencias query y subject y lleva a cabo el Blastp en bash gracias a POPEN.
def BlastP(query, subject= "subject"):
    """query= archivo de tipo fasta o multifasta que contiene la secuencia o secuencias query.
    subject= archivo multifasta que contiene las secuencias subject generado en la función Parser.
    Esta función devuelve un archivo llamado "blast_result" que contiene el resultado del blastp con el ID 
    de la secuencia y del query y los valores de la cobertura, el % de identidad y el evalue respectivamente"""

    if os.path.exists(query): #Si el archivo existe en la carpeta
        Nombre=os.path.splitext(query)
        Extension=Nombre[1] #Se comprueba que la extensión sea la correcta
        if Extension == ".fasta":  #Si lo es, se lleva a cabo el blastP:
            proceso = Popen(['blastp','-query',query,'-subject',subject,'-outfmt',"6 qseqid sseqid qcovs pident evalue" ], stdout=PIPE, stderr=PIPE)
            error_encontrado = proceso.stderr.read()
            listado = proceso.stdout.read().decode("utf-8")
            proceso.stdout.close()
            proceso.stderr.close()

            my_output = open("blast_result","w")
            my_output.write(listado)

            if not error_encontrado: 
                print("""\nEl Blastp se ha llevado a cabo éxitosamente y se ha generado un archivo llamado "blast_result" con sus resultados:\n\n""")
                print("ID_Query"+"\t"+"ID_Subject"+"\t"+"Cobertura"+"\t"+"Pocentaje de Identidad"+"\t"+ "Evalue"+"\n")
                print(listado)
            else: 
                print("Se produjo el siguiente error:\n%s" % error_encontrado)

        else: #Si no lo es
            print("El archivo introducido no tiene extensión .fasta. Por favor, introduzca otro.") #Se vuelve a preguntar al usuario
            salir=input("¿O prefiere salir?[S/N]:" ) #le damos la opción de salir al usuario.
            c=False
            while c== False:
                if salir.upper()== "S":
                    c= True
                    sys.exit()
                elif salir.upper()== "N":  #Si no quiere salir
                    c=True
                    query=input("\t-¿Qué query desea?: ") #Se vuelve a preguntar al usuario
                    BlastP(query) #Se vuelve a llamar a la función con el nuevo archivo
                else: #error
                    print("La opción introducida no es válida.")
                    salir=input("¿O prefiere salir?[S/N]:" ) #vuelve a preguntar si quiere salir

    else: #Si el archivo no existe en la carpeta:
        print("El archivo introducido no existe. Por favor, introduzca otro.")
        salir=input("¿O prefiere salir?[S/N]:" )
        ct=False
        while ct == False:
            if salir.upper()== "S": #si quiere salir se sale
                ct=True
                sys.exit()
            elif salir.upper()== "N": #si se queda
                ct=True
                query=input("\t-¿Qué query desea?: ")  #vuelve a preguntar
                BlastP(query) #Se vuelve a llamar a la función con el nuevo archivo
            else:
                print("La opción introducida no es válida.")
                salir=input("¿O prefiere salir?[S/N]:" )
    
    return

#Función "Filter" --> recibe el archivo con los resultados del Blastp y los filtra en función de los parámetros introducidos por el usuario.
def Filter_Blast(Resultado_Blastp = "blast_result"):
    """Resultado_Blastp= archivo que contiene los resultados del Blastp.
    Esta función devuelve un archivo por query con los subjects y sus respectivas secuencias completas
    obtenidas del Genbank que cumplan el filtro introducido por el usuario."""
    
    #Parámetros de filtrado a utilizar por el usuario:
    print("\nPor favor, introduzca los parámetros:\n")
    try: #Pregunta al usuario qué parámetros quiere
        coverage=float(input("\t\t-¿Qué valor de coverage desea? (filtro por mayor o igual): "))
        pident=float(input("\t\t-¿Qué porcentaje de identidad desea? (filtro por mayor o igual): "))
        evalue=float(input("\t\t-¿Qué valor de evalue desea? (filtro por menor o igual): "))
    except ValueError: #Si no se introduce un número, se vuelve a preguntar al usuario.
        print("\nAlguno de los valores introducidos no es un número. Por favor, vuelva a introducirlos.")
        coverage=float(input("\t\t-¿Qué valor de coverage desea? (filtro por mayor o igual): "))
        pident=float(input("\t\t-¿Qué porcentaje de identidad desea? (filtro por mayor o igual): "))
        evalue=float(input("\t\t-¿Qué valor de evalue desea? (filtro por menor o igual): "))

    #Abrimos el archivo con los resultados del Blastp y lo convertimos en listas para poder trabajar con él.
    Filter=open(Resultado_Blastp)
    Filter=Filter.read()        
    Filter=Filter.split("\n")
    
    List=[] #Lista que contiene los resultados del blast en listas.
    Filtrado=[] #Lista que contiene query y subject que cumplen los parámetros.
    
    for i in Filter: #Recorremos el archivo del Blast spliteado por lineas. De cada linea separamos los elementos por el tabulador
        if i== '': #Los espacios no los tenemos en cuenta, ya que si no se añadirían como un elemento más. 
            pass
        else:
            i=i.split("\t")
            List.append(i)    #Aquí ya tenemos los resultados del Blast en Listas con sublistas.
    
    for j in range(len(List)): #Recorremos cada Lista de List sabiendo y sabiendo la posición que ocupan nuestros parámetros, llevamos a cabo el filtrado.
        if float(List[j][2])>= coverage and float(List[j][3])>= pident and float(List[j][4])<= evalue:
            Filtrado.append([List[j][0],List[j][1]]) #Aquí tenemos la lista con los querys y sus subjects que cumplen los parámetros. Es una lista con listas por cada query.
    
#Si para la combinación de parámetros no hay resultados, se pregunta al usuario qué quiere hacer:
    if Filtrado == []:
        print("\nNo hay resultados para la combinación de parámetros introducidos.")
        C=True
        while C== True:
            otravez=str(input("""\nIntroduzca la opción que desee: 
A)Volver a introducir parámetros
B)Salir
"""))
            if otravez.upper()== "A": #volver a introducirlos
                C=False
                Filter_Blast()
            elif otravez.upper() =="B": #Salir del programa
                C=False
                sys.exit()
            else: #Se equivoca al escribir
                print("La opción introducida no es válida")
                otravez=str(input("""\nIntroduzca la opción que desee: 
A)Volver a introducir parámetros
B)Salir
"""))

    else: #Si hay resultados seguimos palante!
        print("\nEl filtrado de los resultados se ha completado éxitosamente. Se muestra a continuación una lista de listas con los querys y sus respectivos subjects que cumplen los parámetros\n")
        print(Filtrado)
       

    #Lista con los IDs de las querys que pasan el filtro.
    ID_Query=[]
    for i in range(len(Filtrado)): #Recorremos la lista Filtrado
        if Filtrado[i][0] in ID_Query: #Si el elemento [i][0] de Filtrado (que se corresponde con el ID de la Query) ya está en la lista de ID de Querys --> pass
            pass 
        else: #Si no está, se añade y así al final tenemos una lista con los IDs de las queries con las que vamos a trabajar.
            ID_Query.append(Filtrado[i][0])  
   

    #A continuación el objetivo es crear un archivo para cada query con los IDs de sus subjects y sus secuencias completas, obtenidas del Genbank.

    for j in range(len(ID_Query)): #Recorremos la lista de los IDs de los Query
        sbj=[] #Lista con los subjects de determinada Query
        for k in range(len(Filtrado)): #Recorremos Filtrado
            if ID_Query[j] == Filtrado[k][0]: #Si el ID de la Query que se esta recorriendo se corresponde con el elemento [k][0] de Filtrado se añade a Suject.
                sbj.append(Filtrado[k][1]) #Lista con los Subjects del query
      
        file=(ID_Query[j]) #Vamos a querer crear un archivo que se llame con el nombre de cada query.
        Resultado=open(file, "w") 

        Genbank=open("subject","r") #Abrimos el archivo parseado del Genbank que sabemos que se llama "subject" ya que es así como lo devuelve la función Parser.
        Genbank=Genbank.read() #Lo leemos
        s=Genbank.split("\n")  #Spliteamos por salto de linea
        sec=[] #Lista vacía que va a contener los ID_Subject + sus secuencias completas

        for j in range(len(sbj)): #Recorremos Subject
           for i in range(len(s)//2): 
               if s[2*i] == ">" + sbj[j]: #Buscamos coincidencia en el genbank
                sec.append(s[2*i]+"\n"+s[2*i+1]) #Si existe, se guarda el ID con el > que es el elemento 2*i y la secuencia 2*i+1 separados por salto de linea.
        Resultado.write("\n".join(sec)) #Se escribe el Archivo de la query.

    return(ID_Query) #Return de la lista con los IDs de las queries porque nos es útil en el main. 

#Esther Ugarte Carro
#Proyecto Final Programación para Bioinformática
#4º Biotecnología