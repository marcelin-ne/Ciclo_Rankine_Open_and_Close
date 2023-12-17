from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from calculator import Rankine_P_Close
from delimeter import Delimiter
from line_drawer import LineDrawer
from kivy.graphics import Color, InstructionGroup, Line
Builder.load_file('myform.kv')

class MyForm(BoxLayout):
    line_drawer = LineDrawer()
    def __init__(self,**kwargs):
        super(MyForm, self).__init__(**kwargs)
        self.hs= {}
        self.line_drawer = LineDrawer()
        self.add_widget(self.line_drawer)
        # Crear un InstructionGroup para contener las instrucciones de dibujo
        self.cuadrado_instruction = InstructionGroup()

            # Coordenadas del cuadrado (ejemplo: 100x100 con un tamaño de 200x200)
        x, y, size = 1300, 200, 1100

            # Agregar líneas para formar un cuadrado
        self.cuadrado_instruction.add(Line(points=[x, y, x + size, y, x + size, y + size, x, y + size, x, y]))

        self.canvas.add(self.cuadrado_instruction)
    
    def resolve(self):
        #Restart the lines
        self.line_drawer.redraw()
        #Create the object
        cr_close=Rankine_P_Close({},{})
        delimeter=Delimiter()
        #cr_open.calc_ciclo_rankine_in_precal_open_water(float(self.ids.pbbp.text), self.ids.pbap.text, self.ids.psal_cald.text, self.ids.tsal_cald.text, self.ids.ns_turb.text, self.ids.ns_bomba.text)
        cr_close.calc_ciclo_rankine_in_precal_close_water(float(self.ids.p1.text), 0, float(self.ids.p2.text), float(self.ids.p3.text), 0, float(self.ids.T6.text), float(self.ids.mp.text), float(self.ids.nb.text), float(self.ids.nt.text))
        print(cr_close.hs)
        print(cr_close.results)
        self.ids.eficiencia_termica.text = str(cr_close.results['eta']) + " %"
        self.ids.trabajo_neto.text = str(cr_close.results['wturb']) + " kJ/kg"
        hs=delimeter.transform_to_distance(cr_close.hs)
        print("Hs desde delimeter")
        print(hs)
        #Until here i past
        ids=self.line_drawer.get_lines_ids()
        self.redraw_based_on_hs( hs)

    def redraw_based_on_hs(self, hs):
        #h1a
        # self.line_drawer.animate_lines_horizontal('h1', hs['h1'])
        #h2
        self.line_drawer.animate_lines_horizontal('h2a', hs['h2'])
        #h2b
        new_point=self.line_drawer.get_line_coordinate('h2a', 0)
        self.line_drawer.animate_lines_grow_positive('h2b', new_point, 1)
        #h3
        self.line_drawer.animate_lines_horizontal('h3a', hs['h3'])
        #h3b
        new_point=self.line_drawer.get_line_coordinate('h3a', 0)
        self.line_drawer.animate_lines_grow_positive('h3b', new_point, 1)
        #h4
        self.line_drawer.animate_lines_horizontal('h4a', hs['h4'])
        #h4b
        new_point=self.line_drawer.get_line_coordinate('h4a', 0)
        self.line_drawer.animate_lines_grow_negative('h4b', new_point, 1)
        #h5
        self.line_drawer.animate_lines_horizontal('h5a', hs['h5'])
        #h6
        self.line_drawer.animate_lines_horizontal('h6a', hs['h6'])
        #h6b
        new_point=self.line_drawer.get_line_coordinate('h6a', 0)
        self.line_drawer.animate_lines_grow_negative('h6b', new_point, 1)
        # self.line_drawer.animate_lines_horizontal('h6b', hs['h6'])
        #h7
        self.line_drawer.animate_lines_horizontal('h7a', hs['h7'])
        #h7b
        new_point=self.line_drawer.get_line_coordinate('h7a', 0)
        self.line_drawer.animate_lines_grow_positive('h7b', new_point, 1)
        #h8
        self.line_drawer.animate_lines_horizontal('h8a', hs['h8'])
        #h8b
        new_point=self.line_drawer.get_line_coordinate('h8a', 0)
        self.line_drawer.animate_lines_grow_positive('h8b', new_point, 1)
        #h9
        self.line_drawer.animate_lines_horizontal('h9a', hs['h9'])
        #h9b
        new_point=self.line_drawer.get_line_coordinate('h9a', 0)
        self.line_drawer.animate_lines_grow_negative('h9b', new_point, 1)
        #3h7
        self.line_drawer.draw_line_connecting_two_lines('h3a', 'h7a', '3h7')
        #1h2
        self.line_drawer.draw_line_connecting_two_lines('h2a', 'h1a', '1h2')
        #5h6
        self.line_drawer.draw_line_connecting_two_lines('h5a', 'h6a', '5h6')
        #4h5
        self.line_drawer.draw_line_connecting_two_lines('h4a', 'h5a', '4h5')
        #9h5
        self.line_drawer.draw_line_connecting_two_lines('h9a', 'h5a', '9h5')
        #1h8
        self.line_drawer.draw_line_connecting_two_lines('h1a', 'h8a', '1h8')



    def get_hs(self):
        return self.hs
    def set_hs(self, hs):
        self.hs = hs

class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1300, 700)
        myform_instance = MyForm()
        return MyForm()

if __name__ == '__main__':
    MyApp().run()
