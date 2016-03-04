# -*- coding: iso-8859-1 -*-
'''
Created on 14 de feb. de 2016

@author: Andrés Hernández
'''
import os.path
from RegistroRanking import RegistroRanking

class RankingManager(object):
    
    __rankingHeader = 'PUESTO' + ('.' * 5) + 'NOMBRE' + ('.' * 5) + 'NÚM.PREG' + ('.' * 5) + 'ADIVINÓ PERSONAJE'
    
    def __init__(self):
        self.__registros = []
        self.crearFichero()
        self.cargarRegistros()
                
    def crearFichero(self):
        if not os.path.isfile('ranking.txt'):
            try:
                file = open('ranking.txt', 'w')
            except (IOError, OSError):
                print('\nError creando el fichero ranking.txt')
            finally:
                file.close()
                
    def cargarRegistros(self):
        self.__registros = []
        try:
            with open('ranking.txt', 'r') as file:
                n = 0
                for linea in file:
                    n += 1
                    if n == 1:
                        continue
                    registro = RegistroRanking()
                    registro.cargarDatos(linea)
                    self.__registros.append(registro)
        except (IOError, OSError):
            print('\nError leyendo el fichero ranking.txt')
        finally:
            file.close()
            
    def visualizarRegistros(self):
        print('\n')
        print(self.__rankingHeader)
        for registro in self.__registros:
            print(registro)
            
    def insertarRegistro(self, registro):
        self.__registros.append(registro)
            
    def ordenarRegistros(self):
        self.__registros.sort(key=lambda registro: (registro.adivinoPersonaje , -registro.numeroPreguntas), reverse=True)
        
    def establecerPuestos(self):
        puesto = 1
        for registro in self.__registros:
            registro.puesto = puesto
            puesto += 1
        
    def guardarRegistros(self):
        self.ordenarRegistros()
        self.establecerPuestos()
        try:
            with open('ranking.txt', 'w') as file:
                file.write(self.__rankingHeader)
                for registro in self.__registros:
                    file.write('\n')
                    file.write(str(registro))
        except (IOError, OSError):
            print('\nError escribiendo el fichero ranking.txt')
        finally:
            file.close()
        