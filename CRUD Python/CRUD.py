from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#Desarrollo de la Interfaz Grafica

root = Tk()
root.title('Aplicaccion CRUD')
root.geometry('600x350')

miId=StringVar()
miNombre=StringVar()	
miCargo=StringVar()
miSalario=StringVar()

def conexionBBDD():
	miConexion=sqlite3.connect("base")
	miCursor=miConexion.cursor()

	try:
		miCursor.execute("""


			""")		

def elimin