# POLYMORPHISM

class Polygon:
    def rendering(self):
        print("Polygon is rendering")


class Circle(Polygon):
    def rendering(self):
        print("Rendering circle...")
        #return super().rendering()


class Triangle(Polygon):
    def rendering(self):
        print("Rendering Triangle...")
        # return super().rendering()
