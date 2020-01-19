#!/usr/bin/env ipython

import os
import sys
import shutil

def Organize(Querys):
	"""Función que organiza los resultados en carpetas.
	Además, pregunta al usuario si le interesa conservar archivos adicionales que el propio programa no devolvería"""

	## RESULTADOS POR DEFECTO ##

	ruta=os.getcwd()	#Obtener ruta desde la que ejecuta el usuario el programa
	n=range(1001)
	n=list(n) #Creamos una lista compuesta por números del 0 al 1000.
	for num in n: #Se recorre cada número de la lista
		if os.path.isdir(ruta+"/RESULTS"+"_"+str(num)): #Si existe el directorio RESULTS acabado en dicho número, se pasa.
			pass
		else: #Si no existe, se crea
			os.mkdir("RESULTS"+"_"+str(num)) #creamos el directorio RESULTS_num
			os.mkdir("Trees") #creamos el directorio Trees
			os.mkdir("Patterns") #creamos el directorio Patterns
			#movemos Trees y Patterns a RESULTS_num
			shutil.move("Trees","RESULTS"+"_"+str(num)) 
			shutil.move("Patterns","RESULTS"+"_"+str(num))
			#movemos subject y blast_result a RESULTS_num
			shutil.move("subject","RESULTS"+"_"+str(num))
			shutil.move("blast_result","RESULTS"+"_"+str(num))

			for i in Querys: 
				try: #puede ser que para alguna query no exista el árbol porque sólo tenía una secuencia.
					#movemos los archivos de las query a sus respectivas carpetas
					shutil.move(i+"_pattern.txt","RESULTS"+"_"+str(num)+"/Patterns")
					shutil.move(i+".tre","RESULTS"+"_"+str(num)+"/Trees")
				except: #no existe, pues es que no se ha generado y pasamos de él.
					pass
			break #importante, en cuánto se crea la carpeta para un num, se corta el bluce for. 
		
	print("\n\t¡YA TIENE LISTOS SUS RESULTADOS!\n")
	print("""En una carpeta llamada RESULTS encontrará:
		-El archivo "blast_result" con los resultados del BlastP.
		-El archivo "subject" con el genbank introducido parseado.
		-Una carpeta llamada "Trees" que contiene los árboles de todas las query que han generado uno.
		-Una carpeta llamada "Patterns" con los archivos con la información de los patrones para cada query.
	El archivo "prosite_parseada" se guarda en el directorio desde el que se ejecuta el programa.""")

	## RESULTADOS ADICIONALES ##

	#Los archivos que contienen por query los ID_Subject y sus secuencias que han superado el filtro del Blast.
	eliminar=input("\n¿Desea conservar también los archivos que contienen los IDs de las subjects y sus secuencias para cada query resultado del filtro del BlastP?[S/N]: ")
	if eliminar.upper() == "N":	
		print("Los archivos serán eliminados.")
		for i in Querys:
			os.remove(i)
	elif eliminar.upper() == "S":
		print("""Los archivos se conservarán y se guardarán dentro de la carpeta RESULTS en una carpeta llamada "Filter_Data" """)
		os.mkdir("Filter_Data")
		shutil.move("Filter_Data","RESULTS"+"_"+str(num))
		for i in Querys:
			shutil.move(i,"RESULTS"+"_"+str(num)+"/Filter_Data")
	else:
		print("La opción introducida no es válida.")
		eliminar=input("\n¿Desea conservar también los archivos que contienen los IDs de las subjects y sus secuencias para cada query resultado del filtro del BlastP?[S/N]: ")

	#Los archivos que contienen las secuencias alineadas por query para los árboles
	elimina=input("\n¿Desea conservar también los archivos con los alineamientos de Muscle? [S/N]: ")
	if elimina.upper() == "N":	
		print("Los archivos serán eliminados.")
		for i in Querys:
			os.remove(i+".fasta")
	elif elimina.upper() == "S":
		print("""Los archivos se conservarán y se guardarán dentro de la carpeta RESULTS en una carpeta llamada "Muscle_Alignment" """ )
		os.mkdir("Muscle_Alignment")
		shutil.move("Muscle_Alignment","RESULTS"+"_"+str(num))
		for i in Querys:
			try:
				shutil.move(i+".fasta","RESULTS"+"_"+str(num)+"/Muscle_Alignment")
			except:
				pass
	else:
		print("La opción introducida no es válida.")
		elimina=input("\n¿Desea conservar también los archivos con los alineamientos de Muscle? [S/N]: ")


#Esther Ugarte Carro
#Proyecto Final Programación para Bioinformática
#4º Biotecnología