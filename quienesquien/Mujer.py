# -*- coding: iso-8859-1 -*-
'''
Created on 19 de feb. de 2016

@author: Andrés Hernández
'''
from Persona import Persona

class Mujer(Persona):
    
    def __init__(self):
        super().__init__()
        
    def __str__(self):
        cadena = str('Nombre: %s' % self.nombre)
        cadena += str(', sexo: mujer')
        for k, v in self.caracteristicas.items():
            cadena += str(', %s: %s' % (k, v))
        return cadena