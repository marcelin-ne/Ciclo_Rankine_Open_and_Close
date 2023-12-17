from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Line

KV_STRING = """
<MyLayout>:
    orientation: 'vertical'

    MDCard:
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": 0.5}
        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: "Contenido de la tarjeta"
            Widget:
                id: canvas_widget  # Widget para el lienzo

    MDRaisedButton:
        text: "Dibujar Línea"
        on_press: app.draw_line()
"""

class MyLayout(BoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_file('test.kv')

    def draw_line(self):
        canvas_widget = self.root.ids.canvas_widget
        # Modifica los puntos de la línea en el lienzo
        canvas_widget.canvas.children[0].points = [50, 50, 250, 150]

if __name__ == '__main__':
    MyApp().run()
