# -*- coding: iso-8859-1 -*-
'''
Created on 11/2/2016

@author: Andrés Hernández
'''

class Persona(object):
    
    def __init__(self):
        self._nombre = None
        self.caracteristicas = {}
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def colorPelo(self):
        return self.caracteristicas['colorPelo']
    
    @property
    def colorOjos(self):
        return self.caracteristicas['colorOjos']
    
    @property
    def estatura(self):
        return self.caracteristicas['estatura']
    
    @property
    def nacionalidad(self):
        return self.caracteristicas['nacionalidad']
    
    @property
    def profesion(self):
        return self.caracteristicas['profesion']
    
    @property
    def estadoCivil(self):
        return self.caracteristicas['estadoCivil']
    
    @property
    def tieneHijos(self):
        return self.caracteristicas['tieneHijos']
    
    @property
    def llevaGafas(self):
        return self.caracteristicas['llevaGafas']
    
    @property
    def llevaBigote(self):
        return self.caracteristicas['llevaBigote']
        
    def cargarDatos(self, linea):
        linea = linea.lower()
        self._nombre = linea.split(',')[0].strip()
        self.caracteristicas['colorPelo'] = linea.split(',')[2].strip()
        self.caracteristicas['colorOjos'] = linea.split(',')[3].strip()
        self.caracteristicas['estatura'] = linea.split(',')[4].strip()
        self.caracteristicas['nacionalidad'] = linea.split(',')[5].strip()
        self.caracteristicas['profesion'] = linea.split(',')[6].strip()
        self.caracteristicas['estadoCivil'] = linea.split(',')[7].strip()
        self.caracteristicas['tieneHijos'] = linea.split(',')[8].strip()
        self.caracteristicas['llevaGafas'] = linea.split(',')[9].strip()
        self.caracteristicas['llevaBigote'] = linea.split(',')[10].strip()
        
    def comprobarColorPelo(self, colorPelo):
        return self.comprobar('colorPelo', colorPelo)
    
    def comprobarColorOjos(self, colorOjos):
        return self.comprobar('colorOjos', colorOjos)
    
    def comprobarEstatura(self, estatura):
        return self.comprobar('estatura', estatura)
    
    def comprobarNacionalidad(self, nacionalidad):
        return self.comprobar('nacionalidad', nacionalidad)
    
    def comprobarProfesion(self, profesion):
        return self.comprobar('profesion', profesion)
    
    def comprobarEstadoCivil(self, estadoCivil):
        return True if self.caracteristicas['estadoCivil'].lower()[:-1] in estadoCivil.lower() else False
    
    def comprobarTieneHijos(self):
        return self.comprobar('tieneHijos', 'si')
    
    def comprobarLlevaGafas(self):
        return self.comprobar('llevaGafas', 'si')
    
    def comprobarLlevaBigote(self):
        return self.comprobar('llevaBigote', 'si')
        
    def comprobar(self, caracteristica, valor):
        return True if self.caracteristicas[caracteristica].lower() in valor.lower() else False