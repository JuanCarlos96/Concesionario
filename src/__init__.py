#Este fichero configurará la forma de buscar y abrir GTKRC (fichero de configuración del tema de Windows WIMP) 
import os, gtk,sys

#Siempre que ejecutamos un exe se crea un directorio temporal "base" desde donde parte para tomar las rutas relativas
#Está formado por TODOS LOS BINARIOS que hemos almacenado (librerías y demás) y Suele empezar por MEIXXXXX
basedir = sys.path[0] #se toma directorio de trabajo
gtkrc = os.path.join(basedir, 'gtkrc') #junta la ruta de trabajo con el nombre del fichero
print(gtkrc)

#IMPORTANTE: la siguiente línea hace que el fichero gtkrc pueda ser leido por el ejecutable
gtk.rc_set_default_files([gtkrc]) 
print("Fin de procesamiento - fichero init")



