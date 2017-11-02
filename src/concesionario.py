#!/usr/bin/env python
#vim: set encoding=utf-8
from basededatos import *
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

        self.con = Conector("concesionario.db")
        self.db = self.con.dameconexion()
        self.res = self.db.execute("SELECT * FROM sqlite_master WHERE name='Coche'")
        if not self.res.fetchall():
            print("Base de datos vacia. Creando...")
            self.con.crear_esquema("")
        
        print("BBDD Conectada")
        
        #self.db.execute("DELETE FROM Cliente")

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
        "on_btn_cancelar_mod_cliente_clicked" : self.ocultar_mod_cliente,
        "on_Reiniciar _BBDD_activate" : self.reiniciar_bbdd,
        "on_btn_aceptar_add_coche_clicked" : self.add_coche2,
        "on__Salir_activate" : self.on_destroy,
        "on_btn_del_coche_main_clicked" : self.borrar_coche})
        
        self.inicializalistado('treeview1')
        self.listacoches('tabla_coches')
        self.inicializalistado('treeview2')
        self.listarevisiones('revisiones')
        self.inicializalistado('treeview3')
        self.listaventas('venta')
        self.inicializalistado('treeview4')
        self.listadni('dni')
        self.inicializalistado('treeview7')
        self.listacoches2('coches')
        self.inicializalistado('treeview5')
        self.inicializalistado('treeview6')
        self.listaclientes('clientes')
        
        self.b.get_object("main").connect("delete-event", self.on_destroy)
        
        #Toma el nombre de la ventana a mostrar
        self.b.get_object("main").show()
    
    #FUNCIONES PRINCIPALES
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
    
    def add_coche2(self,w):
        bastidor = self.b.get_object("txt_bastidor_add_coche").get_text()
        marca = self.b.get_object("txt_marca_add_coche").get_text()
        modelo = self.b.get_object("txt_modelo_add_coche").get_text()
        tipo = self.b.get_object("txt_tipo_add_coche").get_text()
        motor = self.b.get_object("txt_motor_add_coche").get_text()
        cv = self.b.get_object("txt_cv_add_coche").get_text()
        color = self.b.get_object("txt_color_add_coche").get_text()
        precio = self.b.get_object("txt_precio_add_coche").get_text()
        
        marca = unicode(marca,"utf-8")
        modelo = unicode(modelo,"utf-8")
        tipo = unicode(tipo,"utf-8")
        motor = unicode(motor,"utf-8")
        color = unicode(color,"utf-8")
        
        dialog = self.b.get_object("messagedialog")
        
        error = 0
        
        try:
            value = int(cv)
        except ValueError as err:
            dialog.format_secondary_text("CV no es un número entero")
            self.b.get_object("txt_cv_add_coche").set_text("")
            dialog.run()
            dialog.hide()
            error = 1
        
        try:
            value = float(precio)
        except ValueError as err:
            dialog.format_secondary_text("Precio no es un número real")
            self.b.get_object("txt_precio_add_coche").set_text("")
            dialog.run()
            dialog.hide()
            error = 1
        
        self.db.execute("INSERT INTO Coche('N_Bastidor','Marca','Modelo','Motor','CV','Tipo','Color','Precio') VALUES(?,?,?,?,?,?,?,?)",(bastidor,marca,modelo,motor,cv,tipo,color,precio))
        self.db.commit()
        
        self.b.get_object("txt_bastidor_add_coche").set_text("")
        self.b.get_object("txt_marca_add_coche").set_text("")
        self.b.get_object("txt_modelo_add_coche").set_text("")
        self.b.get_object("txt_tipo_add_coche").set_text("")
        self.b.get_object("txt_motor_add_coche").set_text("")
        self.b.get_object("txt_cv_add_coche").set_text("")
        self.b.get_object("txt_color_add_coche").set_text("")
        self.b.get_object("txt_precio_add_coche").set_text("")
        
        self.b.get_object("add_coche").hide()
        self.listacoches('tabla_coches')
        self.listacoches2('coches')
    
    def ocultar_add_coche(self,w):
        self.ocultar("add_coche")
    
    def mod_coche(self,w):
        self.b.get_object("mod_coche").show()
    
    def borrar_coche(self,w):
        tree_view = self.b.get_object("treeview1")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        bastidor = treemodel.get_value(treeiter, 0)#El número es la columna de la que va a obtener el dato, 0 es la primera columna
        #print(bastidor)
        self.db.execute("DELETE FROM Coche WHERE N_Bastidor=?;",(str(bastidor),))
        self.db.commit()
        self.listarevisiones('revisiones')
        self.listaventas('venta')
        self.listacoches('tabla_coches')
        self.listacoches2('coches')
    
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
    
    def on_destroy(self, w, *signals):
        # return True --> no cierra
        # return False --> cierra
        print("Cerrando BBDD")
        self.db.commit()
        self.db.close()            
        gtk.main_quit()


    #FUNCIONES AUXILIARES
    def ocultar(self,ventana):
        self.b.get_object(ventana).hide()
    
    def reiniciar_bbdd(self,w):
        self.con.crear_esquema("reinicia")
        self.listacoches('tabla_coches')
        self.listarevisiones('revisiones')
        self.listaventas('venta')
        self.listadni('dni')
        self.listacoches2('coches')
        self.listaclientes('clientes')
    
    def inicializalistado(self,treeview):
        celda = gtk.CellRendererText()
        columnas = self.b.get_object(treeview).get_columns()
        i = 0
        for col_i in columnas:
            col_i.pack_start(celda)
            col_i.add_attribute(celda,"text",i)
            i = i+1
    
    def listacoches(self,lista):
        self.lista = self.b.get_object(lista)
        self.lista.clear()
        
        result = self.db.execute('SELECT * FROM Coche')
        for row in result:
            self.lista.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
    
    def listarevisiones(self,lista):
        self.lista = self.b.get_object(lista)
        self.lista.clear()
        
        result = self.db.execute('SELECT N_Revision FROM Revision')
        for row in result:
            self.lista.append([row[0]])
    
    def listaventas(self,lista):
        self.lista = self.b.get_object(lista)
        self.lista.clear()
        
        result = self.db.execute('SELECT N_Bastidor,Dni FROM Venta')
        for row in result:
            self.lista.append([row[0],row[1]])
    
    def listadni(self,lista):
        self.lista = self.b.get_object(lista)
        self.lista.clear()
        
        result = self.db.execute('SELECT Dni FROM Cliente')
        for row in result:
            self.lista.append([row[0]])
    
    def listacoches2(self,lista):
        self.lista = self.b.get_object(lista)
        self.lista.clear()
        
        result = self.db.execute('SELECT N_Bastidor,Marca,Modelo FROM Coche')
        for row in result:
            self.lista.append([row[0],row[1],row[2]])
    
    def listaclientes(self,lista):
        self.lista = self.b.get_object(lista)
        self.lista.clear()
        
        result = self.db.execute('SELECT Dni,Apellidos,Nombre FROM Cliente')
        for row in result:
            self.lista.append([row[0],row[1],row[2]])


if __name__ == "__main__":
    v = Concesionario() #Llama a la Clase
    gtk.main() #Ejecuta el programa
    