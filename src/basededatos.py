#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Este código define un conector a una base de datos SQLITE.
    El método dameconexión abre la base de datos que se le indica
"""

import sys
try:
    import sqlite3
except:
    print("No existe SQLITE3")
    sys.exit(1)

class Conector:
    #El constructor inicia 
    def __init__(self,nombre):
        print ("Clase Conector creada")
        self.cursor=sqlite3.connect(nombre) #crea el fichero db si no existe o devuelve el cursor
        self.cursor.execute("PRAGMA foreign_keys = 1")
        print("Creada conexión para BBDD:", nombre)
                
    #Este método devuelve la conexión    
    def dameconexion(self):
        return self.cursor

    #Crea el esquema de la base de datos
    def crear_esquema(self,tipo):
        if tipo=="reinicia":#Aquí entraría si le paso la variable tipo=reinicia
            self.cursor.execute("DROP TABLE Venta");#Borro tabla Venta
            print("Tabla Venta borrada")
            self.cursor.execute("DROP TABLE Revision");#Borro tabla Revision
            print("Tabla Revision borrada")
            self.cursor.execute("DROP TABLE Cliente");#Borro tabla Cliente
            print("Tabla Cliente borrada")
            self.cursor.execute("DROP TABLE Coche");#Borro tabla Coche
            print("Tabla Coche borrada")
            
        self.cursor.execute(
            """CREATE TABLE `Coche` (
            `N_Bastidor`	TEXT,
            `Marca`	TEXT,
            `Modelo`	TEXT,
            `Motor`	TEXT,
            `CV`	INTEGER,
            `Tipo`	TEXT,
            `Color`	TEXT,
            `Precio`	REAL,
            `Img`       BLOB,
            PRIMARY KEY(N_Bastidor)
            );"""
        )
        
        self.cursor.commit()
        
        self.cursor.execute(
            """CREATE TABLE `Cliente` (
            `Dni`	TEXT,
            `Nombre`	TEXT,
            `Apellidos`	TEXT,
            `Telefono`	TEXT,
            `Domicilio`	TEXT,
            PRIMARY KEY(Dni)
            );"""
        )
        
        self.cursor.commit()
        
        self.cursor.execute(
            """CREATE TABLE `Revision` (
            `N_Revision`	INTEGER DEFAULT 1 PRIMARY KEY,
            `Fecha`	TEXT,
            `Frenos`	TEXT,
            `Aceite`	TEXT,
            `Filtro`	TEXT,
            `N_Bastidor`	TEXT REFERENCES Coche(N_Bastidor)
                ON DELETE CASCADE ON UPDATE CASCADE
            );"""
        )
        
        self.cursor.commit()
        
        self.cursor.execute(
            """CREATE TABLE `Venta` (
            `N_Bastidor`	TEXT REFERENCES Coche(N_Bastidor)
                ON DELETE CASCADE ON UPDATE CASCADE,
            `Dni`	TEXT REFERENCES Cliente(Dni)
                ON DELETE CASCADE ON UPDATE CASCADE,
            `Fecha`	TEXT,
            `Precio`	REAL,
            PRIMARY KEY(N_Bastidor,Dni)
            );"""
        )
        
        self.cursor.commit()
        print("Tablas creadas")