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
        Window.size = (1150, 600)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.accent_palette = "Red"
        #---------------------------#
        self.layout = BoxLayout(orientation='vertical')
        # Cargar el archivo KV después de que los widgets estén construidos
        Builder.load_file('../design/forms.kv')
        self.hs= {}
        # self.line_drawer = LineDrawer()
        # self.layout.add_widget(self.button)
        # self.layout.add_widget(self.line_drawer)
        #return self.layout
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
        # self.line_drawer.animate_lines_horizontal('h1', hs['h1'])
        #h2
        line_drawer.animate_lines_horizontal('h2a', hs['h2'])
        #h2b
        new_point=line_drawer.get_line_coordinate('h2a', 0)
        line_drawer.animate_lines_grow_positive('h2b', new_point, 1)
        #h3
        line_drawer.animate_lines_horizontal('h3a', hs['h3'])
        #h3b
        new_point=line_drawer.get_line_coordinate('h3a', 0)
        line_drawer.animate_lines_grow_positive('h3b', new_point, 1)
        #h4
        line_drawer.animate_lines_horizontal('h4a', hs['h4'])
        #h4b
        new_point=line_drawer.get_line_coordinate('h4a', 0)
        line_drawer.animate_lines_grow_negative('h4b', new_point, 1)
        #h5
        line_drawer.animate_lines_horizontal('h5a', hs['h5'])
        #h6
        line_drawer.animate_lines_horizontal('h6a', hs['h6'])
        #h6b
        new_point=line_drawer.get_line_coordinate('h6a', 0)
        line_drawer.animate_lines_grow_negative('h6b', new_point, 1)
        # self.line_drawer.animate_lines_horizontal('h6b', hs['h6'])
        #h7
        line_drawer.animate_lines_horizontal('h7a', hs['h7'])
        #h7b
        new_point=line_drawer.get_line_coordinate('h7a', 0)
        line_drawer.animate_lines_grow_positive('h7b', new_point, 1)
        #h8
        line_drawer.animate_lines_horizontal('h8a', hs['h8'])
        #h8b
        new_point=line_drawer.get_line_coordinate('h8a', 0)
        line_drawer.animate_lines_grow_positive('h8b', new_point, 1)
        #h9
        line_drawer.animate_lines_horizontal('h9a', hs['h9'])
        #h9b
        new_point=line_drawer.get_line_coordinate('h9a', 0)
        line_drawer.animate_lines_grow_negative('h9b', new_point, 1)
        # #3h7
        # self.line_drawer.draw_line_connecting_two_lines('h3a', 'h7a', '3h7')
        # #1h2
        # self.line_drawer.draw_line_connecting_two_lines('h2a', 'h1a', '1h2')
        # #5h6
        # self.line_drawer.draw_line_connecting_two_lines('h5a', 'h6a', '5h6')
        # #4h5
        # self.line_drawer.draw_line_connecting_two_lines('h4a', 'h5a', '4h5')
        # #9h5
        # self.line_drawer.draw_line_connecting_two_lines('h9a', 'h5a', '9h5')
        # #1h8
        # self.line_drawer.draw_line_connecting_two_lines('h1a', 'h8a', '1h8')

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
            self.root.ids.eficiencia_termica.text = f"{cr_close.results['eta']} %"
            self.root.ids.trabajo_neto.text = f"{cr_close.results['wturb']} kJ/kg"

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