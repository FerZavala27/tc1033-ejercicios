class Vehiculo():
    def _init_(self,_matricula,_medio,_pasajeros,_velocidad):
        self._matricula=matricula
        self._medio=medio
        self._pasajeros=pasajeros
        self._velocidad=velocidad
        
class Motor():
    def _init_(self,_combustible,_fabricante,_potencia):
        self._combustible=combustible
        self._fabricante=fabricante
        self._potencia=potencia

class Terrestre():
    def _init_(self,_ruedas,_motor,_puertas):
        self._ruedas=ruedas
        self._motor=motor
        self._puertas=puertas

class Marino():
    def _init_(self,_propulsion):
        self._propulsion=propulsion
       
class Aereo():
    def _init_(self,_matricula,_medio,_pasajeros,_velocidad):
        self._matricula=matricula
        self._medio=medio
        self._pasajeros=pasajeros
        self._velocidad=velocidad

class Ruedas():
    def _init_(self,_tamaño,_presion,_fabricante):
        self._tamaño=tamaño
        self._presion=presion
        self._fabricante=fabricante
