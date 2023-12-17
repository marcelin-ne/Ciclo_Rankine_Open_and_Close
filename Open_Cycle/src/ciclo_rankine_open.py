import CoolProp.CoolProp as CP
import numpy as np
import matplotlib.pyplot as plt


# Ciclo ideal Rankine  con un calentador cerrado de agua dealimentación y recalentamiento
class Ciclo_Rankine_Open:
    def __init__(self, hs: dict, results: dict):
        """
        Constructor de la clase Ciclo_Rankine_Open.

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

    def calculo_ciclo_rankine_in_precal_open_water(self,Pbbp, Pbap, Psal_cald, Tsal_cald, ns_turb, ns_bomba):
        # Especifica la sustancia como "Water"
        sustancia = "Water"
        # Definir las propiedades de entrada
        x1 = 0
        P1 = Pbbp
        P2 = Pbap

        # h1
        x1 = 0
        P1 = Pbbp         # Presion 1                                       # Pa
        h1 = CP.PropsSI("H", "Q", x1, "P", P1, sustancia)    

        # h2
        ve1 = 1/CP.PropsSI("D", "Q", x1, "P", P1, sustancia)                # m3/kg
        P2 = Pbap         # Presion 2                                       # Pa
        wbbp = ve1*((P2-P1))/ns_bomba   
        h2 = (wbbp + h1)

        # h3
        P3 = Pbap         # Presion 3                                        # Pa
        x3 = 0
        h3 = CP.PropsSI("H", "Q", x3, "P", P3, sustancia)                    # J/kg


        # h4
        ve3 = 1/CP.PropsSI("D", "Q", x3, "P", P3, sustancia)                 # m3/kg
        P4 = Psal_cald    # Presion 4                                        # Pa
        wbap = ve3*(P4-P3)/ns_bomba                                         # J/kg
        h4 = wbap + h3


        # h5
        T5 = Tsal_cald                                                       # °C
        P5 = Psal_cald    # Presion 5                                        # Pa 
        h5 = CP.PropsSI("H", "T", T5 + 273.15, "P", P5, sustancia)           # J/kg 
        s5 = CP.PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)           # J/kg K


        # h6
        s6 = s5                                                              # J/kg K 
        P6 = Pbap         # Presion 6                                        # Pa
        h6s = CP.PropsSI("H", "S", s6, "P", P6, sustancia)                   # J/kg
        h6 = h5-(ns_turb*(h5-h6s))                                           # J/kg


        # h7
        P7 = Pbbp         # Presion 7                                        # Pa
        s7 = s5
        h7s = CP.PropsSI("H", "P", P7, "S", s7, sustancia)                   # J/kg                                         # kJ/kg 
        h7 = h5-(ns_turb*(h5-h7s))                                           # J/kg 


        # a) Calor añadido qin= h5-h4
        qin = h5-h4                   
        # b) calor rechazado qout=h7-h1
        qout = h7-h1                                                    # J/kg 
        
        # c) Trabajo de la turbina
        ws_turb = (h5-h6)+(h5-h7)                                       # J/kg
        wturb = ns_turb*ws_turb
        

        # d) Trabajo neta de las bombas BBP y BAP
        wnetabombas = wbbp+wbap                                          # J/kg

        # e) trabajo neto
        wneto=wturb+wnetabombas
        wneto= self.format_result(wneto)
        self.results['wneto'] = wneto

        # e) Calor en el intercambiador
        qint = h6-h3                                                    # J/kg
        qint= self.format_result(qint)
        self.results['qint'] = qint

        # f) eficiencia termica
        w = wturb+wnetabombas                                           # J/kg
        n = 100*w/qin
        n= self.format_result(n)
        self.results['n'] = n
        wbap = self.format_result(wbap)
        self.hs['wbap'] = wbap
        wbbp = self.format_result(wbbp)
        self.results['wbbp'] = wbbp
        
        
        # CALCULO DE ENTROPIAS
        s1 = CP.PropsSI("S", "Q", x1, "P", P1, sustancia)                    # J/kg K
        s2 = CP.PropsSI("S", "H", h2, "P", P2, sustancia)                    # J/kg K
        s3 = CP.PropsSI("S", "Q", x3, "P", P3, sustancia)                    # J/kg K
        s4 = CP.PropsSI("S", "H", h4, "P", P4, sustancia)                    # J/kg K
        s5 = CP.PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)           # J/kg K
        s6 = s5                                                              # J/kg K
        s7 = s5
        h1=self.format_result(h1)
        self.hs['h1'] = h1
        h2= self.format_result(h2)
        self.hs['h2'] = h2
        h3 = self.format_result(h3)
        self.hs['h3'] = h3
        h4 = self.format_result(h4)
        self.hs['h4'] = h4
        h5= self.format_result(h5)
        self.hs['h5'] = h5
        h6 = self.format_result(h6)
        self.hs['h6'] = h6
        h7= self.format_result(h7)
        self.hs['h7'] = h7
        qin= self.format_result(qin)
        self.results['qin'] = qin
        qout= self.format_result(qout)
        self.results['quot']= qout
        ws_turb= self.format_result(ws_turb)
        self.results['ws_turb'] = ws_turb
        wturb= self.format_result(wturb)
        self.results['wturb'] = wturb


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
# # Example to test the class
# Pbbp=30000        # Pa (Presion bomba baja presion)
# Pbap=1000000      # Pa (Presion bomba alta presion)
# Psal_cald=3000000 # Pa (Presion de salida caldera)
# Tsal_cald=450     # °C (Temperatura de salida caldera)
# ns_turb=0.7       # (Eficiencia turbina isentropica)
# ns_bomba=0.7
# hs = {}
# results = {}
# ciclo_rankine = Ciclo_Rankine_Open(hs, results)
# ciclo_rankine.calculo_ciclo_rankine_in_precal_open_water(Pbbp, Pbap, Psal_cald, Tsal_cald, ns_turb, ns_bomba)
# print(ciclo_rankine.get_hs())
# print(ciclo_rankine.get_results())
