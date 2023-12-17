from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.animation import Animation
from coordinates_control import CoordinatesControl
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import NumericProperty
from kivy.properties import AliasProperty

# Builder.load_file('line_drawer.kv')

class LineDrawer(Widget):
    def __init__(self, **kwargs):
        super(LineDrawer, self).__init__(**kwargs)
        # self.bind(size=self.redraw)
        # self.draw_base()

    def update_and_redraw(self, new_h6):
        # Actualizar el valor de length_h6
        self.length_h6 = new_h6
    # Forzar una actualización de las longitudes dependientes
        self.dispatch('on_length_update')
    # Volver a dibujar el widget
        self.redraw()

        # Inicialización de las coordenadas de la línea
    def draw_line(self, x1, y1, x2, y2, line_id, color=(0, 0, 0, 1), width=1):
        with self.canvas:
            Color(*color)
            # Dibuja la línea y almacena una referencia en el diccionario de identificadores
            self.ids[line_id] = Line(points=[x1, y1, x2, y2], width=width)

    def modify_line(self, line_id, new_points):
        # Modifica la línea con el identificador dado
        line = self.ids[line_id]
        line.points = new_points

    def animate_line(self, line_id, new_points, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        anim = Animation(points=new_points, duration=duration)
        anim.start(line)

    #Get coordenate of the line
    def get_line_coordinates(self, line_id):
        line = self.ids[line_id]
        return line.points
    #Get an especific coordenate of the line
    def get_line_coordinate(self, line_id, index):
        line = self.ids[line_id]
        return line.points[index]

    def animate_lines_vertical(self,line_id, hs, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        points=[line.points[0], line.points[1]+hs, line.points[2], line.points[3]+hs]
        anim = Animation(points=[line.points[0], line.points[1]+hs, line.points[2], line.points[3]+hs], duration=duration)
        anim.start(line)


    def animate_lines_horizontal(self,line_id, hs, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        print(f"Linea {line_id}")
        print(line.points)
        new_points = [line.points[0] + hs, line.points[1], line.points[2] + hs, line.points[3]]
        anim = Animation(points=new_points, duration=duration)
        # anim = Animation(points=[line.points[0]+hs, line.points[1], line.points[2]+hs, line.points[3]], duration=duration)
        anim.start(line)
        line.points = new_points
        print(f"Linea {line_id}")
        print(line.points)
    #Negative because it moves to the left
    def animate_lines_grow_negative(self,line_id, point_final, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        anim = Animation(points=[ point_final, line.points[1], line.points[2], line.points[3]], duration=duration)
        anim.start(line)
    #Positive because it moves to the right
    def animate_lines_grow_positive(self,line_id, point_final, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        anim = Animation(points=[line.points[0], line.points[1], point_final, line.points[3]], duration=duration)
        anim.start(line)
    #Draw a line that connects two lines with animation
    def draw_line_connecting_two_lines(self, line_id1, line_id2, line_id3, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line1 = self.ids[line_id1]
        line2 = self.ids[line_id2]
        line3 = self.ids[line_id3]
        anim = Animation(points=[line1.points[2], line1.points[3], line2.points[0], line2.points[1]], duration=duration)
        anim.start(line3)

    def draw_base(self):
        # Dibuja las líneas base
        self.draw_line(1490, 790, 1490, 1100, 'h6a', color=(0.5, 0, 0.5, 1), width=4)
        self.draw_line(1490, 1100, 1800, 1100, 'h6b', color=(0.5, 0, 0.5, 1), width=3)
        self.draw_line(2350, 850, 2350, 1000, 'h7a', color=(0, 0, 1, 1), width=2)
        self.draw_line(1920, 1000, 2350, 1000, 'h7b', color=(0, 0, 1, 1), width=2)
        self.draw_line(2280, 300, 2280, 480, 'h3a', color=(0, 0.5, 0.5, 1), width=2)
        self.draw_line(1830, 300, 2280, 300, 'h3b', color=(0, 0.5, 0.5, 1), width=2)
        #Line 7h3
        self.draw_line(2280, 480, 2350, 850, '3h7', color=(0.5, 0.5, 0.5, 1), width=1)
        self.draw_line(2250, 850, 2250, 930, 'h8a', color=(0, 1, 1, 1), width=2)
        self.draw_line(2000, 930, 2250, 930, 'h8b', color=(0, 1, 1, 1), width=3)
        self.draw_line(1570, 255, 1570, 545, 'h4a', color=(0.5, 0.5, 0.5, 1), width=2)
        self.draw_line(1570, 255, 1770, 255, 'h4b', color=(0.5, 0.5, 0.5, 1), width=2)
        self.draw_line(1630, 300, 1630, 545, 'h9a', color=(0.5, 1, 0.5, 1), width=4)
        self.draw_line(1630, 300, 1830, 300, 'h9b', color=(0.5, 1, 0.5, 1), width=4)
        self.draw_line(1590, 630, 1590, 680, 'h5a', color=(0.5, 0, 0.5, 1), width=4)
        self.draw_line(2150, 385, 2150, 600, 'h2a', color=(0.5, 0, 1, 1), width=2)
        self.draw_line(2030, 385, 2150, 385, 'h2b', color=(0.5, 0, 1, 1), width=2)
        self.draw_line(2200, 635, 2200, 700, 'h1a', color=(0, 0, 1, 1), width=2)
        #Line 1h2
        self.draw_line(2150, 600, 2200, 635, '1h2', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 5h6
        self.draw_line(1590, 680, 1490, 790, '5h6', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 4h5
        self.draw_line(1570, 545, 1590, 630, '4h5', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 9h5
        self.draw_line(1630, 545,1590, 630, '9h5', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 6h8
        self.draw_line(1800, 1100, 2000, 930, '6h8', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 1h8
        self.draw_line(2200, 700, 2250, 850, '1h8', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 2h9
        self.draw_line(1830, 300, 2030, 385, '2h9', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 3h4
        self.draw_line(1770, 255, 1830, 300, '3h4', color=(0.5, 0.5, 0.5, 1), width=1)


    def redraw(self, *args):
        # Elimina todas las líneas
        self.canvas.clear()
        # Redibuja todas las líneas
        self.draw_base()

    def get_lines_ids(self):
        # Devuelve los identificadores de las líneas
        return self.ids

class LineDrawingApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        line_drawer = LineDrawer()
        line_drawer.draw_base()
        return line_drawer

    def on_start(self):
        pass# Establecer la raíz después de realizar las operaciones

if __name__ == '__main__':
    LineDrawingApp().run()
