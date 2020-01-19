#!/usr/bin/env ipython

import os	#Módulo que nos permite acceder a funcionalidades del Sistema Operativo.
import re   #Módulo que contiene los métodos necesarios para analizar y buscar expresiones regulares en Python.
import sys  #Módulo encargado de proveer variables y funcionalidades.
from Bio.ExPASy import Prosite, Prodoc 

#Función "Parse_dat" --> parsea el archivo.dat que contiene los datos de prosite.
def Parser_dat(prosite="prosite.dat"):
	"""prosite= archivo .dat que contiene la información de la base de datos prosite.
	Esta función genera un archivo llamado "prosite_paraseada" con el anterior parseado."""
	if os.path.exists(prosite):
		handle = open(prosite,"r") #abrimos el .dat
		parseo=open("prosite_parseada","w") #creamos el archivo que vamos a escribir
		head=("NAME"+"\t"+"ACCESSION"+"\t"+"DESCRIPTION"+"\t"+"PATTERN"+"\n")
		parseo.write(head) #y le añadimos una cabecera
		records = Prosite.parse(handle)
		for record in records:
			N=record.name
			A=record.accession
			D=record.description
			P=record.pattern
			resultado=str(N+"\t"+A+"\t"+D+"\t"+P+"\n") #Escribimos la info que queremos
			parseo.write(resultado)
		parseo.close() #cerramos el archivo una vez escrito.
	else:
		print("Ohhh! El archivo prosite.dat no existe en tu directorio. Asegurate que existe la próxima vez :)")
		sys.exit()
	return

def Convert_Pattern(PP):
	"""PP= patrón de prosite.
	Esta función devuelve el patrón de Prosite en un lenguaje que entiende el módulo re"""

	#Reemplazamientos a realizar:
	PP= PP.replace("-","") 
	PP= PP.replace("{","[^") 
	PP= PP.replace("}","]")
	PP= PP.replace(".","")
	PP= PP.replace("x",".")
	PP= PP.replace("(","{")
	PP= PP.replace(")","}")
	PP= PP.replace("<","^") 
	PP= PP.replace(">","$")

	return(PP)


def Find_Domain(query, prosite="prosite_parseada"):
	"""query= archivo de cada query con los IDs de las subjects y sus secuencias.
	prosite= archivo de Prosite parseado.
	Esta función genera un archivo por cada query con la información acerca de """

	sequence=open(query, "r") #abrimos el archivo query con las secuencias
	sequence=sequence.read() #lo leemos
	seq=sequence.split("\n") #spliteamos por linea
	file_patrones=open(query+"_pattern.txt","w") #abrimos un archivo que se llame como la query+"_pattern.txt"
	#Decido hacerlo en columnas separadas por tabulador porque aunque no sea lo más estético es lo más sencillo a la hora de trabajar (por si el usario luego quiere utilizar el archivo para algo)
	cabecera=("ID_SEQ"+"\t"+"NAME"+"\t"+"ACCESSION"+"\t"+"DESCRIPTION"+"\t"+"PATTERN"+"\t"+"MATCHING SITES"+"\t"+"NUMBER OF MATCHES"+"\n")
	file_patrones.write(cabecera) #Escribimos la cabecera.

	for i in range(len(seq)//2): #recorremos seq
		pros=open(prosite,"r") #abrimos y leemos prosite
		pros=pros.read()
		line=pros.split("\n") #spliteamos por salto de linea

		for j in line[1:]: #recorremos cada linea sin tener en cuenta la primera porque es la cabecera.
			coordenadas=[]
			if j== "": 
				pass
			else: 
				j=j.split("\t") 
				RE=Convert_Pattern(j[3]) #La información del patrón se corresponde con j[3] --> lo transformamos a RE
				if len(j[3]) != 0: #hay algunas lineas que no contienen información de los patrones 
					#en sec el elemento 2*i es el ID de la secuencia y el 2*i+1 es la secuencia.
					if re.search(RE, seq[2*i+1]): #buscamos el patron en la secuencia
						for coincidencia in re.finditer(RE, seq[2*i+1]): #vamos a guardar el punto de inicio y fin de la coincidencia
							s=coincidencia.start() #inicio
							e=coincidencia.end() #fin
							coordenadas.append([s,e]) #lo apendeo como una lista de con coordenadas [x,y] siendo x=principio e y=fin
							num=len(coordenadas) #para ver el número de matches contamos el numero de sublistas que contiene coordenadas.
							resultados=(seq[2*i]+"\t"+j[0]+"\t"+j[1]+"\t"+j[2]+"\t"+j[3]+"\t"+str(coordenadas)+"\t"+str(num)+"\n") #almacenamos en resultados lo que queremos escribir 
							file_patrones.write(resultados) #lo escribimos en el archivo _pattern.txt para cada query
					
	file_patrones.close() #lo cerramos.
		
	return

#Esther Ugarte Carro
#Proyecto Final Programación para Bioinformática
#4º Biotecnología






