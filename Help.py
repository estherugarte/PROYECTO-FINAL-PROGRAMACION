#!/usr/bin/env ipython
import sys #Módulo encargado de proveer variables y funcionalidades.
import os #Módulo que nos permite acceder a funcionalidades del Sistema Operativo.


## FUNCIONES DEL MÓDULO HELP##

#Guia de ayuda del Blast, con opción de salir del programa, comenzar o volver a la guía principal.
def Help_BlastP():
	print("""\n\t-- BLAST P --

	El usuario deberá introducir:
	  -Un archivo .gbff con las secuencias frente a las que se se llevará a cabo el blast obtenidas
	  de genbanks. Este archivo se parseará y se guardará como "subject".
	  -Un archivo .fasta que contenga la o las proteínas query.
	Si los archivos introducidos no tienen la extensión correcta o no existen en el directorio, se 
	dará la oportunidad de introducir otros o abandonar el programa.

	Con el genbank parseado y el archivo .fasta se llevará a cabo el blastp pudiéndose filtrar los 
	resultados a continuación.

	Por último, se generará a partir del filtrado un archivo por query con los ID_Subject + su 
	secuencia """) 
	
	quiere=input("\n¿Desea: A)Volver a la guía, B)Empezar la ejecución del programa o C)Salir? [A/B/C]: ")
	c=True
	while c == True:
		if quiere.upper()== "A":
			c=False
			Help_Guide()
		elif quiere.upper() == "B":
			c=False
			break
		elif quiere.upper() == "C":
			c=False
			sys.exit()
		else:
			print("\nLa opción introducida no es válida")
			quiere=input("\n¿Desea: A)Volver a la guía, B)Empezar la ejecución del programa o C)Salir? [A/B/C]: ")

	return

#Guia de ayuda del Mucle, con opción de salir del programa, comenzar o volver a la guía principal.
def  Help_Muscle():
	print("""\n\t-- MUSCLE --

	Los archivos de cada query con los ID_Subject y sus secuencias serán alineados y a partir de
	de dichos alineamientos se generarán los árboles para cada una.

	OJO!!! Aquellas query con una única secuencia no generarán árboles ya que no se puede alinear. """) 

	quiere=input("\n¿Desea: A)Volver a la guía, B)Empezar la ejecución del programa o C)Salir? [A/B/C]: ")
	c=True
	while c == True:
		if quiere.upper()== "A":
			c=False
			Help_Guide()
		elif quiere.upper() == "B":
			c=False
			break
		elif quiere.upper() == "C":
			c=False
			sys.exit()
		else:
			print("\nLa opción introducida no es válida")
			quiere=input("\n¿Desea: A)Volver a la guía, B)Empezar la ejecución del programa o C)Salir ?[A/B/C]: ")

	return

#Guia de ayuda del Prosite, con opción de salir del programa, comenzar o volver a la guía principal.
def Help_Prosite():
	print("""\n\t-- PROSITE --

	Es necesario que el usuario tenga en su directorio de ejecución el archivo "prosite.dat" para 
	completar la tarea. Compruébelo antes de comenzar.
	Este archivo .dat será parseado y se procederá a la búsqueda de patrones en las secuencias de 
	cada query guardándose la información obtenida en un archivo para cada una.""") 

	quiere=input("\n¿Desea: A)Volver a la guía, B)Empezar la ejecución del programa o C)Salir ?[A/B/C]: ")
	c=True
	while c == True:
		if quiere.upper()== "A":
			c=False
			Help_Guide()
		elif quiere.upper() == "B":
			c=False
			break
		elif quiere.upper() == "C":
			c=False
			sys.exit()
		else:
			print("\nLa opción introducida no es válida")
			quiere=input("\n¿Desea: A)Volver a la guía, B)Empezar la ejecución del programa o C)Salir ?[A/B/C]: ")

	return

#Guia principal con idea general de lo que hace el programa. Opción de saber más de los apartados de este, comenzar la ejecución del programa o salir de este.
def Help_Guide():
	print("""\n\t-- GUÍA DE AYUDA --

	Este programa realiza las siguientes tareas:

	  A) BlastP frente a multitud de secuencias de proteínas obtenidas de genbanks que el
	  propio usuario aportará. Además, el usuario aportará una o varias proteínas query. 
	  Los resultados del BlastP serán filtrados en función de parámetros escogidos por el 
	  usuario.

	  B) Una vez obtenidos los hits, las secuencias (hits) serán alineadas y se generará un
	  árbol filogenético Neighbor-Joining (N-J) para cada query usando el programa MUSCLE.

 	  C) Búsqueda de dominios de proteínas presentes en la base de datos Prosite entre los hits
	  de blast obtenidos. Para cada proteína se indicará el dominio que tiene (name), su 
	  accession, descripción, patrón encontrado, sitio de inicio y final de la coincidencia del 
	  patrón así como el número de veces que se ha encontrado el patrón en la secuencia según la 
	  base de datos de PROSITE.\n""")

	info=input("\n¿Desea saber más acerca de alguno de los apartados, comenzar la ejecución del programa o salir?[A/B/C/START/OUT]: ")
	c=True
	while c == True:
		if info.upper() == "A":
			c=False
			Help_BlastP()
		elif info.upper() == "B":
			c=False
			Help_Muscle()
		elif info.upper() == "C":
			c=False
			Help_Prosite()
		elif info.upper() == "START":
			c=False
			break
		elif info.upper() == "OUT":
			c=False
			sys.exit()
		else:
			print("\nLa opción introducida no es válida.")
			info=input("¿Desea saber más acerca de alguno de los apartados o comenzar la ejecución del programa?[A/B/C/START]: ")
	return

#Pregunta de ayuda al usuario
def Ask_Help():
	"""Da la posibilidad de acceder a la guía del programa  antes de comenzar su ejecución"""
	ayuda=input(str("¿Quiere acceder a la guía del programa antes de comenzar?[S/N]: "))
	if ayuda.upper() == "S":
		Help_Guide()
	elif ayuda.upper() == "N":
		pass
	else:
		print("La opción introducida no es válida.")
		Ask_Help()

	return

#Esther Ugarte Carro
#Proyecto Final Programación para Bioinformática
#4º Biotecnología
