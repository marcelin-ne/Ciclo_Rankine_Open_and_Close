from line_drawer import LineDrawer

class Delimiter:
    #This class is a delimiter for the drawing of the lines

    def __init__(self, **kwargs):
        super(Delimiter, self).__init__(**kwargs)
        self.distance = {}
        self.hs= {}

    def get_hs_from_form(self):
        self.hs = self.form.get_hs()
        return self.hs

    def transform_to_distance(self,hs):
        # Nuevo diccionario para almacenar los valores transformados
        for key, value in hs.items():
            sing = self.determinate_sing(hs, key)
        # Convierte el valor a un entero dividiéndolo por 10
            transformed_value = int(float(value) / 10) * sing
        # Agrega el par clave-valor al diccionario distance
            self.distance[key] = transformed_value
        # Devuelve el diccionario distance
        return self.distance

    def determinate_sing(self, hs,key):
        # Determina el signo del valor basado en la clave
        if key in ['h6', 'h5', 'h4', 'h9','h3']:
            # Invierte el signo para 'h6', 'h5', 'h4' y 'h9'
            return -1 if float(hs['h6']) < 51 else 1
        else:
            # Usa el signo normal para otras claves
            return 1

    #Return every element of the dictionary distance individually
    def get_distance(self, key):
        return self.distance[key]


    #Get the limit distance that the lines can be draw 
    def get_limit_distance(self):
        return self.limit_distance
