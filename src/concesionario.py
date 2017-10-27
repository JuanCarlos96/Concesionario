#!/usr/bin/env python
#vim: set encoding=utf-8

import sys
try:
    import pygtk
    pygtk.require("2.0") 
except:
    print "Error GTK"  
    sys.exit(1)
try:
    import gtk
    import gtk.glade
except:
        print "Error GTK"  
	sys.exit(1)

class Concesionario:
	"""Ejemplo de llamada a Interfaz GLADE"""

	def __init__(self):
		
		#Guarda el nombre del fichoro Glade y lo carga
		#self.gladefile = "Ejemplo1.glade"  
		#self.wTree = gtk.glade.XML(self.gladefile) 
                
                self.b = gtk.Builder()
                self.b.add_from_file("concesionario.glade") #Fichero GLADE
                
                self.b.connect_signals({ #Definicion de señales de asociación GLADE-PYGTK
                "on_btn_add_venta_main_clicked" : self.add_venta,
                "on_btn_cancelar_add_venta_clicked" : self.ocultar_add_venta,
                "on_btn_add_revision_main_clicked" : self.add_revision,
                "on_btn_cancelar_add_revision_clicked" : self.ocultar_add_revision})

                #Toma el nombre de la ventana a mostrar
		self.w_main = self.b.get_object("main")
              
                #Muestra la ventana
                self.w_main.show()
        
        def add_venta(self,w):
            self.b.get_object("add_venta").show()
	
        def ocultar_add_venta(self,w):
            self.ocultar("add_venta")
        
        def add_revision(self,w):
            self.b.get_object("add_revision").show()
        
        def ocultar_add_revision(self,w):
            self.ocultar("add_revision")
        
        
        #Funciones auxiliares
        def ocultar(self,ventana):
            self.b.get_object(ventana).hide()
if __name__ == "__main__":
    v = Concesionario() #Llama a la Clase
    gtk.main() #Ejecuta el programa
    