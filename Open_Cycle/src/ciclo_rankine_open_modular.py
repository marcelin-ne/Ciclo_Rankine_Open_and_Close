import CoolProp.CoolProp as CP
from CoolProp.CoolProp import PropsSI
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
        
        # ---------------------CALCULO DE ENTROPIAS----------------------------

    def calculo_ciclo_rankine_in_precal_open_water(self,P_baja, P_intermedia, P_alta, Tsal_cald, ns_turb, ns_bomba, T_0, P_O):
        # Especifica la sustancia como "Water"
        sustancia = "Water"
        # Definir las propiedades de entrada
        x1 = 0
        P1 = P_baja*1000
        P2 = P_intermedia*1000
                 

        # h1
        x1 = 0
        P1 = P_baja*1000                                                 # Pa
        h1 = PropsSI("H", "Q", x1, "P", P1, sustancia)    

        # h2
        ve1 = 1/PropsSI("D", "Q", x1, "P", P1, sustancia)                # m3/kg
        P2 = P_intermedia*1000                                           # Pa
        w_bomba1 = ve1*((P2-P1))/ns_bomba                                # J/kg
        h2 = w_bomba1 + h1                                               # J/kg

        # h3
        P3 = P_intermedia*1000                                           # Pa
        x3 = 0
        h3 = PropsSI("H", "Q", x3, "P", P3, sustancia)                   # J/kg

        # h4
        ve3 = 1/PropsSI("D", "Q", x3, "P", P3, sustancia)                # m3/kg
        P4 = P_alta*1000                                                 # Pa
        w_bomba2 = ve3*(P4-P3)/ns_bomba                                  # J/kg
        h4 = w_bomba2 + h3                                               # J/kg

        # h5
        T5 = Tsal_cald                                                   # °C
        P5 = P_alta*1000                                                 # Pa 
        h5 = PropsSI("H", "T", T5 + 273.15, "P", P5, sustancia)          # J/kg 
        s5 = PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)          # J/kg K

        # h6
        s6 = s5                                                          # J/kg K 
        P6 = P_intermedia*1000                                           # Pa
        h6s = PropsSI("H", "S", s6, "P", P6, sustancia)                  # J/kg
        h6 = h5-(ns_turb*(h5-h6s))                                           # J/kg

        # h7
        P7 = P_baja*1000                                                 # Pa
        s7 = s5                                                          # J/kg K
        h7s = PropsSI("H", "P", P7, "S", s7, sustancia)                  # J/kg                                         # kJ/kg 
        h7 = h5-(ns_turb*(h5-h7s))                                       # J/kg
        
        # Fraccion de vapor
        y = (h3-h2)/(h6-h2)

        # a) Calor añadido
        qan = 1*(h5-h4)                                                  # J/kg
                  
        # b) calor rechazado qout=h7-h1
        qrech = (1-y)*(h7-h1)                                            # J/kg 
        
        # c) Trabajo de la turbina
        w_tap = h5-h6                                                    # J/kg
        w_bap = (1-y)*(h6-h7)                                            # J/kg
        ws_turb = 1*(h5-h6)+(1-y)*(h6-h7)                                # J/kg
        w_turb = ns_turb*ws_turb                                         # J/kg
        
        # d) Trabajo neta de las bombas BBP y BAP
        w_netobombas = w_bomba1+w_bomba2                                 # J/kg

        # e) trabajo neto
        wneto = qan-qrech                                                # J/Kg
        wneto= self.format_result(wneto)
        self.results['wneto'] = wneto

        # e) Calor en el intercambiador
        qint =(1-y)*(h6-h3)                                              # J/kg
        qint= self.format_result(qint)
        self.results['qint'] = qint

        # f) eficiencia termica
        n = 100*(1-qrech/qan)
        n= self.format_result(n*1000)
        self.results['n'] = n
        wbap = self.format_result(w_bomba2)
        self.hs['w_bomba2'] = w_bomba2
        wbbp = self.format_result(w_bomba1)
        self.results['w_bomba1'] = w_bomba1
        
        
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
        qan= self.format_result(qan)
        self.results['qan'] = qan
        qrech= self.format_result(qrech)
        self.results['qrech']= qrech
        ws_turb= self.format_result(ws_turb)
        self.results['ws_turb'] = ws_turb
        w_turb= self.format_result(w_turb)
        self.results['w_turb'] = w_turb
        
        # ------------------CALCULO DE ENTROPIAS-------------------------------
    
    def calculo_entropias(self,P_baja, P_intermedia, P_alta, Tsal_cald, ns_turb, ns_bomba, T_0, P_O):
        # Especifica la sustancia como "Water"
        sustancia = "Water"
        # Definir las propiedades de entrada
        x1 = 0
        P1 = P_baja*1000
        P2 = P_intermedia*1000
                  
    
        # h1
        x1 = 0
        P1 = P_baja*1000                                                 # Pa
        s1 = PropsSI("S", "Q", x1, "P", P1, sustancia)                   # J/kg K
        h1 = PropsSI("H", "Q", x1, "P", P1, sustancia)                   # J/kg
    
        # h2
        ve1 = 1/PropsSI("D", "Q", x1, "P", P1, sustancia)                # m3/kg
        P2 = P_intermedia*1000                                           # Pa
        w_bomba1 = ve1*((P2-P1))/ns_bomba                                # J/kg
        h2 = w_bomba1 + h1                                               # J/kg
        s2 = PropsSI("S", "H", h2, "P", P2, sustancia)                   # J/kg K
    
        # h3
        P3 = P_intermedia*1000                                           # Pa
        x3 = 0
        h3 = PropsSI("H", "Q", x3, "P", P3, sustancia)                   # J/kg
        s3 = PropsSI("S", "Q", x3, "P", P3, sustancia)                   # J/kg K
    
        # h4
        ve3 = 1/PropsSI("D", "Q", x3, "P", P3, sustancia)                # m3/kg
        P4 = P_alta*1000                                                 # Pa
        w_bomba2 = ve3*(P4-P3)/ns_bomba                                  # J/kg
        h4 = w_bomba2 + h3                                               # J/kg
        s4 = PropsSI("S", "H", h4, "P", P4, sustancia)                   # J/kg K
    
        # h5
        T5 = Tsal_cald                                                   # °C
        P5 = P_alta*1000                                                 # Pa 
        h5 = PropsSI("H", "T", T5 + 273.15, "P", P5, sustancia)          # J/kg 
        s5 = PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)          # J/kg K
    
        # h6
        s6s = s5                                                         # J/kg K 
        P6 = P_intermedia*1000                                           # Pa
        h6s = PropsSI("H", "S", s6s, "P", P6, sustancia)                 # J/kg
        h6 = h5-(ns_turb*(h5-h6s))                                       # J/kg
        s6 = PropsSI("S", "H", h6, "P", P6, sustancia)                   # J/kg K
         
        # h7
        P7 = P_baja*1000                                                 # Pa
        s7s = s5                                                         # J/kg K
        h7s = PropsSI("H", "P", P7, "S", s7s, sustancia)                 # J/kg                                         # kJ/kg 
        h7 = h5-(ns_turb*(h5-h7s))                                       # J/kg
        s7 = PropsSI("S", "H", h7, "P", P7, sustancia)                   # J/kg K
         
        # Fraccion de vapor
        y = (h3-h2)/(h6-h2)
    
        # a) Calor añadido
        qan = 1*(h5-h4)                                                  # J/kg
                   
        # b) calor rechazado qout=h7-h1
        qrech = (1-y)*(h7-h1)                                            # J/kg 
         
        # c) Trabajo de la turbina
        w_tap = h5-h6                                                    # J/kg
        w_bap = (1-y)*(h6-h7)                                            # J/kg
        ws_turb = 1*(h5-h6)+(1-y)*(h6-h7)                                # J/kg
        w_turb = ns_turb*ws_turb                                         # J/kg
        
        # d) Trabajo neta de las bombas BBP y BAP
        w_netobombas = w_bomba1+w_bomba2                                 # J/kg
    
        # e) trabajo neto
        wneto = qan-qrech                                                # J/Kg
        wneto= self.format_result(wneto)
        self.results['wneto'] = wneto
    
        # e) Calor en el intercambiador
        qint =(1-y)*(h6-h3)                                              # J/kg
        qint= self.format_result(qint)
        self.results['qint'] = qint
    
        # f) eficiencia termica
        n = 100*(1-qrech/qan)
        n= self.format_result(n*1000)
        self.results['n'] = n
        wbap = self.format_result(w_bomba2)
        self.hs['w_bomba2'] = w_bomba2
        wbbp = self.format_result(w_bomba1)
        self.results['w_bomba1'] = w_bomba1
        
        s1=self.format_result(s1)
        self.ss['s1'] = s1
        s2= self.format_result(s2)
        self.ss['s2'] = s2
        s3 = self.format_result(s3)
        self.ss['s3'] = s3
        s4 = self.format_result(s4)
        self.ss['s4'] = s4
        s5= self.format_result(s5)
        self.ss['s5'] = s5
        s6 = self.format_result(s6)
        self.ss['s6'] = s6
        s7= self.format_result(s7)
        self.ss['s7'] = s7
        qan= self.format_result(qan)
        self.results['qan'] = qan
        qrech= self.format_result(qrech)
        self.results['qrech']= qrech
        ws_turb= self.format_result(ws_turb)
        self.results['ws_turb'] = ws_turb
        w_turb= self.format_result(w_turb)
        self.results['w_turb'] = w_turb
     
        
        # --------------------CALCULO DE EXERGIAS------------------------------
    def format_result(self,exx):
            return "{:.2f}".format(exx/1000)
        

    def calculo_exergias(self, P_baja, P_intermedia, P_alta, Tsal_cald, ns_turb, ns_bomba, T_0, P_O):
        # Especifica la sustancia como "Water"
        sustancia = "Water"
        # Definir las propiedades de entrada
        x1 = 0
        P1 = P_baja*1000
        P2 = P_intermedia*1000
        h0 = PropsSI("H", "P", P_O, "T", T_0+273.15, sustancia)  # J/kg    
        s0 = PropsSI("S", "P", P_O, "T", T_0+273.15, sustancia)  # J/kg K

        # h1
        x1 = 0
        P1 = P_baja*1000                                                 # Pa
        s1 = PropsSI("S", "Q", x1, "P", P1, sustancia)                   # J/kg K
        h1 = PropsSI("H", "Q", x1, "P", P1, sustancia)                   # J/kg
    
        # h2
        ve1 = 1/PropsSI("D", "Q", x1, "P", P1, sustancia)                # m3/kg
        P2 = P_intermedia*1000                                           # Pa
        w_bomba1 = ve1*((P2-P1))/ns_bomba                                # J/kg
        h2 = w_bomba1 + h1                                               # J/kg
        s2 = PropsSI("S", "H", h2, "P", P2, sustancia)                   # J/kg K
    
        # h3
        P3 = P_intermedia*1000                                           # Pa
        x3 = 0
        h3 = PropsSI("H", "Q", x3, "P", P3, sustancia)                   # J/kg
        s3 = PropsSI("S", "Q", x3, "P", P3, sustancia)                   # J/kg K
    
        # h4
        ve3 = 1/PropsSI("D", "Q", x3, "P", P3, sustancia)                # m3/kg
        P4 = P_alta*1000                                                 # Pa
        w_bomba2 = ve3*(P4-P3)/ns_bomba                                  # J/kg
        h4 = w_bomba2 + h3                                               # J/kg
        s4 = PropsSI("S", "H", h4, "P", P4, sustancia)                   # J/kg K
    
        # h5
        T5 = Tsal_cald                                                   # °C
        P5 = P_alta*1000                                                 # Pa 
        h5 = PropsSI("H", "T", T5 + 273.15, "P", P5, sustancia)          # J/kg 
        s5 = PropsSI("S", "T", T5 + 273.15, "P", P5, sustancia)          # J/kg K
    
        # h6
        s6s = s5                                                         # J/kg K 
        P6 = P_intermedia*1000                                           # Pa
        h6s = PropsSI("H", "S", s6s, "P", P6, sustancia)                 # J/kg
        h6 = h5-(ns_turb*(h5-h6s))                                       # J/kg
        s6 = PropsSI("S", "H", h6, "P", P6, sustancia)                   # J/kg K
         
        # h7
        P7 = P_baja*1000                                                 # Pa
        s7s = s5                                                         # J/kg K
        h7s = PropsSI("H", "P", P7, "S", s7s, sustancia)                 # J/kg                                         # kJ/kg 
        h7 = h5-(ns_turb*(h5-h7s))                                       # J/kg
        s7 = PropsSI("S", "H", h7, "P", P7, sustancia)                   # J/kg K
        
        ex1 = (h1-h0)-(T_0+273.15)*(s1-s0)                               # J/kg                          
        ex2 = (h2-h0)-(T_0+273.15)*(s2-s0)                               # J/kg
        ex3 = (h3-h0)-(T_0+273.15)*(s3-s0)                               # J/kg
        ex4 = (h4-h0)-(T_0+273.15)*(s4-s0)                               # J/kg
        ex5 = (h5-h0)-(T_0+273.15)*(s5-s0)                               # J/kg
        ex6 = (h6-h0)-(T_0+273.15)*(s6-s0)                               # J/kg
        ex7 = (h7-h0)-(T_0+273.15)*(s7-s0)                               # J/kg
        
        # Fraccion de vapor
        y = (h3-h2)/(h6-h2)

        # a) Calor añadido
        qan = 1*(h5-h4)                                                  # J/kg
                  
        # b) calor rechazado qout=h7-h1
        qrech = (1-y)*(h7-h1)                                            # J/kg 
        
        # c) Trabajo de la turbina
        w_tap = h5-h6                                                    # J/kg
        w_bap = (1-y)*(h6-h7)                                            # J/kg
        ws_turb = 1*(h5-h6)+(1-y)*(h6-h7)                                # J/kg
        w_turb = ns_turb*ws_turb                                         # J/kg
        
        # d) Trabajo neta de las bombas BBP y BAP
        w_netobombas = w_bomba1+w_bomba2                                 # J/kg

        # e) trabajo neto
        wneto = qan-qrech                                                # J/Kg
        wneto= self.format_result(wneto)
        self.results['wneto'] = wneto

        # e) Calor en el intercambiador
        qint =(1-y)*(h6-h3)                                              # J/kg
        qint= self.format_result(qint)
        self.results['qint'] = qint

        # f) eficiencia termica
        n = 100*(1-qrech/qan)
        n= self.format_result(n*1000)
        self.results['n'] = n
        wbap = self.format_result(w_bomba2)
        self.hs['w_bomba2'] = w_bomba2
        wbbp = self.format_result(w_bomba1)
        self.results['w_bomba1'] = w_bomba1
        
        
        ex1=self.format_result(ex1)
        self.exs['ex1'] = ex1
        ex2= self.format_result(ex2)
        self.exs['ex2'] = ex2
        ex3 = self.format_result(ex3)
        self.exs['ex3'] = ex3
        ex4 = self.format_result(ex4)
        self.exs['ex4'] = ex4
        h5= self.format_result(h5)
        self.exs['ex5'] = ex5
        ex6 = self.format_result(ex6)
        self.exs['ex6'] = ex6
        ex7= self.format_result(ex7)
        self.hs['ex7'] = ex7
        qan= self.format_result(qan)
        self.results['qan'] = qan
        qrech= self.format_result(qrech)
        self.results['qrech']= qrech
        ws_turb= self.format_result(ws_turb)
        self.results['ws_turb'] = ws_turb
        w_turb= self.format_result(w_turb)
        self.results['w_turb'] = w_turb
        


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
#    def get_limits_nt(self):
#        return [0.2, 1]
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
