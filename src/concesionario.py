#Ejemplo 1 GLADE
#Jose Maria Molina
#Desarrollo de Interfaces
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

class Ejemplo1:
	"""Ejemplo de llamada a Interfaz GLADE"""

	def __init__(self):
		
		#Guarda el nombre del fichoro Glade y lo carga
		#self.gladefile = "Ejemplo1.glade"  
		#self.wTree = gtk.glade.XML(self.gladefile) 
                
                builder = gtk.Builder()
                builder.add_from_file("concesionario.glade") #Fichero GLADE


                #Toma el nombre de la ventana a mostrar
		self.window = builder.get_object("main")
              
                #Muestra la ventana
                self.window.show()
	
if __name__ == "__main__":
    v = Ejemplo1() #Llama a la Clase
    gtk.main() #Ejecuta el programa
