import math


class Formula:
    def areaOfCylinder(self, radius = 0, height = 0):
        '''

        :param radius: must be an integer or float
        :param height: must be an integer or float
        :return: area of a cylinder
        '''
        try:
            if radius <= 0:
                return  f"Radius: {radius} is less than or equal to 0"
            elif height <= 0:
                return  f"Height: {height} is less than or equal to 0"

            area_cylinder = 2 * math.pi * radius * height + 2 * math.pi * radius**2
            return area_cylinder
        except Exception as c:
            return f"Error: {c}"

formula = Formula()
print(formula.areaOfCylinder(5, 7))
