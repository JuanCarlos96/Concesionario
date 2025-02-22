#!/usr/bin/env python
#vim: set encoding=utf-8
from basededatos import *
import sys,os
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
        self.res = self.db.execute("SELECT * FROM sqlite_master WHERE name='Venta'")
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
        "on_btn_mod_cliente_clicked" : self.mod_venta_cliente,
        "on_btn_mod_coche_clicked" : self.mod_venta_coche,
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
        "on_btn_del_venta_main_clicked" : self.borrar_venta,
        "on_treeview6_button_press_event" : self.on_boton_cliente2,
        "on_btn_aceptar_mod_venta_clicked" : self.mod_venta2,
        "on_combo_coche_changed" : self.combo_coche_changed,
        "on_btn_buscar_coche_main_clicked" : self.busca_coche_tipo,
        "on_abre_calendario_clicked" : self.abrir_calendario,
        "on_seleccionar_fecha_clicked" : self.seleccionar_fecha,
        "on_treeview6_row_activated" : self.on_treeview6_row_activated,
        "on_treeview5_row_activated" : self.on_treeview5_row_activated,
        "on_treeview7_row_activated" : self.on_treeview7_row_activated,
        "on_treeview1_row_activated" : self.on_treeview1_row_activated,
        "on_treeview2_row_activated" : self.on_treeview2_row_activated,
        "on_treeview3_row_activated" : self.on_treeview3_row_activated,
        "on_treeview4_row_activated" : self.on_treeview4_row_activated,
        "on_treeview4_button_press_event" : self.on_treeview4_button_press_event,
        "on_treeview2_button_press_event" : self.on_treeview2_button_press_event,
        "on_treeview3_button_press_event" : self.on_treeview3_button_press_event,
        "on_combo_cliente1_changed" : self.on_combo_cliente1_changed,
        "on_btn_buscar_cliente1_clicked" : self.on_btn_buscar_cliente1_clicked,
        "on_combo_cliente2_changed" : self.on_combo_cliente2_changed,
        "on_btn_buscar_cliente2_clicked" : self.on_btn_buscar_cliente2_clicked,
        "on_btn_buscar_coche_clicked" : self.on_btn_buscar_coche_clicked,
        "on_combo_coche2_changed" : self.on_combo_coche2_changed,
        "on_treeview7_button_press_event" : self.on_treeview7_button_press_event,
        "on_Acerca_de_activate" : self.on_Acerca_de_activate,
        "on_btnAcercaDe_activate" : self.on_btnAcercaDe_activate,
        "on_btnReiniciarBusqueda_clicked" : self.on_btnReiniciarBusqueda_clicked,
        "on_combo_motor_changed" : self.on_combo_motor_changed,
        "on_combo_marca_changed" : self.on_combo_marca_changed,
        "on_treeview1_key_press_event" : self.on_treeview1_key_press_event,
        "on_treeview2_key_press_event" : self.on_treeview2_key_press_event,
        "on_treeview3_key_press_event" : self.on_treeview3_key_press_event,
        "on_treeview4_key_press_event" : self.on_treeview4_key_press_event,
        "on_btn_sel_imagen_clicked" : self.on_btn_sel_imagen_clicked,
        "on_btn_sel_imagen1_clicked" : self.on_btn_sel_imagen1_clicked,
        "on_treeview1_button_release_event" : self.on_treeview1_button_release_event,
        "on_txt_combo_coche_main_key_release_event" : self.on_txt_combo_coche_main_key_release_event,
        "on_txt_combo_cliente1_key_release_event" : self.on_txt_combo_cliente1_key_release_event,
        "on_txt_combo_cliente2_key_release_event" : self.on_txt_combo_cliente2_key_release_event,
        "on_txt_combo_coche_key_release_event" : self.on_txt_combo_coche_key_release_event,
        "on_manual_activate" : self.on_manual_activate})
        
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
        
        self.blob = None
        
        #FILTRO DEL FILECHOOSER
        selfichero=self.b.get_object("filechooserdialog1")
        filtro=self.b.get_object("filefilter1")
        filtro.set_name("Imágenes JPG")
        filtro.add_pattern("*.jpg")
        selfichero.add_filter(filtro)
        
        self.warning = self.b.get_object("warning")
        self.info = self.b.get_object("info")
        self.mensajeborrar = self.b.get_object("mensajeborrar")
        
        self.b.get_object("txt_combo_coche_main").set_editable(False)
        self.b.get_object("btn_buscar_coche_main").set_sensitive(False)
        self.b.get_object("btn_buscar_coche").set_sensitive(False)
        self.b.get_object("btn_buscar_cliente1").set_sensitive(False)
        self.b.get_object("btn_buscar_cliente2").set_sensitive(False)
        self.b.get_object("btn_add_venta_main").set_sensitive(False)
        self.b.get_object("btn_add_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_coche_main").set_sensitive(False)
        self.b.get_object("btn_del_coche_main").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente2").set_sensitive(False)
        self.b.get_object("btn_mod_revision_main").set_sensitive(False)
        self.b.get_object("btn_del_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_clientes_main").set_sensitive(False)
        self.b.get_object("btn_del_clientes_main").set_sensitive(False)
        self.b.get_object("btn_mod_venta_main").set_sensitive(False)
        self.b.get_object("btn_del_venta_main").set_sensitive(False)
        
        self.b.get_object("main").connect("delete-event", self.on_destroy)
        self.b.get_object("add_coche").connect("delete-event",self.on_destroy2)
        self.b.get_object("add_revision").connect("delete-event",self.on_destroy2)
        self.b.get_object("add_venta").connect("delete-event",self.on_destroy2)
        self.b.get_object("calendario").connect("delete-event",self.on_destroy2)
        self.b.get_object("buscar_cliente_add_venta").connect("delete-event",self.on_destroy2)
        self.b.get_object("buscar_cliente_mod_venta").connect("delete-event",self.on_destroy2)
        self.b.get_object("buscar_coche_mod_venta").connect("delete-event",self.on_destroy2)
        self.b.get_object("message_mod_venta").connect("delete-event",self.on_destroy2)
        self.b.get_object("mod_cliente").connect("delete-event",self.on_destroy2)
        self.b.get_object("mod_coche").connect("delete-event",self.on_destroy2)
        self.b.get_object("mod_revision").connect("delete-event",self.on_destroy2)
        self.b.get_object("mod_venta").connect("delete-event",self.on_destroy2)
        self.b.get_object("filechooserdialog1").connect("delete-event",self.on_destroy2)
        
        #RELLENAR LOS COMBOBOX DE LOS FILTROS: MARCA Y MOTOR
        self.b.get_object("combo_marca").get_model().clear()
        marcas = self.db.execute("SELECT DISTINCT Marca FROM Coche;")
        for marca in marcas:
            self.b.get_object("combo_marca").append_text(marca[0])

        self.b.get_object("combo_motor").get_model().clear()
        motores = self.db.execute("SELECT DISTINCT Motor FROM Coche;")
        for motor in motores:
            self.b.get_object("combo_motor").append_text(motor[0])
        
        #Toma el nombre de la ventana a mostrar
        self.b.get_object("main").show()
    
    #FUNCIONES PRINCIPALES######################################################################################
    def buscar_cliente(self,w):#BOTON DE VENTA EN LA VENTANA PRINCIPAL, ABRE LA VENTANA DE SELECCION DE CLIENTE PARA CREAR UNA VENTA
        self.b.get_object("txt_nombre_add_venta").set_text("")
        self.b.get_object("txt_apellidos_add_venta").set_text("")
        self.b.get_object("txt_dni_add_venta").set_text("")
        self.b.get_object("txt_telefono_add_venta").set_text("")
        self.b.get_object("txt_direccion_add_venta").set_text("")
        self.b.get_object("txt_bastidor_add_venta").set_text("")
        self.b.get_object("txt_marca_add_venta").set_text("")
        self.b.get_object("txt_modelo_add_venta").set_text("")
        self.b.get_object("lbl_precio_add_venta").set_text("")
        
        self.b.get_object("combo_cliente1").set_active(-1)
        self.b.get_object("txt_combo_cliente1").set_text("")
        self.b.get_object("txt_combo_cliente1").set_editable(False)
        self.b.get_object("btn_buscar_cliente1").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
        self.b.get_object("buscar_cliente_add_venta").show()
        self.listaclientes('clientes')
    
    
    
    def buscar_cliente2(self,w):#BOTON DE BUSCAR DNI EN LA VENTANA DE MODIFICAR VENTA, ABRE LA VENTANA DE SELECCION DE CLIENTE PARA MODIFICAR UNA VENTA
        self.b.get_object("combo_cliente2").set_active(-1)
        self.b.get_object("txt_combo_cliente2").set_text("")
        self.b.get_object("txt_combo_cliente2").set_editable(False)
        self.b.get_object("btn_buscar_cliente2").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente2").set_sensitive(False)
        self.b.get_object("buscar_cliente_mod_venta").show()
        self.listaclientes('clientes')
    
    
    
    def buscar_bastidor(self,w):#BOTON DE BUSCAR BASTIDOR EN LA VENTANA DE MODIFICAR VENTA, ABRE LA VENTANA DE SELECCION DE COCHE PARA MODIFICAR UNA VENTA
        self.b.get_object("combo_coche2").set_active(-1)
        self.b.get_object("txt_combo_coche").set_text("")
        self.b.get_object("txt_combo_coche").set_editable(False)
        self.b.get_object("btn_buscar_coche").set_sensitive(False)
        self.b.get_object("btn_seleccionar_coche").set_sensitive(False)
        self.b.get_object("buscar_coche_mod_venta").show()
        self.listacoches2('coches')
    
    
    
    def seleccionar_cliente(self,w):#BOTON DE CARGAR CLIENTE EN LA VENTANA DE SELECCION DE CLIENTE AL MODIFICAR UNA VENTA
        tree_view = self.b.get_object("treeview6")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        dni = treemodel.get_value(treeiter,0)
        
        result = self.db.execute("SELECT Dni FROM Cliente WHERE Dni=?",(str(dni),))
        for row in result:
            self.b.get_object("txt_dni_mod_venta").set_text(str(row[0]))
        
        self.ocultar("buscar_cliente_mod_venta")
        self.b.get_object("mod_venta").show()

    
        
    def seleccionar_coche(self,w):#BOTÓN CARGAR COCHE EN LA VENTANA DE SELECCIÓN DE COCHE AL MODIFICAR UNA VENTA
        tree_view = self.b.get_object("treeview7")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        bastidor = treemodel.get_value(treeiter,0)
        
        result = self.db.execute("SELECT N_Bastidor, Precio FROM Coche WHERE N_Bastidor=?",(str(bastidor),))
        for row in result:
            self.b.get_object("txt_bastidor_mod_venta").set_text(str(row[0]))
            self.b.get_object("txt_precio_mod_venta").set_text(str(row[1]))
        
        self.ocultar("buscar_coche_mod_venta")
        self.b.get_object("mod_venta").show()
    
    
    
    def add_venta(self,w):#BOTON DE NUEVO CLIENTE EN LA SELECCION DEL CLIENTE PARA HACER UNA VENTA NUEVA
        self.ocultar("buscar_cliente_add_venta")
        
        fecha = time.strftime("%d/%m/%Y")#OBTENER LA FECHA DEL SISTEMA CON EL FORMATO 31/12/2017
        self.b.get_object("lbl_fecha_add_venta").set_text(fecha)
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
        
        fecha = time.strftime("%d/%m/%Y")#OBTENER LA FECHA DEL SISTEMA CON EL FORMATO 31/12/2017
        self.b.get_object("lbl_fecha_add_venta").set_text(fecha)
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
        
        dni = unicode(dni.upper(),"utf-8")
        nombre = unicode(nombre,"utf-8")
        apellidos = unicode(apellidos,"utf-8")
        telefono = unicode(telefono,"utf-8")
        direccion = unicode(direccion,"utf-8")
        bastidor = unicode(bastidor,"utf-8")
        p = float(precio)
        fecha = time.strftime("%d/%m/%Y")#OBTENER LA FECHA DEL SISTEMA CON EL FORMATO 31/12/2017
        
        error = 0
        existe = 0
        
        if not(dni) or not(nombre) or not(apellidos) or not(telefono) or not(direccion):
            self.warning.format_secondary_text("Ningún campo puede estar vacío")
            self.warning.run()
            self.warning.hide()
            error = 1
        else:
            if len(dni)!=9:#COMPROBACIÓN DEL FORMATO DEL DNI
                self.warning.format_secondary_text("DNI no tiene el formato correcto")
                self.b.get_object("txt_dni_add_venta").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1
            else:
                numerosdni = dni[0]+dni[1]+dni[2]+dni[3]+dni[4]+dni[5]+dni[6]+dni[7]
                letradni = dni[8]
                try:
                    num = int(numerosdni)
                except ValueError as err:
                    self.warning.format_secondary_text("DNI no tiene el formato correcto")
                    self.b.get_object("txt_dni_add_venta").set_text("")
                    self.warning.run()
                    self.warning.hide()
                    error = 1
                
                if error==0:
                    try:
                        letra = int(letradni)
                        self.warning.format_secondary_text("DNI no tiene el formato correcto")
                        self.b.get_object("txt_dni_add_venta").set_text("")
                        self.warning.run()
                        self.warning.hide()
                        error = 1
                    except ValueError as err:
                        a = 0
            
            if len(telefono)!=9:#COMPROBACIÓN DEL FORMATO DEL TELÉFONO
                self.warning.format_secondary_text("Teléfono no tiene el formato correcto")
                self.b.get_object("txt_telefono_add_venta").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1
            else:
                try:
                    tel = int(telefono)
                except ValueError as err:
                    self.warning.format_secondary_text("Teléfono no tiene el formato correcto")
                    self.b.get_object("txt_telefono_add_venta").set_text("")
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
                    
                    self.listadni('dni')
                    self.listaclientes('clientes')
            
            try:
                self.db.execute("INSERT INTO Venta VALUES(?,?,?,?)",(bastidor,dni,fecha,p))
                self.db.commit()
            except (sqlite3.IntegrityError):
                self.warning.format_secondary_text("Ya existe una venta con estos datos")
                self.warning.run()
                self.warning.hide()
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
                self.listaventas('venta')



    def ocultar_add_venta(self,w):#BOTON DE CANCELAR DE LA VENTANA AÑADIR VENTA
        self.ocultar("add_venta")




    def add_revision(self,w):#BOTÓN REVISIÓN DE LA VENTANA PRINCIPAL, ABRE LA VENTANA PARA AÑADIR UNA NUEVA REVISIÓN
        #OBTENER DATOS DE LA SELECCCION DE LA TABLA DE COCHES
        tree_view = self.b.get_object("treeview1")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        bastidor = treemodel.get_value(treeiter, 0)
        marca = treemodel.get_value(treeiter, 1)
        modelo = treemodel.get_value(treeiter, 2)
        
        fecha = time.strftime("%d/%m/%Y")#OBTENER LA FECHA DEL SISTEMA CON EL FORMATO 31/12/2017
        
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
        
        self.b.get_object("chk_frenos_add_revision").set_active(False)
        self.b.get_object("chk_aceite_add_revision").set_active(False)
        self.b.get_object("chk_filtro_add_revision").set_active(False)
        
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
            
            fecha = unicode(fecha,"utf-8")
            fr = unicode(fr,"utf-8")
            ac = unicode(ac,"utf-8")
            fi = unicode(fi,"utf-8")
            bastidor = unicode(bastidor,"utf-8")
            
            try:
                self.db.execute("INSERT INTO Revision VALUES(?,?,?,?,?,?)",(nrevision,fecha,fr,ac,fi,bastidor))
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
        self.ocultar("add_revision")
    
    
    
    def add_coche(self,w):#BOTON NUEVO DE LA VENTANA PRINCIPAL
        self.b.get_object("txt_bastidor_add_coche").set_text("")
        self.b.get_object("txt_marca_add_coche").set_text("")
        self.b.get_object("txt_modelo_add_coche").set_text("")
        self.b.get_object("txt_tipo_add_coche").set_text("")
        self.b.get_object("txt_motor_add_coche").set_text("")
        self.b.get_object("txt_cv_add_coche").set_text("")
        self.b.get_object("txt_color_add_coche").set_text("")
        self.b.get_object("txt_precio_add_coche").set_text("")
        self.limpia_imagen_nuevo_coche()
        self.blob = None
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
        
        bastidor = unicode(bastidor.upper(),"utf-8")
        marca = unicode(marca.upper(),"utf-8")
        modelo = unicode(modelo.upper(),"utf-8")
        tipo = unicode(tipo.upper(),"utf-8")
        motor = unicode(motor.upper(),"utf-8")
        color = unicode(color.upper(),"utf-8")
        
        error = 0
        
        if self.blob:
            imagen_blob=sqlite3.Binary(self.blob)
        
        if not(self.blob):
            self.warning.format_secondary_text("No has escogido ninguna imagen")
            self.warning.run()
            self.warning.hide()
            error=1
        
        if not(bastidor) or not(marca) or not(modelo) or not(tipo) or not(motor) or not(cv) or not(color) or not(precio):
            self.warning.format_secondary_text("Ningún campo puede estar vacío")
            self.warning.run()
            self.warning.hide()
            error = 1
        else:
            if len(bastidor)!=17:
                self.warning.format_secondary_text("El número de bastidor no tiene el formato correcto")
                self.b.get_object("txt_bastidor_add_coche").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1
            else:
                try:
                    b = int(bastidor[0]+bastidor[1]+bastidor[2])
                except ValueError as err:
                    self.warning.format_secondary_text("El número de bastidor no tiene el formato correcto")
                    self.b.get_object("txt_bastidor_add_coche").set_text("")
                    self.warning.run()
                    self.warning.hide()
                    error = 1
                
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
                self.db.execute("INSERT INTO Coche('N_Bastidor','Marca','Modelo','Motor','CV','Tipo','Color','Precio','Img') VALUES(?,?,?,?,?,?,?,?,?)",(bastidor,marca,modelo,motor,c,tipo,color,p,imagen_blob))
                self.db.commit()
            except (sqlite3.IntegrityError):
                self.warning.format_secondary_text("Ya existe un coche con ese bastidor")
                self.warning.run()
                self.warning.hide()
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
                
                #RELLENAR LOS COMBOBOX DE LOS FILTROS: MARCA Y MOTOR
                self.b.get_object("combo_marca").get_model().clear()
                marcas = self.db.execute("SELECT DISTINCT Marca FROM Coche;")
                for marca in marcas:
                    self.b.get_object("combo_marca").append_text(marca[0])
                
                self.b.get_object("combo_motor").get_model().clear()
                motores = self.db.execute("SELECT DISTINCT Motor FROM Coche;")
                for motor in motores:
                    self.b.get_object("combo_motor").append_text(motor[0])

                self.ocultar("add_coche")
                self.listacoches('tabla_coches')
                self.listacoches2('coches')
                
                self.b.get_object("btn_add_venta_main").set_sensitive(False)
                self.b.get_object("btn_add_revision_main").set_sensitive(False)
                self.b.get_object("btn_mod_coche_main").set_sensitive(False)
                self.b.get_object("btn_del_coche_main").set_sensitive(False)
    
    
    
    def ocultar_add_coche(self,w):#BOTÓN CANCELAR DE LA VENTANA AÑADIR COCHE
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
        if treeiter!=None:
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

            result = self.db.execute("SELECT Img FROM Coche WHERE N_Bastidor=?;",(bastidor,))
            for row in result:
                self.carga_imagen_mod_coche(row[0])
                self.blob = row[0]
        
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
        
        if self.blob:
            imagen_blob=sqlite3.Binary(self.blob)
        
        if not(self.blob):
            self.warning.format_secondary_text("No has escogido ninguna imagen")
            self.warning.run()
            self.warning.hide()
            error=1
        
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
                self.db.execute("UPDATE Coche SET Marca=?, Modelo=?, Motor=?, CV=?, Tipo=?, Color=?, Precio=?, Img=? WHERE N_Bastidor=?;",(marca,modelo,motor,c,tipo,color,p,imagen_blob,bastidor))
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
                
                #RELLENAR LOS COMBOBOX DE LOS FILTROS: MARCA Y MOTOR
                self.b.get_object("combo_marca").get_model().clear()
                marcas = self.db.execute("SELECT DISTINCT Marca FROM Coche;")
                for marca in marcas:
                    self.b.get_object("combo_marca").append_text(marca[0])
                
                self.b.get_object("combo_motor").get_model().clear()
                motores = self.db.execute("SELECT DISTINCT Motor FROM Coche;")
                for motor in motores:
                    self.b.get_object("combo_motor").append_text(motor[0])

                self.ocultar("mod_coche")
                self.b.get_object("btn_add_venta_main").set_sensitive(False)
                self.b.get_object("btn_add_revision_main").set_sensitive(False)
                self.b.get_object("btn_mod_coche_main").set_sensitive(False)
                self.b.get_object("btn_del_coche_main").set_sensitive(False)
    
    
    
    def borrar_coche(self,w):#BOTÓN ELIMINAR DE LA VENTANA PRINCIPAL, ELIMINA EL COCHE SELECCIONADO EN LA TABLA
        tree_view = self.b.get_object("treeview1")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        
        if treeiter!=None:
            self.mensajeborrar.format_secondary_text("¿Desea eliminar el coche?")
            respuesta = self.mensajeborrar.run()
            #print(respuesta)
            self.mensajeborrar.hide()

            if respuesta==-5:

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

                    #RELLENAR LOS COMBOBOX DE LOS FILTROS: MARCA Y MOTOR
                    self.b.get_object("combo_marca").get_model().clear()
                    marcas = self.db.execute("SELECT DISTINCT Marca FROM Coche;")
                    for marca in marcas:
                        self.b.get_object("combo_marca").append_text(marca[0])

                    self.b.get_object("combo_motor").get_model().clear()
                    motores = self.db.execute("SELECT DISTINCT Motor FROM Coche;")
                    for motor in motores:
                        self.b.get_object("combo_motor").append_text(motor[0])

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
        self.limpia_imagen_revision()
        self.b.get_object("chk_frenos_mod_revision").set_active(False)
        self.b.get_object("chk_aceite_mod_revision").set_active(False)
        self.b.get_object("chk_filtro_mod_revision").set_active(False)
        
        #OBTENER DATOS
        treeiter = None
        
        tree_view = self.b.get_object("treeview2")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        if treeiter!=None:
            nrevision = treemodel.get_value(treeiter, 0)

            self.b.get_object("lbl_revision_mod_revision").set_text(str(nrevision))

            result = self.db.execute("SELECT r.Fecha,c.Marca,c.Modelo,r.N_Bastidor,r.Frenos,r.Filtro,r.Aceite FROM Revision AS r, Coche AS c WHERE r.N_Revision=? AND r.N_Bastidor=c.N_Bastidor;",(nrevision,))
            for row in result:#RELLENAR CAJAS DE TEXTO CON LOS DATOS
                self.b.get_object("lbl_fecha_mod_revision").set_text(row[0])
                self.b.get_object("lbl_marca_mod_revision").set_text(row[1])
                self.b.get_object("lbl_modelo_mod_revision").set_text(row[2])
                self.b.get_object("lbl_bastidor_mod_revision").set_text(row[3])

                if row[4]=="Sí":
                    self.b.get_object("chk_frenos_mod_revision").set_active(True)
                else:
                    self.b.get_object("chk_frenos_mod_revision").set_active(False)

                if row[5]=="Sí":
                    self.b.get_object("chk_filtro_mod_revision").set_active(True)
                else:
                    self.b.get_object("chk_filtro_mod_revision").set_active(False)

                if row[6]=="Sí":
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

    
    
    def borrar_revision(self,w):#BOTÓN ELIMINAR DE LA PESTAÑA REVISIONES
        tree_iter = None
        
        seleccion = self.b.get_object("treeview2").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path)
        
        if tree_iter!=None:
            self.mensajeborrar.format_secondary_text("¿Desea eliminar la revisión?")
            respuesta = self.mensajeborrar.run()
            #print(respuesta)
            self.mensajeborrar.hide()

            if respuesta==-5:
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
                    self.limpia_imagen_revision()
                    self.b.get_object("btn_mod_revision_main").set_sensitive(False)
                    self.b.get_object("btn_del_revision_main").set_sensitive(False)



    def borrar_venta(self,w):#BOTÓN ELIMINAR DE LA PESTAÑA VENTAS
        tree_iter = None
        
        seleccion = self.b.get_object("treeview3").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
        
        if tree_iter!=None:
            self.mensajeborrar.format_secondary_text("¿Desea eliminar la venta?")
            respuesta = self.mensajeborrar.run()
            #print(respuesta)
            self.mensajeborrar.hide()

            if respuesta==-5:
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

    
    
    def ocultar_mod_revision(self,w):
        self.ocultar("mod_revision")
    
    
    
    def message_mod_venta(self,w):
        tree_iter = None
        
        seleccion = self.b.get_object("treeview3").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
        
        if tree_iter!=None:
            self.b.get_object("message_mod_venta").show()
    
    
    
    def mod_venta_cliente(self,w):
        seleccion = self.b.get_object("treeview3").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
            
        if tree_iter!=None:
            bastidor = modelo.get_value(tree_iter, 0)
            dni = modelo.get_value(tree_iter, 1)
        
            result = self.db.execute("SELECT * FROM Venta WHERE N_Bastidor=? AND Dni=?;",(bastidor,dni))
            for row in result:
                self.b.get_object("txt_bastidor_mod_venta").set_text(str(row[0]))
                self.b.get_object("txt_dni_mod_venta").set_text(str(row[1]))
                self.b.get_object("txt_fecha_mod_vent").set_text(str(row[2]))
                self.b.get_object("txt_precio_mod_venta").set_text(str(row[3]))

            self.b.get_object("btn_buscar_dni").set_sensitive(True)
            self.b.get_object("btn_buscar_bastidor").set_sensitive(False)

            self.ocultar("message_mod_venta")
            self.b.get_object("mod_venta").show()
    
    
    
    def mod_venta_coche(self,w):
        seleccion = self.b.get_object("treeview3").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
            
        if tree_iter!=None:
            bastidor = modelo.get_value(tree_iter, 0)
            dni = modelo.get_value(tree_iter, 1)
        
            result = self.db.execute("SELECT * FROM Venta WHERE N_Bastidor=? AND Dni=?;",(bastidor,dni))
            for row in result:
                self.b.get_object("txt_bastidor_mod_venta").set_text(str(row[0]))
                self.b.get_object("txt_dni_mod_venta").set_text(str(row[1]))
                self.b.get_object("txt_fecha_mod_vent").set_text(str(row[2]))
                self.b.get_object("txt_precio_mod_venta").set_text(str(row[3]))

            self.b.get_object("btn_buscar_dni").set_sensitive(False)
            self.b.get_object("btn_buscar_bastidor").set_sensitive(True)

            self.ocultar("message_mod_venta")
            self.b.get_object("mod_venta").show()
    
    
    def mod_venta2(self,w):#BOTÓN ACEPTAR DE LA VENTANA MODIFICAR VENTA
        seleccion = self.b.get_object("treeview3").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
            bastidor = modelo.get_value(tree_iter, 0)
            dni = modelo.get_value(tree_iter, 1)
        
        nbastidor = self.b.get_object("txt_bastidor_mod_venta").get_text()
        ndni = self.b.get_object("txt_dni_mod_venta").get_text()
        fecha = self.b.get_object("txt_fecha_mod_vent").get_text()
        precio = self.b.get_object("txt_precio_mod_venta").get_text()
        
        nbastidor = unicode(nbastidor,"utf-8")
        ndni = unicode(ndni,"utf-8")
        fecha = unicode(fecha,"utf-8")
        
        error = 0
        
        if not(fecha) or not(precio):
            self.warning.format_secondary_text("Ningún campo puede estar vacío")
            self.warning.run()
            self.warning.hide()
            error = 1
        else:
            try:
                p = float(precio)
            except ValueError as err:
                self.warning.format_secondary_text("Precio no es un número real")
                self.b.get_object("txt_precio_mod_venta").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1
        
        if error==0:
            try:
                self.db.execute("UPDATE Venta SET N_Bastidor=?, Dni=?, Fecha=?, Precio=? WHERE N_Bastidor=? AND Dni=?;",(nbastidor,ndni,fecha,p,bastidor,dni))
                self.db.commit()
            except (sqlite3.IntegrityError):
                self.warning.format_secondary_text("Ya existe una venta con estos datos")
                self.warning.run()
                self.warning.hide()
            except (sqlite3.ProgrammingError, ValueError, TypeError)as tipoerror:
                self.warning.format_secondary_text(str(tipoerror))
                self.warning.run()
                self.warning.hide()
            else:
                self.info.format_secondary_text("Venta modificada correctamente")
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
                
                self.ocultar("mod_venta")
    
    
    
    def ocultar_mod_venta(self,w):
        self.b.get_object("txt_fecha_mod_vent").set_text("")
        self.b.get_object("txt_dni_mod_venta").set_text("")
        self.b.get_object("txt_bastidor_mod_venta").set_text("")
        self.b.get_object("txt_precio_mod_venta").set_text("")
        self.ocultar("mod_venta")
    
    
    
    def mod_cliente(self,w):#BOTÓN MODIFICAR CLIENTE DE LA PESTAÑA CLIENTES
        #LIMPIAR CAJAS
        self.b.get_object("txt_nombre_mod_cliente").set_text("")
        self.b.get_object("txt_apellidos_mod_cliente").set_text("")
        self.b.get_object("txt_dni_mod_cliente").set_text("")
        self.b.get_object("txt_telefono_mod_cliente").set_text("")
        self.b.get_object("txt_direccion_mod_cliente").set_text("")
        
        #OBTENER DATOS DEL CLIENTE SELECCIONADO
        treeiter = None
        
        tree_view = self.b.get_object("treeview4")
        tree_sel = tree_view.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        if treeiter!=None:
            dni = treemodel.get_value(treeiter, 0)

            self.b.get_object("txt_dni_mod_cliente").set_text(dni)

            result = self.db.execute("SELECT Nombre,Apellidos,Telefono,Domicilio FROM Cliente WHERE Dni=?;",(dni,))
            for row in result:#RELLENAR CAJAS DE TEXTO CON LOS DATOS
                self.b.get_object("txt_nombre_mod_cliente").set_text(row[0])
                self.b.get_object("txt_apellidos_mod_cliente").set_text(row[1])
                self.b.get_object("txt_telefono_mod_cliente").set_text(row[2])
                self.b.get_object("txt_direccion_mod_cliente").set_text(row[3])

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
        else:
            if len(telefono)!=9:#COMPROBACIÓN DEL FORMATO DEL TELÉFONO
                self.warning.format_secondary_text("Teléfono no tiene el formato correcto")
                self.b.get_object("txt_telefono_mod_cliente").set_text("")
                self.warning.run()
                self.warning.hide()
                error = 1
            else:
                try:
                    tel = int(telefono)
                except ValueError as err:
                    self.warning.format_secondary_text("Teléfono no tiene el formato correcto")
                    self.b.get_object("txt_telefono_mod_cliente").set_text("")
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
    
    
    
    def borrar_cliente(self,w):#BOTÓN ELIMINAR CLIENTE DE LA PESTAÑA CLIENTES
        tree_iter = None
        
        seleccion = self.b.get_object("treeview4").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
        
        if tree_iter!=None:
            self.mensajeborrar.format_secondary_text("¿Desea eliminar el cliente?")
            respuesta = self.mensajeborrar.run()
            #print(respuesta)
            self.mensajeborrar.hide()

            if respuesta==-5:
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
    
    
    
    def combo_coche_changed(self,combo):
        index = combo.get_active()
        if index!=-1:
            self.b.get_object("txt_combo_coche_main").set_editable(True)
            self.b.get_object("btn_buscar_coche_main").set_sensitive(True)
    
    
    
    def busca_coche_tipo(self,w):
        campo = self.b.get_object("combo_coche").get_active_text()
        busqueda = self.b.get_object("txt_combo_coche_main").get_text()
        
        if campo=="Bastidor":
            campo = "N_Bastidor"
        
        if not(busqueda):
            self.warning.format_secondary_text("El campo no puede estar vacío")
            self.warning.run()
            self.warning.hide()
        else:
            self.lista = self.b.get_object("tabla_coches")
            self.lista.clear()
            
            result = self.db.execute("SELECT * FROM Coche WHERE "+campo+" LIKE '%"+busqueda+"%';")
            for row in result:
                self.lista.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
            
            self.b.get_object("btn_add_venta_main").set_sensitive(False)
            self.b.get_object("btn_add_revision_main").set_sensitive(False)
            self.b.get_object("btn_mod_coche_main").set_sensitive(False)
            self.b.get_object("btn_del_coche_main").set_sensitive(False)
    
    
    
    def on_combo_cliente1_changed(self,combo):
        index = combo.get_active()
        if index!=-1:
            self.b.get_object("txt_combo_cliente1").set_editable(True)
            self.b.get_object("btn_buscar_cliente1").set_sensitive(True)
    
    
    
    def on_btn_buscar_cliente1_clicked(self,w):
        campo = self.b.get_object("combo_cliente1").get_active_text()
        busqueda = self.b.get_object("txt_combo_cliente1").get_text()
        
        if not(busqueda):
            self.warning.format_secondary_text("El campo no puede estar vacío")
            self.warning.run()
            self.warning.hide()
        else:
            self.lista = self.b.get_object("clientes")
            self.lista.clear()
            
            result = self.db.execute("SELECT Dni, Apellidos, Nombre FROM Cliente WHERE "+campo+" LIKE '%"+busqueda+"%';")
            for row in result:
                self.lista.append([row[0],row[1],row[2]])
            
            self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
    
    
    
    def on_combo_cliente2_changed(self,combo):
        index = combo.get_active()
        if index!=-1:
            self.b.get_object("txt_combo_cliente2").set_editable(True)
            self.b.get_object("btn_buscar_cliente2").set_sensitive(True)
    
    
    
    def on_btn_buscar_cliente2_clicked(self,w):
        campo = self.b.get_object("combo_cliente2").get_active_text()
        busqueda = self.b.get_object("txt_combo_cliente2").get_text()
        
        if not(busqueda):
            self.warning.format_secondary_text("El campo no puede estar vacío")
            self.warning.run()
            self.warning.hide()
        else:
            self.lista = self.b.get_object("clientes")
            self.lista.clear()
            
            result = self.db.execute("SELECT Dni, Apellidos, Nombre FROM Cliente WHERE "+campo+" LIKE '%"+busqueda+"%';")
            for row in result:
                self.lista.append([row[0],row[1],row[2]])
            
            self.b.get_object("btn_seleccionar_cliente2").set_sensitive(False)
    
    
    
    def on_combo_coche2_changed(self,combo):
        index = combo.get_active()
        if index!=-1:
            self.b.get_object("txt_combo_coche").set_editable(True)
            self.b.get_object("btn_buscar_coche").set_sensitive(True)
    
    
    
    def on_combo_motor_changed(self,combo):
        motorseleccionado = self.b.get_object("combo_motor").get_active()
        
        if motorseleccionado!=-1:
            motor = self.b.get_object("combo_motor").get_active_text()
            motor = unicode(motor,"utf-8")
            marcaseleccionada = self.b.get_object("combo_marca").get_active()

            if marcaseleccionada==-1:
                self.lista = self.b.get_object("tabla_coches")
                self.lista.clear()

                result = self.db.execute("SELECT * FROM Coche WHERE Motor=?;",(motor,))
                for row in result:
                    self.lista.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
                
                self.b.get_object("btn_add_venta_main").set_sensitive(False)
                self.b.get_object("btn_add_revision_main").set_sensitive(False)
                self.b.get_object("btn_mod_coche_main").set_sensitive(False)
                self.b.get_object("btn_del_coche_main").set_sensitive(False)
            else:
                marca = self.b.get_object("combo_marca").get_active_text()
                marca = unicode(marca,"utf-8")
                self.lista = self.b.get_object("tabla_coches")
                self.lista.clear()

                result = self.db.execute("SELECT * FROM Coche WHERE Motor=? AND Marca=?;",(motor,marca))
                for row in result:
                    self.lista.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
                
                self.b.get_object("btn_add_venta_main").set_sensitive(False)
                self.b.get_object("btn_add_revision_main").set_sensitive(False)
                self.b.get_object("btn_mod_coche_main").set_sensitive(False)
                self.b.get_object("btn_del_coche_main").set_sensitive(False)
    
    
    
    def on_combo_marca_changed(self,combo):
        marcaseleccionada = self.b.get_object("combo_marca").get_active()
        
        if marcaseleccionada!=-1:
            marca = self.b.get_object("combo_marca").get_active_text()
            marca = unicode(marca,"utf-8")
            motorseleccionado = self.b.get_object("combo_motor").get_active()

            if motorseleccionado==-1:
                self.lista = self.b.get_object("tabla_coches")
                self.lista.clear()

                result = self.db.execute("SELECT * FROM Coche WHERE Marca=?;",(marca,))
                for row in result:
                    self.lista.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
                
                self.b.get_object("btn_add_venta_main").set_sensitive(False)
                self.b.get_object("btn_add_revision_main").set_sensitive(False)
                self.b.get_object("btn_mod_coche_main").set_sensitive(False)
                self.b.get_object("btn_del_coche_main").set_sensitive(False)
            else:
                motor = self.b.get_object("combo_motor").get_active_text()
                motor = unicode(motor,"utf-8")
                self.lista = self.b.get_object("tabla_coches")
                self.lista.clear()

                result = self.db.execute("SELECT * FROM Coche WHERE Marca=? AND Motor=?;",(marca,motor))
                for row in result:
                    self.lista.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
                
                self.b.get_object("btn_add_venta_main").set_sensitive(False)
                self.b.get_object("btn_add_revision_main").set_sensitive(False)
                self.b.get_object("btn_mod_coche_main").set_sensitive(False)
                self.b.get_object("btn_del_coche_main").set_sensitive(False)
    
    
    
    def on_btn_buscar_coche_clicked(self,w):
        campo = self.b.get_object("combo_coche2").get_active_text()
        busqueda = self.b.get_object("txt_combo_coche").get_text()
        
        if campo=="Bastidor":
            campo = "N_Bastidor"
        
        if not(busqueda):
            self.warning.format_secondary_text("El campo no puede estar vacío")
            self.warning.run()
            self.warning.hide()
        else:
            self.lista = self.b.get_object("coches")
            self.lista.clear()
            
            result = self.db.execute("SELECT N_Bastidor, Marca, Modelo FROM Coche WHERE "+campo+" LIKE '%"+busqueda+"%';")
            for row in result:
                self.lista.append([row[0],row[1],row[2]])
            
            self.b.get_object("btn_seleccionar_coche").set_sensitive(False)
    
    
    
    def abrir_calendario(self,w):#BOTÓN ABRIR CALENDARIO DE LA VENTANA MODIFICAR VENTA
        self.b.get_object("calendario").show()
    
    
    
    def seleccionar_fecha(self,w):#BOTÓN SELECCIONAR FECHA DEL CALENDARIO
        anio,mes,dia = self.b.get_object("calendar1").get_date()
        m = int(mes)+1
        fecha = str(dia)+"/"+str(m)+"/"+str(anio)
        self.b.get_object("txt_fecha_mod_vent").set_text(fecha)
        self.ocultar("calendario")
    
    
    
    def on_treeview6_row_activated(self,treeview,path,view_column):
        self.seleccionar_cliente("buscar_cliente_mod_venta")
    
    
    
    def on_treeview5_row_activated(self,treeview,path,view_column):
        self.seleccionar_cliente2("buscar_cliente_add_venta")
    
    
    
    def on_treeview7_row_activated(self,treeview,path,view_column):
        self.seleccionar_coche("buscar_coche_mod_venta")
    
    
    
    def on_treeview1_row_activated(self,treeview,path,view_column):
        self.mod_coche("main")
    
    
    
    def on_treeview2_row_activated(self,treeview,path,view_column):
        self.mod_revision("main")
    
    
    
    def on_treeview3_row_activated(self,treeview,path,view_column):
        self.message_mod_venta("main")
    
    
    
    def on_treeview4_row_activated(self,treeview,path,view_column):
        self.mod_cliente("main")

    
    
    def on_Acerca_de_activate(self,w):
        self.b.get_object("AcercaDe").show()
    
    
    
    def on_btnAcercaDe_activate(self,w):
        self.ocultar("AcercaDe")
    
    
    
    def on_btnReiniciarBusqueda_clicked(self,w):
        self.b.get_object("combo_coche").set_active(-1)
        self.b.get_object("combo_motor").set_active(-1)
        self.b.get_object("combo_marca").set_active(-1)
        self.b.get_object("txt_combo_coche_main").set_editable(False)
        self.b.get_object("txt_combo_coche_main").set_text("")
        self.b.get_object("btn_buscar_coche_main").set_sensitive(False)
        self.b.get_object("btn_add_venta_main").set_sensitive(False)
        self.b.get_object("btn_add_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_coche_main").set_sensitive(False)
        self.b.get_object("btn_del_coche_main").set_sensitive(False)
        self.listacoches('tabla_coches')
    
    
    
    def on_treeview1_key_press_event(self,treeview,evento):
        #print(evento.keyval)
        tecla = evento.keyval
        if tecla==65535:
            self.borrar_coche("main")
    
    
    
    def on_treeview2_key_press_event(self,treeview,evento):
        tecla = evento.keyval
        if tecla==65535:
            self.borrar_revision("main")
    
    
    
    def on_treeview3_key_press_event(self,treeview,evento):
        tecla = evento.keyval
        if tecla==65535:
            self.borrar_venta("main")
    
    
    
    def on_treeview4_key_press_event(self,treeview,evento):
        tecla = evento.keyval
        if tecla==65535:
            self.borrar_cliente("main")
    
    
    
    def limpia_imagen_nuevo_coche(self):
            #Elimino si hubiera una imagen anterior
            hijo=self.b.get_object("hbox1").get_children()#Toma los hijos, aunque solo ha de haber uno
            if hijo: #Para que no de error en el caso de no tener hijo (imagen)
                self.b.get_object("hbox1").remove(hijo[0])#Elimina el enlace
    
    
    
    def limpia_imagen_revision(self):
        hijo=self.b.get_object("hbox2").get_children()#Toma los hijos, aunque solo ha de haber uno
        if hijo: #Para que no de error en el caso de no tener hijo (imagen)
            self.b.get_object("hbox2").remove(hijo[0])#Elimina el enlace
    
    
    
    def limpia_imagen_mod_coche(self):
        hijo=self.b.get_object("hbox3").get_children()#Toma los hijos, aunque solo ha de haber uno
        if hijo: #Para que no de error en el caso de no tener hijo (imagen)
            self.b.get_object("hbox3").remove(hijo[0])#Elimina el enlace
    
    
    
    def on_btn_sel_imagen_clicked(self,w):
        selfichero=self.b.get_object("filechooserdialog1")
        selfichero.set_action(0)#Escojo la opción de CARGAR del filechooserdialog
        respuesta=selfichero.run() #Se quedará parado hasta que pulse algún botón
        selfichero.hide()    

        if respuesta == 1:
            fichero=selfichero.get_filename()
            fichero=unicode(fichero,'utf8')

            self.limpia_imagen_nuevo_coche()

            image = gtk.Image()
            #Se crea un image con un tamaño determinado
            image.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size(fichero,190,190))
            self.b.get_object("hbox1").pack_start(image)
            self.b.get_object("add_coche").show_all() #Ha de repintar la pantalla con el nuevo elemento creado por código (la imagen) 

            with open(fichero, 'rb') as f: #abre como binario y de lectura
                self.blob = f.read()#guardo el fichero en el atributo de clase
                #print(type(self.blob))
                f.close()
    
    
    
    def on_btn_sel_imagen1_clicked(self,w):
        selfichero=self.b.get_object("filechooserdialog1")
        selfichero.set_action(0)#Escojo la opción de CARGAR del filechooserdialog
        respuesta=selfichero.run() #Se quedará parado hasta que pulse algún botón
        selfichero.hide()    

        if respuesta == 1:
            fichero=selfichero.get_filename()
            fichero=unicode(fichero,'utf8')

            self.limpia_imagen_mod_coche()

            image = gtk.Image()
            #Se crea un image con un tamaño determinado
            image.set_from_pixbuf(gtk.gdk.pixbuf_new_from_file_at_size(fichero,190,190))
            self.b.get_object("hbox3").pack_start(image)
            self.b.get_object("mod_coche").show_all() #Ha de repintar la pantalla con el nuevo elemento creado por código (la imagen) 

            with open(fichero, 'rb') as f: #abre como binario y de lectura
                self.blob = f.read()#guardo el fichero en el atributo de clase
                #print(type(self.blob))
                f.close()
    
    
    
    def carga_imagen_bbdd(self,BLOB):
        #Esta funcion limpia donde está la imagen y la muestra
        self.limpia_imagen_revision()

        #Hay que usar una clase cargador para que lea el BLOB y lo convierta en un pixbuf
        #que se pueda cargar normalmente
        loader = gtk.gdk.PixbufLoader("jpeg")
        loader.set_size(220, 150)#Para que se adapte al tamaño del frame donde está contenida la imagen   
        loader.write(BLOB)
        loader.close()
        pixbuf = loader.get_pixbuf()

        #Saca la imagen            
        image = gtk.Image()
#            print(row[5]) #Esto sacaría todo el texto
        image.set_from_pixbuf(pixbuf)
        self.b.get_object("hbox2").pack_start(image)
        self.b.get_object("main").show_all() #si no no lo muestra
    
    
    def carga_imagen_mod_coche(self,BLOB):
        #Esta funcion limpia donde está la imagen y la muestra
        self.limpia_imagen_mod_coche()

        #Hay que usar una clase cargador para que lea el BLOB y lo convierta en un pixbuf
        #que se pueda cargar normalmente
        loader = gtk.gdk.PixbufLoader("jpeg")
        loader.set_size(190, 150)#Para que se adapte al tamaño del frame donde está contenida la imagen   
        loader.write(BLOB)
        loader.close()
        pixbuf = loader.get_pixbuf()

        #Saca la imagen            
        image = gtk.Image()
#            print(row[5]) #Esto sacaría todo el texto
        image.set_from_pixbuf(pixbuf)
        self.b.get_object("hbox3").pack_start(image)
        self.b.get_object("mod_coche").show_all() #si no no lo muestra
    
    
    
    def on_txt_combo_coche_main_key_release_event(self, w, event):
        #print(event.keyval)
        tecla = event.keyval
        if tecla==65293:
            self.busca_coche_tipo("txt_combo_coche_main")
    
    
    
    def on_txt_combo_cliente1_key_release_event(self, w, event):
        tecla = event.keyval
        if tecla==65293:
            self.on_btn_buscar_cliente1_clicked("txt_combo_cliente1")
    
    

    def on_txt_combo_cliente2_key_release_event(self, w, event):
        tecla = event.keyval
        if tecla==65293:
            self.on_btn_buscar_cliente2_clicked("txt_combo_cliente2")
    
    
    
    def on_txt_combo_coche_key_release_event(self, w, event):
        tecla = event.keyval
        if tecla==65293:
            self.on_btn_buscar_coche_clicked("txt_combo_coche")
    
    
    
    def on_manual_activate(self,w):
        manual="MANUAL.pdf" #ha de estar en la misma carpeta del proyecto
        if (sys.platform=="linux"):
            subprocess.call(["xdg-open", manual])
        else: #si win32 o win64
            os.startfile(manual)
    
    
    
    def on_destroy(self, w, *signals):
        # return True --> no cierra
        # return False --> cierra
        print("Cerrando BBDD")
        self.db.commit()
        self.db.close()            
        gtk.main_quit()
    
    
    
    def on_destroy2(self,w,*signals):
        w.hide()
        return True



    #FUNCIONES AUXILIARES########################################################################################
    def ocultar(self,ventana):
        self.b.get_object(ventana).hide()
    
    
    
    def reiniciar_bbdd(self,w):
        self.mensajeborrar.format_secondary_text("¿Desea reiniciar la base de datos?")
        respuesta = self.mensajeborrar.run()
        #print(respuesta)
        self.mensajeborrar.hide()

        if respuesta==-5:
            self.con.crear_esquema("reinicia")
            self.listacoches('tabla_coches')
            self.listarevisiones('revisiones')
            self.listaventas('venta')
            self.listadni('dni')
            self.listacoches2('coches')
            self.listaclientes('clientes')
            #COMBOBOX
            self.b.get_object("combo_coche").set_active(-1)
            #CAJAS DE TEXTO
            self.b.get_object("txt_combo_coche_main").set_editable(False)
            self.b.get_object("txt_combo_coche_main").set_text("")
            #BOTONES
            self.b.get_object("btn_buscar_cliente1").set_sensitive(False)
            self.b.get_object("btn_buscar_cliente2").set_sensitive(False)
            self.b.get_object("btn_buscar_coche_main").set_sensitive(False)
            self.b.get_object("btn_buscar_coche").set_sensitive(False)
            self.b.get_object("btn_add_venta_main").set_sensitive(False)
            self.b.get_object("btn_add_revision_main").set_sensitive(False)
            self.b.get_object("btn_mod_coche_main").set_sensitive(False)
            self.b.get_object("btn_del_coche_main").set_sensitive(False)
            self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
            self.b.get_object("btn_seleccionar_cliente2").set_sensitive(False)
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
        
        result = self.db.execute('SELECT N_Bastidor,Marca,Modelo,Motor,CV,Tipo,Color,Precio FROM Coche')
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
    
    
    
    def on_treeview1_button_release_event(self,treeview,evento):
        botonpulsado = evento.button
        treeiter = None
        
        tree_sel = treeview.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        
        if botonpulsado==1 and treeiter!=None:#BOTÓN IZQUIERDO
            self.b.get_object("btn_add_venta_main").set_sensitive(True)
            self.b.get_object("btn_add_revision_main").set_sensitive(True)
            self.b.get_object("btn_mod_coche_main").set_sensitive(True)
            self.b.get_object("btn_del_coche_main").set_sensitive(True)
    
    
    
    def on_boton_coche(self,treeview,evento):
        botonpulsado = evento.button
        
        if botonpulsado == 3: #Botón derecho
            self.menu = gtk.Menu()#Se crea el menú
            #Primer item
            menu_item1 = gtk.ImageMenuItem(gtk.STOCK_NEW)
            self.menu.append(menu_item1)
            menu_item1.connect("activate", self.add_coche)
            #Segundo item
            menu_item2 = gtk.ImageMenuItem(gtk.STOCK_EDIT)
            self.menu.append(menu_item2)
            menu_item2.connect("activate", self.mod_coche)
            #Tercer item
            menu_item3 = gtk.ImageMenuItem(gtk.STOCK_DELETE)
            self.menu.append(menu_item3)
            menu_item3.connect("activate", self.borrar_coche)
            self.menu.popup(None,None,None,evento.button,evento.time)
            menu_item1.show()
            menu_item2.show()
            menu_item3.show()
    
    
    
    def on_boton_cliente(self,treeview,evento):
        botonpulsado = evento.button
        treeiter = None
        
        tree_sel = treeview.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        
        if botonpulsado==1 and treeiter!=None:
            self.b.get_object("btn_seleccionar_cliente1").set_sensitive(True)
    
    
    
    def on_treeview7_button_press_event(self,treeview,evento):
        botonpulsado = evento.button
        treeiter = None
        
        tree_sel = treeview.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        
        if botonpulsado==1 and treeiter!=None:
            self.b.get_object("btn_seleccionar_coche").set_sensitive(True)
    
    
    
    def on_treeview4_button_press_event(self,treeview,evento):
        botonpulsado = evento.button
        if botonpulsado == 3: #Botón derecho
            self.menu = gtk.Menu()#Se crea el menú
            #Primer item
            menu_item1 = gtk.ImageMenuItem(gtk.STOCK_EDIT)
            self.menu.append(menu_item1)
            menu_item1.connect("activate", self.mod_cliente)
            #Segundo item
            menu_item2 = gtk.ImageMenuItem(gtk.STOCK_DELETE)
            self.menu.append(menu_item2)
            menu_item2.connect("activate", self.borrar_cliente)
            self.menu.popup(None,None,None,evento.button,evento.time)
            menu_item1.show()
            menu_item2.show()
    
    
    
    def on_treeview2_button_press_event(self,treeview,evento):
        botonpulsado = evento.button
        if botonpulsado == 3: #Botón derecho
            self.menu = gtk.Menu()#Se crea el menú
            #Primer item
            menu_item1 = gtk.ImageMenuItem(gtk.STOCK_EDIT)
            self.menu.append(menu_item1)
            menu_item1.connect("activate", self.mod_revision)
            #Segundo item
            menu_item2 = gtk.ImageMenuItem(gtk.STOCK_DELETE)
            self.menu.append(menu_item2)
            menu_item2.connect("activate", self.borrar_revision)
            self.menu.popup(None,None,None,evento.button,evento.time)
            menu_item1.show()
            menu_item2.show()
    
    
    
    def on_treeview3_button_press_event(self,treeview,evento):
        botonpulsado = evento.button
        if botonpulsado == 3: #Botón derecho
            self.menu = gtk.Menu()#Se crea el menú
            #Primer item
            menu_item1 = gtk.ImageMenuItem(gtk.STOCK_EDIT)
            self.menu.append(menu_item1)
            menu_item1.connect("activate", self.message_mod_venta)
            #Segundo item
            menu_item2 = gtk.ImageMenuItem(gtk.STOCK_DELETE)
            self.menu.append(menu_item2)
            menu_item2.connect("activate", self.borrar_venta)
            self.menu.popup(None,None,None,evento.button,evento.time)
            menu_item1.show()
            menu_item2.show()
    
    
    def on_boton_cliente2(self,treeview,evento):
        botonpulsado = evento.button
        treeiter = None
        
        tree_sel = treeview.get_selection()
        (treemodel, treeiter) = tree_sel.get_selected()
        
        if botonpulsado==1 and treeiter!=None:
            self.b.get_object("btn_seleccionar_cliente2").set_sensitive(True)
    
    
    
    def on_btn_dni(self,treeview,evento):
        botonpulsado = evento.button
        tree_iter = None
        
        seleccion = self.b.get_object("treeview4").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
        
        if botonpulsado==1 and tree_iter!=None:
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
        tree_iter = None
        
        seleccion = self.b.get_object("treeview3").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
        
        if botonpulsado==1 and tree_iter!=None:
            bastidor = modelo.get_value(tree_iter, 0)
            dni = modelo.get_value(tree_iter, 1)
            
            result = self.db.execute("SELECT v.Fecha,cl.Nombre,cl.Apellidos,cl.Dni,co.Marca || ' ' || co.Modelo AS Coche,v.Precio FROM Venta AS v,Coche AS co,Cliente AS cl WHERE v.N_Bastidor=? AND v.Dni=? AND v.N_Bastidor=co.N_Bastidor AND v.Dni=cl.Dni;",(bastidor,dni))
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
        tree_iter = None
        
        seleccion = self.b.get_object("treeview2").get_selection()
        (modelo, pathlist) = seleccion.get_selected_rows()
        for path in pathlist :
            tree_iter = modelo.get_iter(path) #se coge el puntero a la fila
        
        if botonpulsado==1 and tree_iter!=None:
            nrevision = modelo.get_value(tree_iter, 0)
            
            result = self.db.execute("SELECT r.N_Revision,r.Fecha,r.N_Bastidor,c.Marca,c.Modelo,r.Frenos,r.Filtro,r.Aceite,c.Img FROM Revision AS r, Coche AS c WHERE N_Revision=? AND r.N_Bastidor=c.N_Bastidor;",(nrevision,))
            for row in result:
                self.b.get_object("lbl_numero_revision_main").set_text(str(row[0]))
                self.b.get_object("lbl_fecha_revision_main").set_text(str(row[1]))
                self.b.get_object("lbl_bastidor_revision_main").set_text(str(row[2]))
                self.b.get_object("lbl_marca_revision_main").set_text(str(row[3]))
                self.b.get_object("lbl_modelo_revision_main").set_text(str(row[4]))
                self.b.get_object("lbl_frenos_revision_main").set_text(str(row[5]))
                self.b.get_object("lbl_filtro_revision_main").set_text(str(row[6]))
                self.b.get_object("lbl_aceite_revision_main").set_text(str(row[7]))
                self.carga_imagen_bbdd(row[8])
            
            self.b.get_object("btn_mod_revision_main").set_sensitive(True)
            self.b.get_object("btn_del_revision_main").set_sensitive(True)
    
    
    
    def activaLabel(self, notebook, page, page_num):
        #BOTONES
        self.b.get_object("btn_add_venta_main").set_sensitive(False)
        self.b.get_object("btn_add_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_coche_main").set_sensitive(False)
        self.b.get_object("btn_del_coche_main").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente1").set_sensitive(False)
        self.b.get_object("btn_seleccionar_cliente2").set_sensitive(False)
        self.b.get_object("btn_mod_revision_main").set_sensitive(False)
        self.b.get_object("btn_del_revision_main").set_sensitive(False)
        self.b.get_object("btn_mod_clientes_main").set_sensitive(False)
        self.b.get_object("btn_del_clientes_main").set_sensitive(False)
        self.b.get_object("btn_mod_venta_main").set_sensitive(False)
        self.b.get_object("btn_del_venta_main").set_sensitive(False)
        self.b.get_object("txt_combo_coche_main").set_editable(False)
        #ETIQUETAS DE LA PESTAÑA REVISIONES
        self.b.get_object("lbl_numero_revision_main").set_text("")
        self.b.get_object("lbl_fecha_revision_main").set_text("")
        self.b.get_object("lbl_bastidor_revision_main").set_text("")
        self.b.get_object("lbl_marca_revision_main").set_text("")
        self.b.get_object("lbl_modelo_revision_main").set_text("")
        self.b.get_object("lbl_frenos_revision_main").set_text("")
        self.b.get_object("lbl_filtro_revision_main").set_text("")
        self.b.get_object("lbl_aceite_revision_main").set_text("")
        self.limpia_imagen_revision()
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
    