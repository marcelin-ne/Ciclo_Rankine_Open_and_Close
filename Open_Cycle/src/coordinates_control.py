class CoordinatesControl:
    def __init__(self, widget):
        self.widget = widget



    def calculate_new_coordinates(self, line_id, hx=0, hy=0):
        current_coordinates = self.get_line_coordinates(line_id)
        new_coordinates = [
            current_coordinates[0] + self.widget.width * hx,
            current_coordinates[1] + self.widget.height * hy,
            current_coordinates[2] + self.widget.width * hx,
            current_coordinates[3] + self.widget.height * hy,
        ]
        return new_coordinates

    def modify_line_with_offset(self, line_id, hx=0, hy=0):
        new_coordinates = self.calculate_new_coordinates(line_id, hx, hy)
        line = self.widget.ids[line_id]
        line.points = new_coordinates

#Example of use
    def generate_points_with_offset(self, current_coordinates, hx=0, hy=0):
        """
        Genera nuevos puntos aplicando un desplazamiento (hx, hy) a las coordenadas actuales.
        :param current_coordinates: Coordenadas actuales en el formato [x1, y1, x2, y2, ...]
        :param hx: Desplazamiento en la dirección X
        :param hy: Desplazamiento en la dirección Y
        :return: Nuevos puntos después de aplicar el desplazamiento
        """
        if len(current_coordinates) % 2 != 0:
            # Asegúrate de que la lista de coordenadas tiene una longitud par
            raise ValueError("La lista de coordenadas debe tener una longitud par")

        new_points = []
        for i in range(0, len(current_coordinates), 2):
            # Para cada par de coordenadas (x, y), aplica el desplazamiento hx a la coordenada x
            new_x = current_coordinates[i] + hx
            new_y = current_coordinates[i + 1] + hy
            new_points.extend([new_x, new_y])

        return new_points
    