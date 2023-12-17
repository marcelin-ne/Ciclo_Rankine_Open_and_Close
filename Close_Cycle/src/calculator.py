from CoolProp.CoolProp import PropsSI
import numpy as np
import matplotlib.pyplot as plt


# Ciclo ideal Rankine  con un calentador cerrado de agua dealimentación y recalentamiento
class Rankine_P_Close:
    def __init__(self, hs: dict, results: dict):
        """
        Constructor de la clase Rankine_P_Open.

        :param hs: Un diccionario de valores hs.
        :type hs: dict
        :param results: Un diccionario de resultados.
        :type results: dict
        """
        self.hs = hs
        self.results = results
#Metods
    def format_result(self,hx):
            return "{:.2f}".format(hx/1000)

    def calc_ciclo_rankine_in_precal_close_water(self,p1, x1, p2, p3, x3, T6,nb,nt):
        # Definir las propiedades de entrada
        p4 = p2 # Presión a la salida de la segunda bomba
        p5 = p2 # Presión a la entrada de la caldera en Pa
        p6 = p5 # Presión a la entrada de la turbina en Pa
        p7 = p3 # Presión a la salida de la turbina hacia el calentador de agua de alimentacion en Pa
        p8 = p1 # Presión a la salida de la turbina hacia el condensador en Pa
        p9 = p2 # Presión a la salida del CAA cerrado
        mp = 15 
        # Calcular laS propiedades en cada punto del ciclo
        h1 = PropsSI('H', 'Q', x1, 'P', p1, 'Water')
        s1 = PropsSI('S', 'Q', x1, 'P', p1, 'Water')
        h2s = PropsSI('H', 'S', s1, 'P', p2, 'Water')
        wb1 = (h2s-h1)/nb # Trabajo de la bomba 1
        h2 = h1+wb1
        h3 = PropsSI('H', 'Q', x3, 'P', p3, 'Water')
        s3 = PropsSI('S', 'Q', x3, 'P', p3, 'Water')
        h4s = PropsSI('H', 'S', s3, 'P', p4, 'Water')
        wb2 = (h4s-h3)/nb # Trabajo de la bomba 2
        h4 = h3+wb2
        h9 = h3
        h6 = PropsSI('H', 'T', T6+273.15, 'P', p6, 'Water')
        s6 = PropsSI('S', 'T', T6+273.15, 'P', p6, 'Water')
        h6s = PropsSI('H', 'S', s6, 'P', p6, 'Water')
        h7s = PropsSI('H', 'S', s6, 'P', p7, 'Water')
        h7=h6-nt*(h6-h7s)
        y  = (h9-h2)/(h7-h3+h9-h2) # Balance energetico en el calentador de aguade alimentación cerrado
        h5 = y*h9+(1-y)*h4
        h8s = PropsSI('H', 'S', s6, 'P', p8, 'Water')
        h8 = h6-nt*(h6-h8s)
        # Calcular la eficiencia térmica y el trabajo neto
        q_in = h6-h5
        q_out = (1-y)*(h8-h1)
        Wnet = mp*(q_in-q_out) # Balance energético del sistema
        eta = 1- (q_out/ q_in)
        #Formatear y guardar en el diccionario
        h1=self.format_result(h1)
        self.hs['h1'] = h1
        h2s= self.format_result(h2s)
        self.hs['h2s'] = h2s
        h2 = self.format_result(h2)
        self.hs['h2'] = h2
        h3 = self.format_result(h3)
        self.hs['h3'] = h3
        h4s = self.format_result(h4s)
        self.hs['h4s'] = h4s
        h4 = self.format_result(h4)
        self.hs['h4'] = h4
        h9 = self.format_result(h9)
        self.hs['h9'] = h9
        h6 = self.format_result(h6)
        self.hs['h6'] = h6
        h6s= self.format_result(h6s)
        self.hs['h6s'] = h6s
        h7s = self.format_result(h7s)
        self.hs['h7s'] = h7s
        h7= self.format_result(h7)
        self.hs['h7'] = h7
        h5= self.format_result(h5)
        self.hs['h5'] = h5
        h8s= self.format_result(h8s)
        self.hs['h8s'] = h8s
        h8= self.format_result(h8)
        self.hs['h8'] = h8
        Wnet= self.format_result(Wnet)
        self.results['wturb'] = Wnet
        eta= "{0:.2f}".format(eta * 100)
        self.results['eta'] = eta #Eficienci Termica Resultante 

#Return hs and results
    def get_hs(self):
        return self.hs
    def get_results(self):
        return self.results
    
#Set the limits of every variable of the cycle 
#P1
    def get_limits_p1(self):
        return [3, 30]
#P2
    def get_limits_p2(self):
        return [2000, 36000]
#P3
    def get_limits_p3(self):
        return [1000,22000]
#T6
    def get_limits_t6(self):
        return [200, 800]
#nb
    def get_limits_nb(self):
        return [0.2, 1]
#nt
    def get_limits_nt(self):
        return [0.2, 1]