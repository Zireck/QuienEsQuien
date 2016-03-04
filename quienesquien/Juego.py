# -*- coding: iso-8859-1 -*-
'''
Created on 13 de feb. de 2016

@author: Andrés Hernández
'''
import random
from Hombre import Hombre
from Mujer import Mujer
from RegistroRanking import RegistroRanking
from RankingManager import RankingManager

class Juego(object):
    
    def __init__(self):
        self.__personas = []
        self.__personasCandidatas = []
        self.__personaEnJuego = None
        self.__numeroPreguntas = 0
        self.__preguntasFormuladas = {}
        self.__preguntaRepetida = False
        self.__preguntaInvalida = False
        self.__caracteristicasAcertadas = {}
        self.__caracteristicasErradas = {}
        self.__numeroAciertos = 0
        self.__adivinoPersonaje = False
        self.__rankingManager = RankingManager()
    
    def cargarPersonas(self):
        self.__personas = []
        try:
            file = open('personajes.txt', 'r')
            for linea in file:
                if 'hombre' in linea.lower():
                    persona = Hombre()
                else:
                    persona = Mujer()
                
                persona.cargarDatos(linea)
                self.__personas.append(persona)
        except (IOError, OSError):
            print('\nError leyendo el fichero personajes.txt')
        finally:
            file.close()
            
    def visualizarPersonas(self):
        for persona in self.__personas:
            print(persona)
            
    def generarPersonaAleatoria(self):
        return random.choice(self.__personas)
        
    def esUnaPregunta(self, linea):
        return True if linea[0] == '¿' and linea[-1] == '?' else False 
        
    def intentaResolver(self, linea):
        return True if 'LA PERSONA ES '.lower() in linea.strip().lower() else False
    
    def inicializarPreguntasFormuladas(self):
        self.__preguntasFormuladas = {}
        self.__preguntasFormuladas['sexo'] = False
        self.__preguntasFormuladas['colorPelo'] = False
        self.__preguntasFormuladas['colorOjos'] = False
        self.__preguntasFormuladas['estatura'] = False
        self.__preguntasFormuladas['nacionalidad'] = False
        self.__preguntasFormuladas['profesion'] = False
        self.__preguntasFormuladas['estadoCivil'] = False
        self.__preguntasFormuladas['tieneHijos'] = False
        self.__preguntasFormuladas['llevaGafas'] = False
        self.__preguntasFormuladas['llevaBigote'] = False
    
    def comprobarPreguntaRepetida(self, caracteristicaPreguntada):
        if self.__preguntasFormuladas[caracteristicaPreguntada]:
            self.__preguntaRepetida = True
        self.__preguntasFormuladas[caracteristicaPreguntada] = True
        
    def procesarPregunta(self, pregunta):
        pregunta = pregunta.replace('?', '').lower()
        valor = pregunta.split()[-1]
        if any(palabra in pregunta for palabra in ('sexo', 'hombre', 'mujer')):
            self.comprobarPreguntaRepetida('sexo')
            
            if 'hombre' in valor:
                if isinstance(self.__personaEnJuego, Hombre):
                    respuestaEsCorrecta = True
                    self.mantenerHombres()
                else:
                    respuestaEsCorrecta = False
                    self.descartarHombres()
            else:
                if isinstance(self.__personaEnJuego, Mujer):
                    respuestaEsCorrecta = True
                    self.mantenerMujeres()
                else:
                    respuestaEsCorrecta = False
                    self.descartarMujeres()
            
            return respuestaEsCorrecta
        elif any(palabra in pregunta for palabra in('pelo', 'rubio', 'moreno', 'castaño', 'pelirrojo')):
            self.comprobarPreguntaRepetida('colorPelo')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarColorPelo(valor)
            if respuestaEsCorrecta:
                self.mantenerPersonas('colorPelo', valor)
            else:
                self.descartarPersonas('colorPelo', valor)
            return respuestaEsCorrecta
        elif 'ojos' in pregunta:
            self.comprobarPreguntaRepetida('colorOjos')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarColorOjos(valor)
            if respuestaEsCorrecta:
                self.mantenerPersonas('colorOjos', valor)
            else:
                self.descartarPersonas('colorOjos', valor)
            return respuestaEsCorrecta
        elif any(palabra in pregunta for palabra in ('profesion', 'trabajo', 'trabaja', 'curra')):
            self.comprobarPreguntaRepetida('profesion')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarProfesion(valor)
            if respuestaEsCorrecta:
                self.mantenerPersonas('profesion', valor)
            else:
                self.descartarPersonas('profesion', valor)
            return respuestaEsCorrecta
        elif any(palabra in pregunta for palabra in('estatura', 'alta', 'baja')):
            self.comprobarPreguntaRepetida('estatura')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarEstatura(valor)
            if respuestaEsCorrecta:
                self.mantenerPersonas('estatura', valor)
            else:
                self.descartarPersonas('estatura', valor)
            return respuestaEsCorrecta
        elif 'nacionalidad' in pregunta:
            self.comprobarPreguntaRepetida('nacionalidad')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarNacionalidad(valor)
            if respuestaEsCorrecta:
                self.mantenerPersonas('nacionalidad', valor)
            else:
                self.descartarPersonas('nacionalidad', valor)
            return respuestaEsCorrecta
        elif any(palabra in pregunta for palabra in ('estado', 'civil', 'estado civil', 'casado', 'soltero')):
            self.comprobarPreguntaRepetida('estadoCivil')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarEstadoCivil(valor)
            if respuestaEsCorrecta:
                self.mantenerPersonas('estadoCivil', valor)
            else:
                self.descartarPersonas('estadoCivil', valor)
            return respuestaEsCorrecta
        elif 'hijos' in pregunta:
            self.comprobarPreguntaRepetida('tieneHijos')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarTieneHijos()
            if respuestaEsCorrecta:
                self.mantenerPersonas('tieneHijos', 'si')
            else:
                self.descartarPersonas('tieneHijos', 'si')
            return respuestaEsCorrecta
        elif 'gafas' in pregunta:
            self.comprobarPreguntaRepetida('llevaGafas')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarLlevaGafas()
            if respuestaEsCorrecta:
                self.mantenerPersonas('llevaGafas', 'si')
            else:
                self.descartarPersonas('llevaGafas', 'si')
            return respuestaEsCorrecta
        elif 'bigote' in pregunta:
            self.comprobarPreguntaRepetida('llevaBigote')
            
            respuestaEsCorrecta = self.__personaEnJuego.comprobarLlevaBigote()
            if respuestaEsCorrecta:
                self.mantenerPersonas('llevaBigote', 'si')
            else:
                self.descartarPersonas('llevaBigote', 'si')
            return respuestaEsCorrecta
            
        print('> Pregunta no reconocida.')
        self.__preguntaInvalida = True
            
        return False
        
    def resolver(self, pregunta):
        persona = pregunta.split()[-1].strip().lower()
        return True if persona in self.__personaEnJuego.nombre else False
    
    def mantenerPersonas(self, caracteristica, valor):
        for persona in list(self.__personas):
            if not persona.comprobar(caracteristica, valor):
                self.__personas.remove(persona)
    
    def descartarPersonas(self, caracteristica, valor):
        for persona in list(self.__personas):
            if persona.comprobar(caracteristica, valor):
                self.__personas.remove(persona)
                
    def mantenerHombres(self):
        for persona in list(self.__personas):
            if not isinstance(persona, Hombre):
                self.__personas.remove(persona)
        
    def descartarHombres(self):
        for persona in list(self.__personas):
            if isinstance(persona, Hombre):
                self.__personas.remove(persona)
    
    def mantenerMujeres(self):
        for persona in list(self.__personas):
            if not isinstance(persona, Mujer):
                self.__personas.remove(persona)

    def descartarMujeres(self):
        for persona in list(self.__personas):
            if isinstance(persona, Mujer):
                self.__personas.remove(persona)
    
    def visualizarPersonasCandidatas(self):
        print('\nPersonajes candidatos: ')
        for candidata in self.__personas:
            print(candidata)
                    
    def preguntarNuevaPartida(self):
        respuesta = None
        while respuesta not in ('y', 'n'):
            respuesta = input('\n¿Desea jugar una nueva partida? (y/n)')
            if respuesta == 'y':
                return True
            elif respuesta == 'n':
                return False
            
    def jugarPartida(self):
        self.__numeroAciertos = 0
        self.inicializarPreguntasFormuladas()
        self.__preguntaRepetida = False
        self.__caracteristicasAcertadas = {}
        self.__personasCandidatas = []
        self.__adivinoPersonaje = False
        self.cargarPersonas()
        
        print('\nVisualización inicial de todos los personajes:')
        self.visualizarPersonas()
        
        input('\nPulsa un tecla para comenzar el juego....')
        
        print('\nPersona en juego:')
        self.__personaEnJuego = self.generarPersonaAleatoria()
        print(self.__personaEnJuego)
        
        print('\nComenzando juego.')
        
        self.__numeroPreguntas = 0
        fin = False
        acertado = False
        self.__preguntaInvalida = False
        while not fin and self.__numeroPreguntas < 10:
            if not self.__preguntaInvalida:
                self.__numeroPreguntas += 1
                
            self.visualizarPersonasCandidatas()
        
            self.__preguntaInvalida = False
            pregunta = input('\n> Pregunta %d:\n' % self.__numeroPreguntas)
            if not pregunta or (not self.esUnaPregunta(pregunta) and not self.intentaResolver(pregunta)):
                print('Pregunta inválida.')
                self.__preguntaInvalida = True
            else:
                if self.esUnaPregunta(pregunta):
                    if self.procesarPregunta(pregunta):
                        if self.__preguntaRepetida:
                            self.__preguntaRepetida = False
                            print('> Pregunta repetida.')
                        else:
                            self.__numeroAciertos += 1
                            
                        print('> Respuesta: Sí.')
                    else:
                        if self.__preguntaRepetida:
                            self.__preguntaRepetida = False
                            print('> Pregunta repetida.')
                            
                        print('> Respuesta: No.')
                elif self.intentaResolver(pregunta):
                    fin = True
                    if self.resolver(pregunta):
                        acertado = True
                        self.__adivinoPersonaje = True
                        print('> ¡Has acertado!')
                    else:
                        self.__adivinoPersonaje = False
                        print('> ¡Has fallado!')
        
        if acertado:
            print('\nFin del juego: Has ganado.')
        else:
            print('\nFin del juego: Has perdido.')
        
    def gestionarRanking(self):
        iniciales = input('\nIntroduce tus iniciales: ')
        while not iniciales or len(iniciales) <= 0 or len(iniciales) > 3:
            iniciales = input('\nIntroduce correctamente tus iniciales (3 caracteres como máximo): ')
            
        puntuacion = iniciales + ', número preguntas: ' + str(self.__numeroPreguntas) + ', adivinó personaje: ' + ('si' if self.__adivinoPersonaje else 'no')
        print(puntuacion)
        
        registroActual = RegistroRanking()
        registroActual.nombre = iniciales
        registroActual.numeroPreguntas = self.__numeroPreguntas
        registroActual.adivinoPersonaje = self.__adivinoPersonaje
        
        self.__rankingManager.cargarRegistros()
        self.__rankingManager.insertarRegistro(registroActual)
        self.__rankingManager.guardarRegistros()
         
    
    def jugar(self):
        self.jugarPartida()
        self.gestionarRanking()
        
    def verRanking(self):
        self.__rankingManager.cargarRegistros()
        self.__rankingManager.guardarRegistros()
        self.__rankingManager.visualizarRegistros()
            
    def mostrarMenu(self):
        opcion = None
        continuar = True
        while continuar or not opcion or opcion not in ('1', '2', '3'):
            print('\n')
            print('1. Jugar')
            print('2. Ver Ranking')
            print('3. Salir')
            opcion = input('Selecciona una opción: ')
            if opcion in '1':
                self.jugar()
            elif opcion in '2':
                self.verRanking()
            elif opcion in '3':
                continuar = False
        
        