from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from ciclo_rankine_open import Ciclo_Rankine_Open


class MainApp(MDApp):
    def build(self):
        #Variables for calculate the cycle
        self.hs = {}
        self.results = {}
        # Window.size = (1000, 900)
        self.theme_cls.theme_style = "Dark"
        #light theme
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('../desing/forms.kv')
        # return Builder.load_file('forms.kv')
    def login(self):
        self.root.ids.welcome_label.text = "Hello " + self.root.ids.user.text
    def clear(self):
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def resolve(self):
        hs_data = {}  # Tu diccionario hs
        results_data = {}  # Tu diccionario de resultados
        ciclo_rankine = Ciclo_Rankine_Open(hs=hs_data, results=results_data)
        #Calculate the cycle with the input variables from the form 
        ciclo_rankine.calculo_ciclo_rankine_in_precal_open_water(float(self.root.ids.Pbbp.text), float(self.root.ids.Pbap.text), float(self.root.ids.Psal_cald.text), float(self.root.ids.Tsal_cald.text), float(self.root.ids.ns_bomba.text), float(self.root.ids.ns_turb.text))
        #Test the calculate in the terminal
        print(ciclo_rankine.hs)
        print(ciclo_rankine.results)
        #Show the results in the front

        #Result 1 : Calor
        self.root.ids.qin.text = str(ciclo_rankine.results['qin'])
        #self.root.ids.quot.text = str(ciclo_rankine.results['quot'])
        self.root.ids.qint.text = str(ciclo_rankine.results['qint'])

        #Trabajo del Ciclo
        self.root.ids.wneto.text = str(ciclo_rankine.results['wneto'])
        # Eficiencia del Ciclo
        self.root.ids.n.text= str(ciclo_rankine.results['n'])

        #Entalpia bard long
        #self.root.ids.h1.value = str(ciclo_rankine.hs['h1'])
        #self.root.ids.ws_turb.text = str(ciclo_rankine.results['ws_turb'])
MainApp().run()