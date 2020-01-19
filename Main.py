#!/usr/bin/env ipython

import os #Módulo que nos permite acceder a funcionalidades del Sistema Operativo.
import sys #Módulo encargado de proveer variables y funcionalidades.
import re #Módulo que contiene los métodos necesarios para analizar y buscar expresiones regulares en Python.
import shutil #Módulo de operaciones de archivos de alto nivel como copiar y archivar.
from subprocess import Popen, PIPE #Módulo necesario para la realización de Blast y Muscle.
from Bio import Seq  #Módulo necesario para el parseado del genbank.
from Bio import SeqIO #Módulo necesario para el parseado del genbank.

import Blast 
import Carpet
import Help
import Muscle
import Prosite

## BIENVENIDA AL PROGRAMA ##

print("""\n\t\t¡BIENVENID@S AL PROGRAMA "SEQEUC"!\n 
Este proyecto ha sido realizado por Esther Ugarte Carro como entrega final de Programación de 4º de Biotecnología.\n""")

Help.Ask_Help() #Acceso a la guía del programa antes de comenzar si el usuario así lo desea.


## INTRODUCCIÓN DEL GENBANK Y LA(S) PROTEÍNA(S) QUERY --> PARSEADO Y BLASTP ##
#Archivo Genbank
print("\n\t-PARSEO DEL GENBANK\n")
print("""Por favor, introduzca a continuación el nombre del archivo del genbank frente al que desea realizar el 
BlastP para su parseo. Su extensión debe ser .gbff o se tendrá que introducir de nuevo otro archivo.\n """)
Archivo_genbank=input("\t-¿Qué genbank desea?: ") #El usuario introduce el nombre del archivo. Control de errores dentro de la función
Blast.Parser(Archivo_genbank)

#Archivo Query
print("\n\t-BLASTP")
print("""\nPor favor, ahora introduzca el archivo tipo fasta con su(s) proteína(s) query para poder llevar a cabo el
BlastP frente al subject generado. Su extensión debe ser .fasta o se tendrá que introducir de nuevo otro archivo.\n""")
query=input("\t-¿Qué query desea?: ") #El usuario introduce el nombre del archivo. Control de errores dentro de la función.
Blast.BlastP(query)

## FILTRADO DEL BLAST ##
print("\n\t-FILTRO DE LOS RESULTADOS DEL BLAST\n")
print("""A continuación, se llevará a cabo el filtrado de los resultados del BlastP.""")
Querys=Blast.Filter_Blast()

## ÁRBOLES NEIGHBORJOINING CON MUSCLE ##
print("\n\t-ÁRBOLES NEIGHBORJOINING CON MUSCLE\n")
print("\nAlineando las secuencias de cada query...")
print("\nCreando los árboles para cada query...")
for i in Querys: #Para cada archivo de query con sus secuencias:
	Muscle.Aling(i) #Alineamiento
	Muscle.Make_Tree(i) #Árboles
print("\n ¡Los árboles para aquellas query con más de una secuencia se han generado éxitosamente!")

## PROSITE --> BÚSQUEDA DE PATRONES ##
print("\n\t-BÚSQUEDA DE PATRONES DE PROSITE EN LAS SECUENCIAS\n")

#Comprobar si existe la base de datos Prosite ya parseada y si no, parsearla.
if os.path.exists("prosite_parseada"): #Si es la segunda vez que se ejecuta el programa, la base de datos de Prosite ya estará parseada y podemos evitarnos este paso.
	pass
else: #Si no existe, parseamos Prosite.dat
	Prosite.Parser_dat() 
	print("""\nLa base de datos prosite.dat se ha parseado correctamente. Se ha guardado en un archivo llamado "prosite_parseada". """)

#Búsqueda de patrones para cada secuencia de los querys.
print("\nBuscando los patrones para las secuencias de cada query...")
for i in Querys:
	Prosite.Find_Domain(i) 
print("\n¡La búsqueda de patrones se ha completado éxitosamente!")

## CARPETAS Y ARCHIVOS --> ORGANIZACIÓN RESULTADOS ##
Carpet.Organize(Querys)

print("""\n\t\t¡YA ESTÁ TODO LISTO, MUCHAS GRACIAS POR USAR "SEQEUC" ;) !\n""")


#Esther Ugarte Carro
#Proyecto Final Programación para Bioinformática
#4º Biotecnología





