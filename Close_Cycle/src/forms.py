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
from kivy.animation import Animation
from kivymd.uix.responsivelayout import MDResponsiveLayout
#Import packages for the logic
from calculator import Rankine_P_Close
from delimeter import Delimiter
from line_drawer import LineDrawer
#Builder.load_file('../design/forms.kv')
#

# class LineDrawer(BoxLayout):
#     def __init__(self, **kwargs):
#         super(LineDrawer, self).__init__(**kwargs)

# class MyBoxLayout(BoxLayout):
#     def __init__(self, **kwargs):
#         super(MyBoxLayout, self).__init__(**kwargs)
#         self.line_drawer = self.ids.line_drawer

#         # Aplica la animación cuando se crea la instancia del BoxLayout
#         self.line_drawer.animate_line()
        
class MainApp(MDApp):
    def build(self):
        # Window.size = (1150, 600)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.accent_palette = "Red"
        #---------------------------#
        self.layout = BoxLayout(orientation='vertical')
        # Cargar el archivo KV después de que los widgets estén construidos
        Builder.load_file('../design/forms.kv')
        self.hs= {}
        
        #Definig the windows dimentions
        # Establecer dimensiones mínimas y máximas para la ventana
        Window.minimum_width, Window.minimum_height = 1200, 300
        Window.maximum_width, Window.maximum_height = 1300, 400

        return Builder.load_file('../design/forms.kv')


    def validate_textfield(self, text_field, min_limit, max_limit):
        input_text = text_field.text.strip()
        try:
            input_value = float(input_text)  # Intentar convertir el texto a un entero
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
        if self.validate_textfield(self.root.ids.p1, 3, 30) and self.validate_textfield(self.root.ids.p2, 2000, 36000) and self.validate_textfield(self.root.ids.p3, 1000, 22000) and self.validate_textfield(self.root.ids.t6, 200, 800)  and self.validate_textfield(self.root.ids.nb, 0.2, 1) and self.validate_textfield(self.root.ids.nt, 0.2, 1):
            return True
        else:
            return False

    #Function to redraw the lines based on hs
    def redraw_based_on_hs(self, hs):
        line_drawer = self.root.ids.line_drawer
        #h1a
        line_drawer.animate_lines_horizontal('h1a', hs['h1'])
        #h2
        line_drawer.animate_lines_grow_and_shift_positive_negative('h2a', 'h2b', hs['h2'], 1)
        #h3
        line_drawer.animate_lines_grow_and_shift_positive_negative('h3a', 'h3b', hs['h3'], 1)
        #h4
        line_drawer.animate_lines_grow_and_shift_negative('h4a', 'h4b', -hs['h4'], 1)
        #h5
        line_drawer.animate_lines_horizontal('h5a', -hs['h5'])
        #h6
        line_drawer.animate_lines_grow_and_shift_negative_positive('h6a', 'h6b', hs['h6'], 1)
        #h7
        line_drawer.animate_lines_grow_and_shift_positive('h7a', 'h7b', hs['h7'], 1)
        #h8
        line_drawer.animate_lines_grow_and_shift_positive('h8a', 'h8b', hs['h8'], 1)
        #h9
        line_drawer.animate_lines_grow_and_shift_negative('h9a', 'h9b', -hs['h9'], 1)
        #3h7
        line_drawer.draw_line_connecting_two_lines('h3a', 'h7a', '7h3')
        # #1h2
        line_drawer.draw_line_connecting_two_lines('h2a', 'h1a', '1h2')
        # #5h6
        line_drawer.draw_line_connecting_two_lines('h5a', 'h6a', '5h6')
        # #4h5
        line_drawer.draw_line_connecting_two_lines('h4a', 'h5a', '4h5')
        # #9h5
        line_drawer.draw_line_connecting_two_lines('h9a', 'h5a', '9h5')
        # #1h8
        line_drawer.draw_line_connecting_two_lines('h1a', 'h8a', '1h8')
        # #Connect h9a and h9b
        # line_drawer.animate_and_connect_lines_vertical('h9a', 'h9b')

    def resolve(self):
        #Restart the lines
        # self.line_drawer.redraw()
        # Si todas las validaciones son correctas, calcular y dibujar
        if self.validate_all_textfields():

        # Crear el objeto
            cr_close = Rankine_P_Close({}, {})
            delimeter = Delimiter()

        # Calcular el ciclo Rankine
            cr_close.calc_ciclo_rankine_in_precal_close_water(
            float(self.root.ids.p1.text),
            float(self.root.ids.p2.text),
            float(self.root.ids.p3.text),
            float(self.root.ids.t6.text),
            float(self.root.ids.nb.text),
            float(self.root.ids.nt.text)
            )

        # Imprimir resultados
            print(cr_close.hs)
            print(cr_close.results)

        # Actualizar etiquetas en el archivo kv
            self.root.ids.eficiencia_termica_result.text = f"{cr_close.results['eta']} "
            self.root.ids.trabajo_neto.text = f"{cr_close.results['wturb']}"
        
        # Actualizar el valor de hs
            self.root.ids.h1_valor.text = f"{cr_close.hs['h1']} "
            self.root.ids.h2_valor.text = f"{cr_close.hs['h2']} "
            self.root.ids.h3_valor.text = f"{cr_close.hs['h3']} "
            self.root.ids.h4_valor.text = f"{cr_close.hs['h4']} "
            self.root.ids.h5_valor.text = f"{cr_close.hs['h5']} "
            self.root.ids.h6_valor.text = f"{cr_close.hs['h6']} "
            self.root.ids.h7_valor.text = f"{cr_close.hs['h7']} "
            self.root.ids.h8_valor.text = f"{cr_close.hs['h8']} "
            self.root.ids.h9_valor.text = f"{cr_close.hs['h9']} "

        # Transformar hs utilizando el objeto Delimiter
            hs = delimeter.transform_to_distance(cr_close.hs)
            print("Hs desde delimeter")
            print(hs)
        #Redraw the lines of line_drawe based on hs 
            # self.line_drawer.draw_base()
            self.redraw_based_on_hs(hs)

    def get_hs(self):
        return self.hs
    def set_hs(self, hs):
        self.hs = hs

MainApp().run()