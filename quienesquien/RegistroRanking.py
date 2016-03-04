# -*- coding: iso-8859-1 -*-
'''
Created on 13 de feb. de 2016

@author: Andrés Hernández
'''
class RegistroRanking(object):
    
    def __init__(self):
        self.__puesto = 0
        self.__nombre = None
        self.__numeroPreguntas = 0
        self.__adivinoPersonaje = False
    
    @property
    def puesto(self):
        return self.__puesto
    
    @puesto.setter
    def puesto(self, value):
        self.__puesto = value
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @property
    def numeroPreguntas(self):
        return self.__numeroPreguntas
    
    @numeroPreguntas.setter
    def numeroPreguntas(self, value):
        self.__numeroPreguntas = value
        
    @property
    def adivinoPersonaje(self):
        return self.__adivinoPersonaje
    
    @adivinoPersonaje.setter
    def adivinoPersonaje(self, value):
        self.__adivinoPersonaje = value
    
    def cargarDatos(self, registro):
        registro = registro.strip().lower()
        valores = [valor.strip() for valor in registro.split('.') if valor]
        self.__puesto = int(valores[0])
        self.__nombre = valores[1]
        self.__numeroPreguntas = int(valores[2])
        self.__adivinoPersonaje = (True if valores[3] in 'si' else False)
        
    def __str__(self):
        return (('%s' + ('.' * 10) + '%s' + ('.' * 8) + '%s' + ('.' * 13) + '%s') % (self.__puesto, self.__nombre, str(self.__numeroPreguntas), ('SI' if self.__adivinoPersonaje else 'NO')))