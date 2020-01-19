#!/usr/bin/env ipython

import os #Módulo que nos permite acceder a funcionalidades del Sistema Operativo.
import sys #Módulo encargado de proveer variables y funcionalidades.
from subprocess import Popen, PIPE #Necesario para la realización del Blast.

## FUNCIONES DEL MÓDULO MUSCLE##

#Función Aling --> alineamiento de las secuencias seleccionadas para cada query.
def Aling(queryID):
	"""queryID= Archivo con el nombre de cada query resultante de la función Filter del módulo Blast, que contiene 
	los ID_Subjects y sus respectivas secuencias completas.
	Esta función devuelve un archivo para cada query con su alineamiento"""
	proceso = Popen(['muscle','-in',queryID], stdout=PIPE, stderr=PIPE)
	listado = proceso.stdout.read().decode("utf-8")
	proceso.stdout.close()
	my_output = open(queryID+".fasta","w")
	my_output.write(listado)
	my_output.close()

	return

#Función Make_Tree --> genera árboles a partir de los alineamientos de cada query. El método elegido es neighborjoining.
def Make_Tree(queryID):
	"""queryID= Archivo con el nombre de cada query.
	Esta función devuelve un archivo .tre con el árbol para cada query"""
	
	#Se tiene en cuenta que el que usa es el de extensión .fasta al añadirlo con +".fasta" y que el de salida es +".tre"
	proceso = Popen(['muscle','-maketree','-in',queryID+".fasta",'-out',queryID+".tre", '-cluster', 'neighborjoining'], stderr=PIPE)
	
	return
#Esther Ugarte Carro
#Proyecto Final Programación para Bioinformática
#4º Biotecnología