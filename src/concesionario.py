#!/usr/bin/env python
#vim: set encoding=utf-8
from basededatos import *
import sys
import time
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
        "on_btn_seleccionar_cliente1_clicked" : self.seleccionar_cliente2,
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
        "on_btn_del_coche_main_clicked" : self.borrar_coche,
        "on_BotonIzquierdo_Coche" : self.on_boton_coche,
        "on_btn_aceptar_add_venta_clicked" : self.add_venta2,
        "on_SeleccionCliente" : self.on_boton_cliente,
        "on_btn_aceptar_add_revision_clicked" : self.add_revision2,
        "on_SeleccionDni" : self.on_btn_dni,
        "on_SeleccionVenta" : self.on_btn_venta,
        "on_btn_aceptar_mod_coche_clicked" : self.mod_coche2,
        "activaLabel" : self.activaLabel,
        "on_btn_revision" : self.on_btn_revision,
        "on_btn_aceptar_mod_cliente_clicked" : self.mod_cliente2,
        "on_btn_del_clientes_main_clicked" : self.borrar_cliente,
        "on_btn_aceptar_mod_revision_clicked" : self.mod_revision2,
        "on_btn_del_revision_main_clicked" : self.borrar_revision,
        "on_btn_del_venta_main_clicked" : self.borrar_venta})
        
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
        #self.comboMarcas
        
        self.warning = self.b.get_object("warning")
        self.info = self.b.get_object("info")
        self.mensajeborrar = self.b.get_object("mensajeborrar")
        
        self.b.get_object("btn_add_venta_main").set_sensitive(False)
        self.b.get_object("btn_add_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_coche_main").set_sensitive(False)
        self.b.get_object("btn_del_coche_main").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
        self.b.get_object("btn_mod_revision_main").set_sensitive(False)
        self.b.get_object("btn_del_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_clientes_main").set_sensitive(False)
        self.b.get_object("btn_del_clientes_main").set_sensitive(False)
        self.b.get_object("btn_mod_venta_main").set_sensitive(False)
        self.b.get_object("btn_del_venta_main").set_sensitive(False)
        
        self.b.get_object("main").connect("delete-event", self.on_destroy)
        
        #Toma el nombre de la ventana a mostrar
        self.b.get_object("main").show()
    
    #FUNCIONES PRINCIPALES######################################################################################
    def buscar_cliente(self,w):#BOTON DE VENTA EN LA VENTANA PRINCIPAL, ABRE LA VENTANA DE SELECCION DE CLIENTE PARA CREAR UNA VENTA
        self.b.get_object("buscar_cliente_add_venta").show()
    
    
    
    def buscar_cliente2(self,w):#BOTON DE BUSCAR DNI EN LA VENTANA DE MODIFICAR VENTA, ABRE LA VENTANA DE SELECCION DE CLIENTE PARA MODIFICAR UNA VENTA
        self.ocultar("mod_venta")
        self.b.get_object("buscar_cliente_mod_venta").show()
    
    
    
    def buscar_bastidor(self,w):#BOTON DE BUSCAR BASTIDOR EN LA VENTANA DE MODIFICAR VENTA, ABRE LA VENTANA DE SELECCION DE COCHE PARA MODIFICAR UNA VENTA
        self.ocultar("mod_venta")
        self.b.get_object("buscar_coche_mod_venta").show()
    
    
    
    def seleccionar_cliente(self,w):#BOTON DE CARGAR CLIENTE EN LA VENTANA DE SELECCION DE CLIENTE AL MODIFICAR UNA VENTA
        self.ocultar("buscar_cliente_mod_venta")
        self.b.get_object("mod_venta").show()
    
    
    
    def seleccionar_coche(self,w):
        self.ocultar("buscar_coche_mod_venta")
        self.b.get_object("mod_venta").show()
    
    
    
    def add_venta(self,w):#BOTON DE NUEVO CLIENTE EN LA SELECCION DEL CLIENTE PARA HACER UNA VENTA NUEVA
        self.ocultar("buscar_cliente_add_venta")
        
        self.b.get_object("txt_nombre_add_venta").set_editable(True)
        self.b.get_object("txt_apellidos_add_venta").set_editable(True)
        self.b.get_object("txt_dni_add_venta").set_editable(True)
        self.b.get_object("txt_telefono_add_venta").set_editable(True)
        self.b.get_object("txt_direccion_add_venta").set_editable(True)
        
        #OBTENER DATOS DE LA SELECCCION DE LA TABLA DE COCHES
        tree_view = self.b.get_object("treeview1")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        bastidor = treemodel.get_value(treeiter, 0)
        marca = treemodel.get_value(treeiter, 1)
        modelo = treemodel.get_value(treeiter, 2)
        precio = treemodel.get_value(treeiter, 7)
        
        self.b.get_object("txt_bastidor_add_venta").set_text(str(bastidor))
        self.b.get_object("txt_marca_add_venta").set_text(str(marca))
        self.b.get_object("txt_modelo_add_venta").set_text(str(modelo))
        self.b.get_object("lbl_precio_add_venta").set_text(str(precio))
        
        self.b.get_object("add_venta").show()
    
    
    
    def seleccionar_cliente2(self,w):#BOTON CARGAR CLIENTE EN LA VENTANA DE SELECCION DE CLIENTE AL CREAR UNA VENTA
        self.ocultar("buscar_cliente_add_venta")
        
        #OBTENER DATOS DEL CLIENTE SELECCIONADO EN LA VENTANA DE SELECCION DE CLIENTE
        tree_view = self.b.get_object("treeview5")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        dni = treemodel.get_value(treeiter,0)
        
        result = self.db.execute("SELECT * FROM Cliente WHERE Dni=?",(str(dni),))
        for row in result:
            self.b.get_object("txt_nombre_add_venta").set_text(str(row[1]))
            self.b.get_object("txt_apellidos_add_venta").set_text(str(row[2]))
            self.b.get_object("txt_dni_add_venta").set_text(str(row[0]))
            self.b.get_object("txt_telefono_add_venta").set_text(str(row[3]))
            self.b.get_object("txt_direccion_add_venta").set_text(str(row[4]))
        
        self.b.get_object("txt_nombre_add_venta").set_editable(False)
        self.b.get_object("txt_apellidos_add_venta").set_editable(False)
        self.b.get_object("txt_dni_add_venta").set_editable(False)
        self.b.get_object("txt_telefono_add_venta").set_editable(False)
        self.b.get_object("txt_direccion_add_venta").set_editable(False)
        
        #OBTENER DATOS DE LA SELECCCION DE LA TABLA DE COCHES
        tree_view = self.b.get_object("treeview1")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        bastidor = treemodel.get_value(treeiter, 0)
        marca = treemodel.get_value(treeiter, 1)
        modelo = treemodel.get_value(treeiter, 2)
        precio = treemodel.get_value(treeiter, 7)
        
        self.b.get_object("txt_bastidor_add_venta").set_text(str(bastidor))
        self.b.get_object("txt_marca_add_venta").set_text(str(marca))
        self.b.get_object("txt_modelo_add_venta").set_text(str(modelo))
        self.b.get_object("lbl_precio_add_venta").set_text(str(precio))
        
        self.b.get_object("add_venta").show()
        self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
    
    
    
    def add_venta2(self,w):#BOTON DE ACEPTAR DE LA VENTANA AÑADIR VENTA
        dni = self.b.get_object("txt_dni_add_venta").get_text()
        nombre = self.b.get_object("txt_nombre_add_venta").get_text()
        apellidos = self.b.get_object("txt_apellidos_add_venta").get_text()
        telefono = self.b.get_object("txt_telefono_add_venta").get_text()
        direccion = self.b.get_object("txt_direccion_add_venta").get_text()
        bastidor = self.b.get_object("txt_bastidor_add_venta").get_text()
        precio = self.b.get_object("lbl_precio_add_venta").get_text()
        
        dni = unicode(dni,"utf-8")
        nombre = unicode(nombre,"utf-8")
        apellidos = unicode(apellidos,"utf-8")
        telefono = unicode(telefono,"utf-8")
        direccion = unicode(direccion,"utf-8")
        bastidor = unicode(bastidor,"utf-8")
        p = float(precio)
        fecha = time.strftime("%d/%m/%y")#OBTENER LA FECHA DEL SISTEMA CON EL FORMATO 31/12/17
        
        error = 0
        existe = 0
        
        if not(dni) or not(nombre) or not(apellidos) or not(telefono) or not(direccion):
            self.warning.format_secondary_text("Ningún campo puede estar vacío")
            self.warning.run()
            self.warning.hide()
            error = 1
        
        if error==0:
            result = self.db.execute("SELECT Dni FROM Cliente")
            for row in result:
                if row[0]==dni:#COMPRUEBO SI EL DNI QUE HA SIDO INTRODUCIDO YA EXISTE
                    existe = 1
            
            if existe==0:#EN CASO DE QUE NO EXISTA INSERTARÁ EL NUEVO CLIENTE EN SU TABLA
                try:
                    self.db.execute("INSERT INTO Cliente VALUES(?,?,?,?,?)",(dni,nombre,apellidos,telefono,direccion))
                    self.db.commit()
                except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                    self.warning.format_secondary_text(str(tipoerror))
                    self.warning.run()
                    self.warning.hide()
                else:
                    self.info.format_secondary_text("Nuevo cliente introducido correctamente")
                    self.info.run()
                    self.info.hide()
            
            try:
                self.db.execute("INSERT INTO Venta VALUES(?,?,?,?)",(bastidor,dni,fecha,p))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Venta introducida correctamente")
                self.info.run()
                self.info.hide()
                
                self.b.get_object("txt_nombre_add_venta").set_text("")
                self.b.get_object("txt_apellidos_add_venta").set_text("")
                self.b.get_object("txt_dni_add_venta").set_text("")
                self.b.get_object("txt_telefono_add_venta").set_text("")
                self.b.get_object("txt_direccion_add_venta").set_text("")
                self.b.get_object("txt_bastidor_add_venta").set_text("")
                self.b.get_object("txt_marca_add_venta").set_text("")
                self.b.get_object("txt_modelo_add_venta").set_text("")
                self.b.get_object("lbl_precio_add_venta").set_text("")
                
                self.ocultar("add_venta")
                self.listadni('dni')
                self.listaclientes('clientes')
                self.listaventas('venta')



    def ocultar_add_venta(self,w):#BOTON DE CANCELAR DE LA VENTANA AÑADIR VENTA
        self.b.get_object("txt_nombre_add_venta").set_text("")
        self.b.get_object("txt_apellidos_add_venta").set_text("")
        self.b.get_object("txt_dni_add_venta").set_text("")
        self.b.get_object("txt_telefono_add_venta").set_text("")
        self.b.get_object("txt_direccion_add_venta").set_text("")
        self.b.get_object("txt_bastidor_add_venta").set_text("")
        self.b.get_object("txt_marca_add_venta").set_text("")
        self.b.get_object("txt_modelo_add_venta").set_text("")
        self.b.get_object("lbl_precio_add_venta").set_text("")
        self.ocultar("add_venta")




    def add_revision(self,w):#BOTÓN REVISIÓN DE LA VENTANA PRINCIPAL, ABRE LA VENTANA PARA AÑADIR UNA NUEVA REVISIÓN
        #OBTENER DATOS DE LA SELECCCION DE LA TABLA DE COCHES
        tree_view = self.b.get_object("treeview1")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        bastidor = treemodel.get_value(treeiter, 0)
        marca = treemodel.get_value(treeiter, 1)
        modelo = treemodel.get_value(treeiter, 2)
        
        fecha = time.strftime("%d/%m/%y")#OBTENER LA FECHA DEL SISTEMA CON EL FORMATO 31/12/17
        
        result = self.db.execute("SELECT MAX(N_Revision) FROM Revision")
        for row in result:
            #print(row[0])
            #COMPRUEBO SI EXISTE ALGUNA REVISIÓN
            if row[0]==None:#EN EL CASO DE QUE NO EXISTA LA CONSULTA DEVOLVERÁ NONE Y LE ASIGNO EL VALOR 1
                nrevision = 1
            else:#SI EXISTE TOMO EL VALOR MÁS GRANDE QUE HAYA DEL CAMPO N_Revision PARA LUEGO SUMARLE 1
                nrevision = row[0]
                nrevision = nrevision+1
        
        #print(nrevision)
        
        self.b.get_object("lbl_revision_add_revision").set_text(str(nrevision))
        self.b.get_object("lbl_fecha_add_revision").set_text(str(fecha))
        self.b.get_object("lbl_marca_add_revision").set_text(str(marca))
        self.b.get_object("lbl_modelo_add_revision").set_text(str(modelo))
        self.b.get_object("lbl_bastidor_add_revision").set_text(str(bastidor))
        
        self.b.get_object("add_revision").show()



    def add_revision2(self,w):#BOTÓN DE ACEPTAR DE LA VENTANA AÑADIR REVISIÓN
        frenos = self.b.get_object("chk_frenos_add_revision").get_active()
        aceite = self.b.get_object("chk_aceite_add_revision").get_active()
        filtro = self.b.get_object("chk_filtro_add_revision").get_active()
        
        if frenos==False and aceite==False and filtro==False:#COMPRUEBO SI ESTÁN TODAS LAS OPCIONES DESMARCADAS
            self.warning.format_secondary_text("Debe seleccionar alguna operación")
            self.warning.run()
            self.warning.hide()
        else:#EN CASO CONTRARIO REALIZO LA INSERCIÓN EN LA TABLA REVISIÓN
            nrevision = int(self.b.get_object("lbl_revision_add_revision").get_text())
            fecha = self.b.get_object("lbl_fecha_add_revision").get_text()
            bastidor = self.b.get_object("lbl_bastidor_add_revision").get_text()
            
            #COMPROBACIÓN DE LOS CHECK BUTTONS MARCADOS
            if frenos==True:
                fr = "Si"
            else:
                fr = "No"
            
            if aceite==True:
                ac = "Si"
            else:
                ac = "No"
            
            if filtro==True:
                fi = "Si"
            else:
                fi = "No"
            
            fecha = unicode(fecha,"utf-8")
            fr = unicode(fr,"utf-8")
            ac = unicode(ac,"utf-8")
            fi = unicode(fi,"utf-8")
            bastidor = unicode(bastidor,"utf-8")
            
            try:
                self.db.execute("INSERT INTO Revision VALUES(?,?,?,?,?,?)",(nrevision,fecha,frenos,aceite,filtro,bastidor))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Revisión introducida correctamente")
                self.info.run()
                self.info.hide()
                
                self.ocultar("add_revision")
                self.b.get_object("chk_frenos_add_revision").set_active(False)
                self.b.get_object("chk_aceite_add_revision").set_active(False)
                self.b.get_object("chk_filtro_add_revision").set_active(False)
                self.listarevisiones('revisiones')



    def ocultar_add_revision(self,w):#BOTÓN CANCELAR DE LA VENTANA AÑADIR REVISIÓN
        self.b.get_object("chk_frenos_add_revision").set_active(False)
        self.b.get_object("chk_aceite_add_revision").set_active(False)
        self.b.get_object("chk_filtro_add_revision").set_active(False)
        self.ocultar("add_revision")
    
    
    
    def add_coche(self,w):#BOTON NUEVO DE LA VENTANA PRINCIPAL
        self.b.get_object("add_coche").show()
    
    
    
    def add_coche2(self,w):#BOTON DE ACEPTAR DE LA VENTANA AÑADIR COCHE
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
        
        error = 0
        
        if not(bastidor) or not(marca) or not(modelo) or not(tipo) or not(motor) or not(cv) or not(color) or not(precio):
            self.warning.format_secondary_text("Ningún campo puede estar vacío")
            self.warning.run()
            self.warning.hide()
            error = 1
        else:
            try:
                c = int(cv)
            except ValueError as err:
                self.warning.format_secondary_text("CV no es un número entero")
                self.b.get_object("txt_cv_add_coche").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1

            try:
                p = float(precio)
            except ValueError as err:
                self.warning.format_secondary_text("Precio no es un número real")
                self.b.get_object("txt_precio_add_coche").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1
        
        if error==0:
            try:
                self.db.execute("INSERT INTO Coche('N_Bastidor','Marca','Modelo','Motor','CV','Tipo','Color','Precio') VALUES(?,?,?,?,?,?,?,?)",(bastidor,marca,modelo,motor,c,tipo,color,p))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Coche introducido correctamente")
                self.info.run()
                self.info.hide()

                self.b.get_object("txt_bastidor_add_coche").set_text("")
                self.b.get_object("txt_marca_add_coche").set_text("")
                self.b.get_object("txt_modelo_add_coche").set_text("")
                self.b.get_object("txt_tipo_add_coche").set_text("")
                self.b.get_object("txt_motor_add_coche").set_text("")
                self.b.get_object("txt_cv_add_coche").set_text("")
                self.b.get_object("txt_color_add_coche").set_text("")
                self.b.get_object("txt_precio_add_coche").set_text("")

                self.ocultar("add_coche")
                self.listacoches('tabla_coches')
                self.listacoches2('coches')
    
    
    
    def ocultar_add_coche(self,w):#BOTÓN CANCELAR DE LA VENTANA AÑADIR COCHE
        self.b.get_object("txt_bastidor_add_coche").set_text("")
        self.b.get_object("txt_marca_add_coche").set_text("")
        self.b.get_object("txt_modelo_add_coche").set_text("")
        self.b.get_object("txt_tipo_add_coche").set_text("")
        self.b.get_object("txt_motor_add_coche").set_text("")
        self.b.get_object("txt_cv_add_coche").set_text("")
        self.b.get_object("txt_color_add_coche").set_text("")
        self.b.get_object("txt_precio_add_coche").set_text("")
        self.ocultar("add_coche")
    
    
    
    def mod_coche(self,w):#BOTÓN MODIFICAR DE LA VENTANA PRINCIPAL, MODIFICA EL COCHE SELECCIONADO EN LA TABLA
        #LIMPIAR LAS CAJAS DE TEXTO
        self.b.get_object("txt_bastidor_mod_coche").set_text("")
        self.b.get_object("txt_marca_mod_coche").set_text("")
        self.b.get_object("txt_modelo_mod_coche").set_text("")
        self.b.get_object("txt_tipo_mod_coche").set_text("")
        self.b.get_object("txt_motor_mod_coche").set_text("")
        self.b.get_object("txt_cv_mod_coche").set_text("")
        self.b.get_object("txt_color_mod_coche").set_text("")
        self.b.get_object("txt_precio_mod_coche").set_text("")
        
        #OBTENER DATOS DEL COCHE SELECCIONADO
        tree_view = self.b.get_object("treeview1")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        bastidor = treemodel.get_value(treeiter, 0)
        marca = treemodel.get_value(treeiter, 1)
        modelo = treemodel.get_value(treeiter, 2)
        motor = treemodel.get_value(treeiter, 3)
        cv = treemodel.get_value(treeiter, 4)
        tipo = treemodel.get_value(treeiter, 5)
        color = treemodel.get_value(treeiter, 6)
        precio = treemodel.get_value(treeiter, 7)
        
        #RELLENAR LAS CAJAS DE TEXTO CON LOS DATOS DE COCHE
        self.b.get_object("txt_bastidor_mod_coche").set_text(str(bastidor))
        self.b.get_object("txt_marca_mod_coche").set_text(str(marca))
        self.b.get_object("txt_modelo_mod_coche").set_text(str(modelo))
        self.b.get_object("txt_tipo_mod_coche").set_text(str(tipo))
        self.b.get_object("txt_motor_mod_coche").set_text(str(motor))
        self.b.get_object("txt_cv_mod_coche").set_text(str(cv))
        self.b.get_object("txt_color_mod_coche").set_text(str(color))
        self.b.get_object("txt_precio_mod_coche").set_text(str(precio))
        
        #MOSTRAR LA VENTANA
        self.b.get_object("mod_coche").show()
    
    
    
    def mod_coche2(self,w):#BOTÓN ACEPTAR DE LA VENTANA MODIFICAR COCHE
        bastidor = self.b.get_object("txt_bastidor_mod_coche").get_text()
        marca = self.b.get_object("txt_marca_mod_coche").get_text()
        modelo = self.b.get_object("txt_modelo_mod_coche").get_text()
        motor = self.b.get_object("txt_motor_mod_coche").get_text()
        cv = self.b.get_object("txt_cv_mod_coche").get_text()
        tipo = self.b.get_object("txt_tipo_mod_coche").get_text()
        color = self.b.get_object("txt_color_mod_coche").get_text()
        precio = self.b.get_object("txt_precio_mod_coche").get_text()
        
        bastidor = unicode(bastidor,"utf-8")
        marca = unicode(marca,"utf-8")
        modelo = unicode(modelo,"utf-8")
        motor = unicode(motor,"utf-8")
        tipo = unicode(tipo,"utf-8")
        color = unicode(color,"utf-8")
        
        error = 0
        
        if not(marca) or not(modelo) or not(tipo) or not(motor) or not(cv) or not(color) or not(precio):
            self.warning.format_secondary_text("Ningún campo puede estar vacío")
            self.warning.run()
            self.warning.hide()
            error = 1
        else:
            try:
                c = int(cv)
            except ValueError as err:
                self.warning.format_secondary_text("CV no es un número entero")
                self.b.get_object("txt_cv_mod_coche").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1

            try:
                p = float(precio)
            except ValueError as err:
                self.warning.format_secondary_text("Precio no es un número real")
                self.b.get_object("txt_precio_mod_coche").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1
        
        if error==0:
            try:
                self.db.execute("UPDATE Coche SET Marca=?, Modelo=?, Motor=?, CV=?, Tipo=?, Color=?, Precio=? WHERE N_Bastidor=?;",(marca,modelo,motor,c,tipo,color,p,bastidor))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Coche modificado correctamente")
                self.info.run()
                self.info.hide()

                self.listacoches('tabla_coches')
                self.listacoches2('coches')
                self.listarevisiones('revisiones')
                self.listaventas('venta')

                self.ocultar("mod_coche")
                self.b.get_object("btn_add_venta_main").set_sensitive(False)
                self.b.get_object("btn_add_revision_main").set_sensitive(False)
                self.b.get_object("btn_mod_coche_main").set_sensitive(False)
                self.b.get_object("btn_del_coche_main").set_sensitive(False)
    
    
    
    def borrar_coche(self,w):#BOTÓN ELIMINAR DE LA VENTANA PRINCIPAL, ELIMINA EL COCHE SELECCIONADO EN LA TABLA
        self.mensajeborrar.format_secondary_text("¿Desea eliminar el coche?")
        respuesta = self.mensajeborrar.run()
        #print(respuesta)
        self.mensajeborrar.hide()
        
        if respuesta==-5:
            tree_view = self.b.get_object("treeview1")
            tree_sel = tree_view.get_selection()
            (treemodel, treeiter) = tree_sel.get_selected()
            bastidor = treemodel.get_value(treeiter, 0)#El número es la columna de la que va a obtener el dato, 0 es la primera columna
            #print(bastidor)
            
            try:
                self.db.execute("DELETE FROM Coche WHERE N_Bastidor=?;",(str(bastidor),))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Coche eliminado correctamente")
                self.info.run()
                self.info.hide()
                
                self.listacoches('tabla_coches')
                self.listacoches2('coches')
                self.listarevisiones('revisiones')
                self.listaventas('venta')
                
                self.b.get_object("btn_add_venta_main").set_sensitive(False)
                self.b.get_object("btn_add_revision_main").set_sensitive(False)
                self.b.get_object("btn_mod_coche_main").set_sensitive(False)
                self.b.get_object("btn_del_coche_main").set_sensitive(False)
    
    
    
    def ocultar_mod_coche(self,w):
        self.ocultar("mod_coche")
    
    
    
    def mod_revision(self,w):#BOTÓN MODIFICAR DE LA PESTAÑA DE REVISIONES
        #LIMPIAR VENTANA
        self.b.get_object("lbl_revision_mod_revision").set_text("")
        self.b.get_object("lbl_fecha_mod_revision").set_text("")
        self.b.get_object("lbl_marca_mod_revision").set_text("")
        self.b.get_object("lbl_modelo_mod_revision").set_text("")
        self.b.get_object("lbl_bastidor_mod_revision").set_text("")
        self.b.get_object("chk_frenos_mod_revision").set_active(False)
        self.b.get_object("chk_aceite_mod_revision").set_active(False)
        self.b.get_object("chk_filtro_mod_revision").set_active(False)
        
        #OBTENER DATOS
        nrevision = self.b.get_object("lbl_numero_revision_main").get_text()
        fecha = self.b.get_object("lbl_fecha_revision_main").get_text()
        bastidor = self.b.get_object("lbl_bastidor_revision_main").get_text()
        marca = self.b.get_object("lbl_marca_revision_main").get_text()
        modelo = self.b.get_object("lbl_modelo_revision_main").get_text()
        frenos = self.b.get_object("lbl_frenos_revision_main").get_text()
        filtro = self.b.get_object("lbl_filtro_revision_main").get_text()
        aceite = self.b.get_object("lbl_aceite_revision_main").get_text()
        
        #RELLENAR VENTANA CON LOS DATOS
        self.b.get_object("lbl_revision_mod_revision").set_text(str(nrevision))
        self.b.get_object("lbl_fecha_mod_revision").set_text(str(fecha))
        self.b.get_object("lbl_marca_mod_revision").set_text(str(marca))
        self.b.get_object("lbl_modelo_mod_revision").set_text(str(modelo))
        self.b.get_object("lbl_bastidor_mod_revision").set_text(str(bastidor))
        
        if frenos=="Sí":
            self.b.get_object("chk_frenos_mod_revision").set_active(True)
        else:
            self.b.get_object("chk_frenos_mod_revision").set_active(False)
        
        if filtro=="Sí":
            self.b.get_object("chk_filtro_mod_revision").set_active(True)
        else:
            self.b.get_object("chk_filtro_mod_revision").set_active(False)
        
        if aceite=="Sí":
            self.b.get_object("chk_aceite_mod_revision").set_active(True)
        else:
            self.b.get_object("chk_aceite_mod_revision").set_active(False)
        
        self.b.get_object("mod_revision").show()
    
    
    
    def mod_revision2(self,w):#BOTÓN ACEPTAR DE LA VENTANA MODIFICAR REVISIÓN
        frenos = self.b.get_object("chk_frenos_mod_revision").get_active()
        aceite = self.b.get_object("chk_aceite_mod_revision").get_active()
        filtro = self.b.get_object("chk_filtro_mod_revision").get_active()
        
        if frenos==False and aceite==False and filtro==False:#COMPRUEBO SI ESTÁN TODAS LAS OPCIONES DESMARCADAS
            self.warning.format_secondary_text("Debe seleccionar alguna operación")
            self.warning.run()
            self.warning.hide()
        else:#EN CASO CONTRARIO REALIZO LA ACTUALIZACIÓN EN LA TABLA REVISIÓN
            nrevision = int(self.b.get_object("lbl_revision_mod_revision").get_text())
            
            #COMPROBACIÓN DE LOS CHECK BUTTONS MARCADOS
            if frenos==True:
                fr = "Sí"
            else:
                fr = "No"
            
            if aceite==True:
                ac = "Sí"
            else:
                ac = "No"
            
            if filtro==True:
                fi = "Sí"
            else:
                fi = "No"
            
            fr = unicode(fr,"utf-8")
            ac = unicode(ac,"utf-8")
            fi = unicode(fi,"utf-8")
            
            try:
                self.db.execute("UPDATE Revision SET Frenos=?, Aceite=?, Filtro=? WHERE N_Revision=?",(fr,ac,fi,nrevision))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Revisión modificada correctamente")
                self.info.run()
                self.info.hide()
                
                self.ocultar("mod_revision")
                
                self.b.get_object("lbl_numero_revision_main").set_text("")
                self.b.get_object("lbl_fecha_revision_main").set_text("")
                self.b.get_object("lbl_bastidor_revision_main").set_text("")
                self.b.get_object("lbl_marca_revision_main").set_text("")
                self.b.get_object("lbl_modelo_revision_main").set_text("")
                self.b.get_object("lbl_frenos_revision_main").set_text("")
                self.b.get_object("lbl_filtro_revision_main").set_text("")
                self.b.get_object("lbl_aceite_revision_main").set_text("")
                
                self.b.get_object("btn_mod_revision_main").set_sensitive(False)
                self.b.get_object("btn_del_revision_main").set_sensitive(False)
                
                self.listarevisiones('revisiones')

    
    
    def borrar_revision(self,w):
        self.mensajeborrar.format_secondary_text("¿Desea eliminar la revisión?")
        respuesta = self.mensajeborrar.run()
        #print(respuesta)
        self.mensajeborrar.hide()
        
        if respuesta==-5:
            seleccion = self.b.get_object("treeview2").get_selection()
            (modelo, pathlist) = seleccion.get_selected_rows()
            for path in pathlist :
                tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
                nrevision = modelo.get_value(tree_iter,0)
            
            try:
                self.db.execute("DELETE FROM Revision WHERE N_Revision=?;",(int(nrevision),))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Revisión eliminada correctamente")
                self.info.run()
                self.info.hide()
                
                self.listarevisiones('revisiones')
                
                self.b.get_object("lbl_numero_revision_main").set_text("")
                self.b.get_object("lbl_fecha_revision_main").set_text("")
                self.b.get_object("lbl_bastidor_revision_main").set_text("")
                self.b.get_object("lbl_marca_revision_main").set_text("")
                self.b.get_object("lbl_modelo_revision_main").set_text("")
                self.b.get_object("lbl_frenos_revision_main").set_text("")
                self.b.get_object("lbl_filtro_revision_main").set_text("")
                self.b.get_object("lbl_aceite_revision_main").set_text("")
                
                self.b.get_object("btn_mod_revision_main").set_sensitive(False)
                self.b.get_object("btn_del_revision_main").set_sensitive(False)



    def borrar_venta(self,w):
        self.mensajeborrar.format_secondary_text("¿Desea eliminar la venta?")
        respuesta = self.mensajeborrar.run()
        #print(respuesta)
        self.mensajeborrar.hide()
        
        if respuesta==-5:
            seleccion = self.b.get_object("treeview3").get_selection()
            (modelo, pathlist) = seleccion.get_selected_rows()
            for path in pathlist :
                tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
                bastidor = modelo.get_value(tree_iter,0)
                dni = modelo.get_value(tree_iter,1)
            
            try:
                self.db.execute("DELETE FROM Venta WHERE N_Bastidor=? AND Dni=?;",(bastidor,dni))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Venta eliminada correctamente")
                self.info.run()
                self.info.hide()
                
                self.listaventas('venta')
                
                self.b.get_object("lbl_fecha_venta_main").set_text("")
                self.b.get_object("lbl_nombre_ventas_main").set_text("")
                self.b.get_object("lbl_apellidos_ventas_main").set_text("")
                self.b.get_object("lbl_dni_ventas_main").set_text("")
                self.b.get_object("lbl_coche_ventas_main").set_text("")
                self.b.get_object("lbl_precio_ventas_main").set_text("")
                
                self.b.get_object("btn_mod_venta_main").set_sensitive(False)
                self.b.get_object("btn_del_venta_main").set_sensitive(False)
######################################VOY POR AQUÍ#############################################################################################################################################################################    

    
    
    def ocultar_mod_revision(self,w):
        self.ocultar("mod_revision")
    
    
    
    def message_mod_venta(self,w):
        self.b.get_object("message_mod_venta").show()
    
    
    
    def mod_venta(self,w):
        self.ocultar("message_mod_venta")
        self.b.get_object("mod_venta").show()
    
    
    
    def ocultar_mod_venta(self,w):
        self.ocultar("mod_venta")
    
    
    
    def mod_cliente(self,w):#BOTÓN MODIFICAR CLIENTE DE LA PESTAÑA CLIENTES
        #LIMPIAR CAJAS
        self.b.get_object("txt_nombre_mod_cliente").set_text("")
        self.b.get_object("txt_apellidos_mod_cliente").set_text("")
        self.b.get_object("txt_dni_mod_cliente").set_text("")
        self.b.get_object("txt_telefono_mod_cliente").set_text("")
        self.b.get_object("txt_direccion_mod_cliente").set_text("")
        
        #OBTENER DATOS DE LAS ETIQUETAS
        dni = self.b.get_object("lbl_dni_clientes_main").get_text()
        nombre = self.b.get_object("lbl_nombre_clientes_main").get_text()
        apellidos = self.b.get_object("lbl_apellidos_clientes_main").get_text()
        telefono = self.b.get_object("lbl_telefono_clientes_main").get_text()
        direccion = self.b.get_object("lbl_direccion_clientes_main").get_text()
        
        #RELLENAR CAJAS DE TEXTO CON LOS DATOS
        self.b.get_object("txt_nombre_mod_cliente").set_text(nombre)
        self.b.get_object("txt_apellidos_mod_cliente").set_text(apellidos)
        self.b.get_object("txt_dni_mod_cliente").set_text(dni)
        self.b.get_object("txt_telefono_mod_cliente").set_text(telefono)
        self.b.get_object("txt_direccion_mod_cliente").set_text(direccion)
        
        self.b.get_object("mod_cliente").show()
    
    
    
    def mod_cliente2(self,w):#BOTÓN ACEPTAR DE LA VENTANA MODIFICAR CLIENTE
        nombre = self.b.get_object("txt_nombre_mod_cliente").get_text()
        apellidos = self.b.get_object("txt_apellidos_mod_cliente").get_text()
        dni = self.b.get_object("txt_dni_mod_cliente").get_text()
        telefono = self.b.get_object("txt_telefono_mod_cliente").get_text()
        direccion = self.b.get_object("txt_direccion_mod_cliente").get_text()
        
        nombre = unicode(nombre,"utf-8")
        apellidos = unicode(apellidos,"utf-8")
        dni = unicode(dni,"utf-8")
        telefono = unicode(telefono,"utf-8")
        direccion = unicode(direccion,"utf-8")
        
        error = 0
        
        if not(nombre) or not(apellidos) or not(telefono) or not(direccion):
            self.warning.format_secondary_text("Ningún campo puede estar vacío")
            self.warning.run()
            self.warning.hide()
            error = 1
        
        if error==0:
            try:
                self.db.execute("UPDATE Cliente SET Nombre=?, Apellidos=?, Telefono=?, Domicilio=? WHERE Dni=?;",(nombre,apellidos,telefono,direccion,dni))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Cliente modificado correctamente")
                self.info.run()
                self.info.hide()
                
                self.listadni('dni')
                self.listaclientes('clientes')
                
                self.ocultar("mod_cliente")
                self.b.get_object("lbl_dni_clientes_main").set_text("")
                self.b.get_object("lbl_nombre_clientes_main").set_text("")
                self.b.get_object("lbl_apellidos_clientes_main").set_text("")
                self.b.get_object("lbl_telefono_clientes_main").set_text("")
                self.b.get_object("lbl_direccion_clientes_main").set_text("")
                self.b.get_object("btn_mod_clientes_main").set_sensitive(False)
                self.b.get_object("btn_del_clientes_main").set_sensitive(False)
    
    
    
    def borrar_cliente(self,w):
        self.mensajeborrar.format_secondary_text("¿Desea eliminar el cliente?")
        respuesta = self.mensajeborrar.run()
        #print(respuesta)
        self.mensajeborrar.hide()
        
        if respuesta==-5:
            seleccion = self.b.get_object("treeview4").get_selection()
            (modelo, pathlist) = seleccion.get_selected_rows()
            for path in pathlist :
                tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
                dni = modelo.get_value(tree_iter,0)
            
            try:
                self.db.execute("DELETE FROM Cliente WHERE Dni=?;",(str(dni),))
                self.db.commit()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Cliente eliminado correctamente")
                self.info.run()
                self.info.hide()
                
                self.listadni('dni')
                self.listaclientes('clientes')
                self.listaventas('venta')
                
                self.b.get_object("lbl_dni_clientes_main").set_text("")
                self.b.get_object("lbl_nombre_clientes_main").set_text("")
                self.b.get_object("lbl_apellidos_clientes_main").set_text("")
                self.b.get_object("lbl_telefono_clientes_main").set_text("")
                self.b.get_object("lbl_direccion_clientes_main").set_text("")
                self.b.get_object("btn_mod_clientes_main").set_sensitive(False)
                self.b.get_object("btn_del_clientes_main").set_sensitive(False)
    
    
    
    def ocultar_mod_cliente(self,w):
        self.ocultar("mod_cliente")
    
    
    
    def on_destroy(self, w, *signals):
        # return True --> no cierra
        # return False --> cierra
        print("Cerrando BBDD")
        self.db.commit()
        self.db.close()            
        gtk.main_quit()


    #FUNCIONES AUXILIARES########################################################################################
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
        #BOTONES
        self.b.get_object("btn_add_venta_main").set_sensitive(False)
        self.b.get_object("btn_add_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_coche_main").set_sensitive(False)
        self.b.get_object("btn_del_coche_main").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
        self.b.get_object("btn_mod_revision_main").set_sensitive(False)
        self.b.get_object("btn_del_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_clientes_main").set_sensitive(False)
        self.b.get_object("btn_del_clientes_main").set_sensitive(False)
        self.b.get_object("btn_mod_venta_main").set_sensitive(False)
        self.b.get_object("btn_del_venta_main").set_sensitive(False)
        #ETIQUETAS DE LA PESTAÑA REVISIONES
        self.b.get_object("lbl_numero_revision_main").set_text("")
        self.b.get_object("lbl_fecha_revision_main").set_text("")
        self.b.get_object("lbl_bastidor_revision_main").set_text("")
        self.b.get_object("lbl_marca_revision_main").set_text("")
        self.b.get_object("lbl_modelo_revision_main").set_text("")
        self.b.get_object("lbl_frenos_revision_main").set_text("")
        self.b.get_object("lbl_filtro_revision_main").set_text("")
        self.b.get_object("lbl_aceite_revision_main").set_text("")
        #ETIQUETAS DE LA PESTAÑA CLIENTES
        self.b.get_object("lbl_dni_clientes_main").set_text("")
        self.b.get_object("lbl_nombre_clientes_main").set_text("")
        self.b.get_object("lbl_apellidos_clientes_main").set_text("")
        self.b.get_object("lbl_telefono_clientes_main").set_text("")
        self.b.get_object("lbl_direccion_clientes_main").set_text("")
        #ETIQUETAS DE LA PESTAÑA VENTAS
        self.b.get_object("lbl_fecha_venta_main").set_text("")
        self.b.get_object("lbl_nombre_ventas_main").set_text("")
        self.b.get_object("lbl_apellidos_ventas_main").set_text("")
        self.b.get_object("lbl_dni_ventas_main").set_text("")
        self.b.get_object("lbl_coche_ventas_main").set_text("")
        self.b.get_object("lbl_precio_ventas_main").set_text("")
    
    
    
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
    
    
    
    def on_boton_coche(self,treeview,evento):
        botonpulsado = evento.button
        if botonpulsado==1:
            self.b.get_object("btn_add_venta_main").set_sensitive(True)
            self.b.get_object("btn_add_revision_main").set_sensitive(True)
            self.b.get_object("btn_mod_coche_main").set_sensitive(True)
            self.b.get_object("btn_del_coche_main").set_sensitive(True)
    
    
    
    def on_boton_cliente(self,treeview,evento):
        botonpulsado = evento.button
        if botonpulsado==1:
            self.b.get_object("btn_seleccionar_cliente1").set_sensitive(True)
    
    
    
    def on_btn_dni(self,treeview,evento):
        botonpulsado = evento.button
        if botonpulsado==1:
            seleccion = self.b.get_object("treeview4").get_selection()
            (modelo, pathlist) = seleccion.get_selected_rows()
            for path in pathlist :
                tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
                dni = modelo.get_value(tree_iter,0)
                #print(dni)
            
            result = self.db.execute("SELECT * FROM Cliente WHERE Dni=?;",(dni,))
            for row in result:
                self.b.get_object("lbl_dni_clientes_main").set_text(str(row[0]))
                self.b.get_object("lbl_nombre_clientes_main").set_text(str(row[1]))
                self.b.get_object("lbl_apellidos_clientes_main").set_text(str(row[2]))
                self.b.get_object("lbl_telefono_clientes_main").set_text(str(row[3]))
                self.b.get_object("lbl_direccion_clientes_main").set_text(str(row[4]))
            
            self.b.get_object("btn_mod_clientes_main").set_sensitive(True)
            self.b.get_object("btn_del_clientes_main").set_sensitive(True)
    
    
    
    def on_btn_venta(self,treeview,evento):
        botonpulsado = evento.button
        if botonpulsado==1:
            seleccion = self.b.get_object("treeview3").get_selection()
            (modelo, pathlist) = seleccion.get_selected_rows()
            for path in pathlist :
                tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
                bastidor = modelo.get_value(tree_iter, 0)
                dni = modelo.get_value(tree_iter, 1)
            
            result = self.db.execute("SELECT v.Fecha,cl.Nombre,cl.Apellidos,cl.Dni,co.Marca || ' ' || co.Modelo AS Coche,co.Precio FROM Venta AS v,Coche AS co,Cliente AS cl WHERE v.N_Bastidor=? AND v.Dni=? AND v.N_Bastidor=co.N_Bastidor AND v.Dni=cl.Dni;",(bastidor,dni))
            for row in result:
                self.b.get_object("lbl_fecha_venta_main").set_text(str(row[0]))
                self.b.get_object("lbl_nombre_ventas_main").set_text(str(row[1]))
                self.b.get_object("lbl_apellidos_ventas_main").set_text(str(row[2]))
                self.b.get_object("lbl_dni_ventas_main").set_text(str(row[3]))
                self.b.get_object("lbl_coche_ventas_main").set_text(str(row[4]))
                self.b.get_object("lbl_precio_ventas_main").set_text(str(row[5]))
            
            self.b.get_object("btn_mod_venta_main").set_sensitive(True)
            self.b.get_object("btn_del_venta_main").set_sensitive(True)
    
    
    
    def on_btn_revision(self,treeview,evento):
        botonpulsado = evento.button
        if botonpulsado==1:
            seleccion = self.b.get_object("treeview2").get_selection()
            (modelo, pathlist) = seleccion.get_selected_rows()
            for path in pathlist :
                tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
                nrevision = modelo.get_value(tree_iter, 0)
            
            result = self.db.execute("SELECT r.N_Revision,r.Fecha,r.N_Bastidor,c.Marca,c.Modelo,r.Frenos,r.Filtro,r.Aceite FROM Revision AS r, Coche AS c WHERE N_Revision=? AND r.N_Bastidor=c.N_Bastidor;",(nrevision,))
            for row in result:
                self.b.get_object("lbl_numero_revision_main").set_text(str(row[0]))
                self.b.get_object("lbl_fecha_revision_main").set_text(str(row[1]))
                self.b.get_object("lbl_bastidor_revision_main").set_text(str(row[2]))
                self.b.get_object("lbl_marca_revision_main").set_text(str(row[3]))
                self.b.get_object("lbl_modelo_revision_main").set_text(str(row[4]))
                self.b.get_object("lbl_frenos_revision_main").set_text(str(row[5]))
                self.b.get_object("lbl_filtro_revision_main").set_text(str(row[6]))
                self.b.get_object("lbl_aceite_revision_main").set_text(str(row[7]))
            
            self.b.get_object("btn_mod_revision_main").set_sensitive(True)
            self.b.get_object("btn_del_revision_main").set_sensitive(True)
    
    
    
    def comboMarcas(self,w):#################MIRAR MÁS TARDE##################################
        model = self.b.get_object("comboMarca")
        result = self.db.execute("SELECT DISTINCT Marca FROM Coche;")
        for row in result:
            model.append(str(row[0]))
        
        cell = self.b.get_object("cellrenderertext1")
        combo = self.b.get_object("combo_marca")
        combo.set_model(model=model)
        combo.pack_start(cell)
        combo.set_attributes(cell, text=0)
    
    
    
    def activaLabel(self, notebook, page, page_num):
        #BOTONES
        self.b.get_object("btn_add_venta_main").set_sensitive(False)
        self.b.get_object("btn_add_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_coche_main").set_sensitive(False)
        self.b.get_object("btn_del_coche_main").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
        self.b.get_object("btn_mod_revision_main").set_sensitive(False)
        self.b.get_object("btn_del_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_clientes_main").set_sensitive(False)
        self.b.get_object("btn_del_clientes_main").set_sensitive(False)
        self.b.get_object("btn_mod_venta_main").set_sensitive(False)
        self.b.get_object("btn_del_venta_main").set_sensitive(False)
        #ETIQUETAS DE LA PESTAÑA REVISIONES
        self.b.get_object("lbl_numero_revision_main").set_text("")
        self.b.get_object("lbl_fecha_revision_main").set_text("")
        self.b.get_object("lbl_bastidor_revision_main").set_text("")
        self.b.get_object("lbl_marca_revision_main").set_text("")
        self.b.get_object("lbl_modelo_revision_main").set_text("")
        self.b.get_object("lbl_frenos_revision_main").set_text("")
        self.b.get_object("lbl_filtro_revision_main").set_text("")
        self.b.get_object("lbl_aceite_revision_main").set_text("")
        #ETIQUETAS DE LA PESTAÑA CLIENTES
        self.b.get_object("lbl_dni_clientes_main").set_text("")
        self.b.get_object("lbl_nombre_clientes_main").set_text("")
        self.b.get_object("lbl_apellidos_clientes_main").set_text("")
        self.b.get_object("lbl_telefono_clientes_main").set_text("")
        self.b.get_object("lbl_direccion_clientes_main").set_text("")
        #ETIQUETAS DE LA PESTAÑA VENTAS
        self.b.get_object("lbl_fecha_venta_main").set_text("")
        self.b.get_object("lbl_nombre_ventas_main").set_text("")
        self.b.get_object("lbl_apellidos_ventas_main").set_text("")
        self.b.get_object("lbl_dni_ventas_main").set_text("")
        self.b.get_object("lbl_coche_ventas_main").set_text("")
        self.b.get_object("lbl_precio_ventas_main").set_text("")


if __name__ == "__main__":
    v = Concesionario() #Llama a la Clase
    gtk.main() #Ejecuta el programa
    