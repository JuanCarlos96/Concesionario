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
        "on_btn_add_venta_main_clicked" : self.buscar_cliente,
        "on_btn_cancelar_add_venta_clicked" : self.ocultar_add_venta,
        "on_btn_nuevo_cliente_clicked" : self.add_venta,
        "on_btn_seleccionar_cliente1_clicked" : self.add_venta,
        "on_btn_add_revision_main_clicked" : self.add_revision,
        "on_btn_cancelar_add_revision_clicked" : self.ocultar_add_revision,
        "on_btn_add_coche_main_clicked" : self.add_coche,
        "on_btn_cancelar_add_coche_clicked" : self.ocultar_add_coche,
        "on_btn_mod_coche_main_clicked" : self.mod_coche,
        "on_btn_cancelar_mod_coche_clicked" : self.ocultar_mod_coche,
        "on_btn_mod_revision_main_clicked" : self.mod_revision,
        "on_btn_cancelar_mod_revision_clicked" : self.ocultar_mod_revision,
        "on_btn_mod_venta_main_clicked" : self.message_mod_venta,
        "on_btn_mod_cliente_clicked" : self.mod_venta,
        "on_btn_mod_coche_clicked" : self.mod_venta,
        "on_btn_buscar_dni_clicked" : self.buscar_cliente2,
        "on_btn_buscar_bastidor_clicked" : self.buscar_bastidor,
        "on_btn_seleccionar_cliente2_clicked" : self.seleccionar_cliente,
        "on_btn_seleccionar_coche_clicked" : self.seleccionar_coche,
        "on_btn_cancelar_mod_venta_clicked" : self.ocultar_mod_venta,
        "on_btn_mod_clientes_main_clicked" : self.mod_cliente,
        "on_btn_cancelar_mod_cliente_clicked" : self.ocultar_mod_cliente})

        #Toma el nombre de la ventana a mostrar
        self.b.get_object("main").show()

    def buscar_cliente(self,w):
        self.b.get_object("buscar_cliente_add_venta").show()
    
    def buscar_cliente2(self,w):
        self.ocultar("mod_venta")
        self.b.get_object("buscar_cliente_mod_venta").show()
    
    def buscar_bastidor(self,w):
        self.ocultar("mod_venta")
        self.b.get_object("buscar_coche_mod_venta").show()
    
    def seleccionar_cliente(self,w):
        self.ocultar("buscar_cliente_mod_venta")
        self.b.get_object("mod_venta").show()
    
    def seleccionar_coche(self,w):
        self.ocultar("buscar_coche_mod_venta")
        self.b.get_object("mod_venta").show()
    
    def add_venta(self,w):
        self.ocultar("buscar_cliente_add_venta")
        self.b.get_object("add_venta").show()

    def ocultar_add_venta(self,w):
        self.ocultar("add_venta")

    def add_revision(self,w):
        self.b.get_object("add_revision").show()

    def ocultar_add_revision(self,w):
        self.ocultar("add_revision")
    
    def add_coche(self,w):
        self.b.get_object("add_coche").show()
    
    def ocultar_add_coche(self,w):
        self.ocultar("add_coche")
    
    def mod_coche(self,w):
        self.b.get_object("mod_coche").show()
    
    def ocultar_mod_coche(self,w):
        self.ocultar("mod_coche")
    
    def mod_revision(self,w):
        self.b.get_object("mod_revision").show()
    
    def ocultar_mod_revision(self,w):
        self.ocultar("mod_revision")
    
    def message_mod_venta(self,w):
        self.b.get_object("message_mod_venta").show()
    
    def mod_venta(self,w):
        self.ocultar("message_mod_venta")
        self.b.get_object("mod_venta").show()
    
    def ocultar_mod_venta(self,w):
        self.ocultar("mod_venta")
    
    def mod_cliente(self,w):
        self.b.get_object("mod_cliente").show()
    
    def ocultar_mod_cliente(self,w):
        self.ocultar("mod_cliente")


    #Funciones auxiliares
    def ocultar(self,ventana):
        self.b.get_object(ventana).hide()


if __name__ == "__main__":
    v = Concesionario() #Llama a la Clase
    gtk.main() #Ejecuta el programa
    