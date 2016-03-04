# -*- coding: iso-8859-1 -*-
'''
Created on 19 de feb. de 2016

@author: Andrés Hernández
'''
from Persona import Persona

class Hombre(Persona):
    
    def __init__(self):
        super().__init__()
        
    def __str__(self):
        cadena = str('Nombre: %s' % self.nombre)
        cadena += str(', sexo: hombre')
        for k, v in self.caracteristicas.items():
            cadena += str(', %s: %s' % (k, v))
        return cadena