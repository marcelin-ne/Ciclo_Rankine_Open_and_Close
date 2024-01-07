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
        new_points = [int(line.points[0]), int(line.points[1] + hs), int(line.points[2]), int(line.points[3] + hs)]
        anim = Animation(points=[line.points[0], line.points[1]+hs, line.points[2], line.points[3]+hs], duration=duration)
        anim.start(line)
        line=self.modify_line(line_id, new_points)

    def animate_lines_grow_and_shift_negative(self, line_id_a,line_id_b, hs, duration=1):
        linea = self.ids[line_id_a]
        lineb = self.ids[line_id_b]
        animA=Animation(points=[linea.points[0] + hs, lineb.points[1]+hs, linea.points[2] + hs, linea.points[3]], duration=duration)
        new_points_a = [int(linea.points[0] + hs), int(lineb.points[1]+hs), int(linea.points[2] + hs), int(linea.points[3])]
        animA.start(linea)
        animB=Animation(points=[lineb.points[0] + hs, lineb.points[1]+hs, lineb.points[2] , lineb.points[3]+hs], duration=duration)
        new_points_b = [int(lineb.points[0] + hs), int(lineb.points[1]+hs), int(lineb.points[2]), int(lineb.points[3]+hs)]
        animB.start(lineb)
        linea=self.modify_line(line_id_a, new_points_a)
        lineb=self.modify_line(line_id_b, new_points_b)

    def animate_lines_grow_and_shift_positive(self, line_id_a,line_id_b, hs, duration=1):
        linea = self.ids[line_id_a]
        lineb = self.ids[line_id_b]
        animA=Animation(points=[linea.points[0]+hs, linea.points[1], linea.points[2]+hs, lineb.points[3]+hs], duration=duration)
        new_points_a = [int(linea.points[0]+hs), int(linea.points[1]), int(linea.points[2]+hs), int(lineb.points[3]+hs)]
        animA.start(linea)
        animB=Animation(points=[lineb.points[0], lineb.points[1]+hs, linea.points[2] + hs, lineb.points[3]+hs], duration=duration)
        new_points_b = [int(lineb.points[0]), int(lineb.points[1]+hs), int(linea.points[2] + hs), int(lineb.points[3]+hs)]
        animB.start(lineb)
        lineb=self.modify_line(line_id_b, new_points_b)
        linea=self.modify_line(line_id_a, new_points_a)
        
    def animate_lines_grow_and_shift_negative_positive(self, line_id_a,line_id_b, hs, duration=1):
        linea = self.ids[line_id_a]
        lineb = self.ids[line_id_b]
        animA=Animation(points=[linea.points[0] - hs, linea.points[1], linea.points[2] - hs, lineb.points[3]+hs], duration=duration)
        new_points_a = [int(linea.points[0] - hs), int(linea.points[1]), int(linea.points[2] - hs), int(lineb.points[3]+hs)]
        animA.start(linea)
        animB=Animation(points=[linea.points[0]-hs, lineb.points[1]+hs, lineb.points[2] , lineb.points[3]+hs], duration=duration)
        new_points_a = [int(linea.points[0]-hs), int(lineb.points[1]+hs), int(lineb.points[2]), int(lineb.points[3]+hs)]
        animB.start(lineb)
        linea=self.modify_line(line_id_a, new_points_a)
        lineb=self.modify_line(line_id_b, new_points_a)
    
    def animate_lines_grow_and_shift_positive_negative(self, line_id_a,line_id_b, hs, duration=1):
        linea = self.ids[line_id_a]
        lineb = self.ids[line_id_b]
        animA=Animation(points=[linea.points[0]+hs, linea.points[1], linea.points[2]+hs, lineb.points[3]-hs], duration=duration)
        new_points_a = [int(linea.points[0]+hs), int(linea.points[1]), int(linea.points[2]+hs), int(lineb.points[3]-hs)]
        animA.start(linea)
        animB=Animation(points=[lineb.points[0], lineb.points[1]-hs, linea.points[2] + hs, lineb.points[3]-hs], duration=duration)
        new_points_b = [int(lineb.points[0]), int(lineb.points[1]-hs), int(linea.points[2] + hs), int(lineb.points[3]-hs)]
        animB.start(lineb)
        linea=self.modify_line(line_id_a, new_points_a)
        lineb=self.modify_line(line_id_b, new_points_b)


    def animate_lines_horizontal(self,line_id, hs, duration=1):
        # Agrega una animación a la línea con el identificador dado
        line = self.ids[line_id]
        print(f"Linea {line_id}")
        print(line.points)
        #new_points = [line.points[0] + hs, line.points[1], line.points[2] + hs, line.points[3]]
        new_points = [int(line.points[0] + hs), line.points[1], int(line.points[2] + hs), line.points[3]]
        #Print line id + hs 
        print(f"Linea {line_id} + {hs}")
        # line=self.modify_line(line_id, new_points)
        #anim = Animation(points=new_points, duration=duration)
        anim = Animation(points=[line.points[0]+hs, line.points[1], line.points[2]+hs, line.points[3]], duration=duration)
        anim.start(line)
        line=self.modify_line(line_id, new_points)
        # line.points = new_points
        print(f"Linea New  {line_id}")
        print(f"Nuevas coordenadas: {new_points}")
        
    
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
        self.draw_line(750, 500, 750, 590, 'h6a', color=(0, 0, 0, 1), width=3)
        self.draw_line(750, 590, 850, 590, 'h6b', color=(0, 0, 0, 1), width=3)
        
        self.draw_line(1080, 350, 1080, 575, 'h7a', color=(0.5, 0, 0.5, 1), width=2)
        self.draw_line(887, 575, 1080, 575, 'h7b', color=(0.5, 0, 0.5, 1), width=2)
        #Change the color to purple
        self.draw_line(1050, 265, 1050, 340, 'h3a', color=(1, 0, 0, 1), width=2)
        self.draw_line(940, 265, 1050, 265, 'h3b', color=(1, 0, 0, 1), width=2)
        #Line 7h3 union
        self.draw_line(1050, 340, 1080, 350, '7h3', color=(0.5, 0.5, 0.5, 1), width=1)
        self.draw_line(1065, 500, 1065, 550, 'h8a', color=(0, 0, 1, 1), width=2)
        self.draw_line(940, 550, 1065, 550, 'h8b', color=(0, 0, 1, 1), width=2)
        self.draw_line(735, 255, 735, 355, 'h4a', color=(1, 0, 0, 1), width=2)
        self.draw_line(735, 255, 880, 255, 'h4b', color=(1, 0, 0, 1), width=2)
        self.draw_line(760, 270, 760, 355, 'h9a',color=(0, 0, 1, 1), width=2)
        self.draw_line(760, 270, 875, 270, 'h9b', color=(0, 0, 1, 1), width=2)
        self.draw_line(775, 420, 775, 480, 'h5a', color=(0, 0, 0, 1), width=3)
        self.draw_line(1035, 285, 1035, 400, 'h2a', color=(0, 0, 1, 1), width=2)
        self.draw_line(1010, 285, 1035, 285, 'h2b', color=(0, 0, 1, 1), width=2)
        self.draw_line(1050, 430, 1050, 470, 'h1a', color=(0, 0, 0, 1), width=2)
        #Line 1h2 union
        self.draw_line(1035, 400, 1050, 430, '1h2', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 5h6 union 
        self.draw_line(775, 480, 750, 500, '5h6', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 4h5 union 
        self.draw_line(735, 355, 775, 420, '4h5', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 9h5
        self.draw_line(760, 355, 775, 420, '9h5', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 6h8 union 
        self.draw_line(850, 590, 940, 550, '6h8', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 1h8
        self.draw_line(1050, 470, 1065, 500, '1h8', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 2h9 union
        self.draw_line(875, 270, 1010, 285, '2h9', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 3h4 union 
        self.draw_line(880, 255, 940, 265, '3h4', color=(0.5, 0.5, 0.5, 1), width=1)
    
    def draw_max_base(self):
        self.draw_line(480, 500, 480, 750, 'h6a', color=(0, 0, 0, 1), width=3)
        self.draw_line(480, 750, 750, 750, 'h6b', color=(0, 0, 0, 1), width=3)
        
        self.draw_line(1280, 350, 1280, 685, 'h7a', color=(0.5, 0, 0.5, 1), width=2)
        self.draw_line(887, 685, 1280, 685, 'h7b', color=(0.5, 0, 0.5, 1), width=2)
        #Change the color to purple
        self.draw_line(1170, 65, 1170, 320, 'h3a', color=(1, 0, 0, 1), width=2)
        self.draw_line(940, 65, 1170, 65, 'h3b', color=(1, 0, 0, 1), width=2)
        self.draw_line(1200, 500, 1200, 650, 'h8a', color=(0, 0, 1, 1), width=2)
        self.draw_line(940, 650, 1200, 650, 'h8b', color=(0, 0, 1, 1), width=2)
        self.draw_line(450, 55, 450, 355, 'h4a', color=(1, 0, 0, 1), width=2)
        self.draw_line(450, 55, 780, 55, 'h4b', color=(1, 0, 0, 1), width=2)
        self.draw_line(510, 90, 510, 355, 'h9a',color=(0, 0, 1, 1), width=2)
        self.draw_line(510, 90, 875, 90, 'h9b', color=(0, 0, 1, 1), width=2)
        self.draw_line(530, 420, 530, 480, 'h5a', color=(0, 0, 0, 1), width=3)
        self.draw_line(1115, 115, 1115, 400, 'h2a', color=(0, 0, 1, 1), width=2)
        self.draw_line(1010, 115, 1115, 115, 'h2b', color=(0, 0, 1, 1), width=2)
        self.draw_line(1150, 430, 1150, 470, 'h1a', color=(0, 0, 0, 1), width=2)
        #Line 1h2 new union
        self.draw_line(1115, 400, 1150, 430, '1h2', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 5h6 new union
        self.draw_line(530, 480, 480, 500, '5h6', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 4h5 new union
        self.draw_line(450, 355, 530, 420, '4h5', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 9h5 new union
        self.draw_line(510, 355, 530, 420, '9h5', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 6h8 new union
        self.draw_line(750, 750, 940, 650, '6h8', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 1h8 new union
        self.draw_line(1150, 470, 1200, 500, '1h8', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 2h9 new union
        self.draw_line(875, 90, 1010, 115, '2h9', color=(0.5, 0.5, 0.5, 1), width=1)
        #line 3h4 new union
        self.draw_line(780, 55, 940, 65, '3h4', color=(0.5, 0.5, 0.5, 1), width=1)
        #Line 7h3 new union
        self.draw_line(1170, 320, 1280, 350, '7h3', color=(0.5, 0.5, 0.5, 1), width=1)



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
