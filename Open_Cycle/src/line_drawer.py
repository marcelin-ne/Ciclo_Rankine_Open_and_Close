from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color ,Ellipse
from kivy.animation import Animation
from coordinates_control import CoordinatesControl
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.properties import NumericProperty
from kivy.properties import AliasProperty
from kivy.clock import Clock
# Builder.load_file('line_drawer.kv')

class LineDrawer(Widget):
    def __init__(self, **kwargs):
        super(LineDrawer, self).__init__(**kwargs)
        #self.bind(size=self.redraw)
        self.draw_base()

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

    def draw_circle(self, center_x, center_y, radius, circle_id, color=(0, 0, 0, 1), width=2):
        with self.canvas:
            Color(*color)
            self.ids[circle_id] = Line(circle=(center_x, center_y, radius), width=width)

    def draw_arc(self, center_x, center_y, radius, start_angle, end_angle, arc_id, color=(1, 1, 1, 1), width=2):
        with self.canvas:
            Color(*color)
            # Dibuja una parte de un círculo utilizando Line y la propiedad ellipse
            self.ids[arc_id] = Line(ellipse=(center_x - radius, center_y - radius, radius * 2, radius * 2,
                                            start_angle, end_angle), width=width)

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


    
    #Draw a line that connects two lines with animation
    def draw_line_connecting_two_lines(self, line_id1, line_id2, line_id3, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line1 = self.ids[line_id1]
        line2 = self.ids[line_id2]
        line3 = self.ids[line_id3]
        anim = Animation(points=[line1.points[2], line1.points[3], line2.points[0], line2.points[1]], duration=duration)
        anim.start(line3)
    


    def draw_base(self):
        # Dibujar arcos en distintas ubicaciones y tamaños
        self.draw_arc(900, 400, 180, 300, 233, arc_id='h4')
        self.draw_arc(900, 400, 180, 225, 190, arc_id='h3')
        self.draw_arc(900, 400, 180, 170, 130, arc_id='h2')
        self.draw_arc(900, 400, 180, 120, 97, arc_id='h1')
        self.draw_arc(900, 400, 180, 97, 50, arc_id='h7')
        self.draw_arc(900, 400, 200, 190, 50, arc_id='h6')
        # self.draw_arc(900, 400, 180, 50, 300, arc_id='h5') 
        # self.grow_arc_radius('h3', 50, duration=0.5)
        

    def grow_arc_radius(self, arc_id, delta_radius, duration=1):
        # Función para animar el cambio de radio del arco
        current_ellipse = self.ids[arc_id].ellipse
        center_x, center_y, radius = current_ellipse[0] + current_ellipse[2] / 2, current_ellipse[1] + current_ellipse[3] / 2, current_ellipse[2] / 2
        new_radius = radius + delta_radius
        # Animación suave del cambio de radio
        anim = Animation(ellipse=(center_x - new_radius, center_y - new_radius, new_radius * 2, new_radius * 2,
                                  current_ellipse[4], current_ellipse[5]), duration=duration)
        anim.start(self.ids[arc_id])
        
    
    

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
