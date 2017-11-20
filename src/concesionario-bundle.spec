# -*- mode: python -*-

block_cipher = None

#Esto analizará los ficheros que se le indican para ver las dependencias y coger los DLL y PYD necesarios
a = Analysis(['__init__.py','concesionario.py'],
             pathex=['C:\\Users\\almc\\Documents\\NetBeansProjects\\Concesionario_v2\\src'], #Directorio de trabajo (CAMBIAR)
             binaries=None, #Inicializa todo lo que va dentro del EXE (Librerías, etc..)
             datas=None, #Inicializa
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
			 
pyz = PYZ(a.pure, a.zipped_data,cipher=block_cipher)

#Se incluyen ficheros externos 			 
a.datas += [('concesionario.glade', 'concesionario.glade', 'DATA')]
a.datas += [('concesionario.db', 'concesionario.db', 'DATA')]
a.datas += [('cliente.ico', 'cliente.ico', 'DATA')]
a.datas += [('coche.ico', 'coche.ico', 'DATA')]
a.datas += [('factura.ico', 'factura.ico', 'DATA')]
a.datas += [('herramientas.ico', 'herramientas.ico', 'DATA')]
a.datas += [('warning.ico', 'warning.ico', 'DATA')]

#Se incluyen ficheros extras para que tome el tema de windows WIMP
a.binaries += [(r'lib\gtk-2.0\2.10.0\engines\libwimp.dll', r'C:\Python27\Lib\site-packages\gtk-2.0\runtime\lib\gtk-2.0\2.10.0\engines\libwimp.dll', 'BINARY') ]
a.binaries += [('gtkrc', r'C:\Python27\Lib\site-packages\gtk-2.0\runtime\share\themes\MS-Windows\gtk-2.0\gtkrc', 'DATA')]
			 
exe = EXE(pyz,
          a.scripts,
          #exclude_binaries=True,
          a.binaries,
          a.zipfiles,		  
          name='Concesionario',
          debug=False,
          strip=None,
          upx=True,
          console=True, #Se puede poner a True/False
		  icon=['coche.ico']
		  )
		  
coll = COLLECT(exe,
               #a.binaries, # Quito los binarios
               #a.zipfiles, # Quito los comprimidos
               a.datas,			   
               strip=None,
               upx=True,
               name='Concesionario')
