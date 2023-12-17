#Import libraries for the design
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import platform
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivymd.app import MDApp
#Import packages for the logic
from calculator import Rankine_P_Close
from delimeter import Delimiter
from line_drawer import LineDrawer


class MainApp(MDApp):
    line_drawer = LineDrawer()
    def build(self):
        Window.size = (1150, 600)
        #Line Drawer
        #Theme
        self.theme_cls.theme_style = "Light"
        #Colors
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('../design/forms.kv')


    def validate_textfield(self, text_field, min_limit, max_limit):
        input_text = text_field.text.strip()
        try:
            input_value = int(input_text)  # Intentar convertir el texto a un entero
            if min_limit <= input_value <= max_limit:
                text_field.helper_text = ""
                text_field.error = False
                text_field.text_color = 1, 1, 1, 1  # Color de texto normal
                return True
            else:
                text_field.helper_text = f"Valor fuera de rango ({min_limit}-{max_limit})"
                text_field.error = True
                text_field.text_color = 1, 0, 0, 1  # Rojo
                return False
        except ValueError:
            text_field.helper_text = "Ingrese un número válido"
            text_field.error = True
            text_field.text_color = 1, 0, 0, 1  # Rojo

    #Function to validate every textfield that returns true if all the textfields are correct
    def validate_all_textfields(self):
        #Validate the textfields
        if self.validate_textfield(self.root.ids.p1, 3, 30000) and self.validate_textfield(self.root.ids.p2, 2000, 36000) and self.validate_textfield(self.root.ids.p3, 1000, 22000) and self.validate_textfield(self.root.ids.t6, 200, 800)  and self.validate_textfield(self.root.ids.nb, 0.2, 1) and self.validate_textfield(self.root.ids.nt, 0.2, 1):
            return True
        else:
            return False

    def resolve(self):
        # Si todas las validaciones son correctas, calcular y dibujar
        if self.validate_all_textfields():
        # Reiniciar las líneas
            self.line_drawer.redraw()

        # Crear el objeto
            cr_close = Rankine_P_Close({}, {})
            delimeter = Delimiter()

        # Calcular el ciclo Rankine
            cr_close.calc_ciclo_rankine_in_precal_close_water(
            float(self.root.ids.p1.text),
            0,
            float(self.root.ids.p2.text),
            float(self.root.ids.p3.text),
            0,
            float(self.root.ids.t6.text),
            float(self.root.ids.nb.text),
            float(self.root.ids.nt.text)
            )

        # Imprimir resultados
            print(cr_close.hs)
            print(cr_close.results)

        # Actualizar etiquetas en el archivo kv
            self.root.ids.eficiencia_termica.text = f"{cr_close.results['eta']} %"
            self.root.ids.trabajo_neto.text = f"{cr_close.results['wturb']} kJ/kg"

        # Transformar hs utilizando el objeto Delimiter
            hs = delimeter.transform_to_distance(cr_close.hs)
            print("Hs desde delimeter")
            print(hs)

MainApp().run()