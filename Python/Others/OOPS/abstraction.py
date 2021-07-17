from abc import ABC, abstractmethod


class Polygon:
    @abstractmethod
    def noofSide(self):
        pass
    
class Triangle:
    # overriding the abstract method
    def noofSide(self):
        return "3 Sides"

class Square:
    # overriding the abstract method
    def noofSide(self):
        return "4 Sides"


tri = Triangle()
sq = Square()   

print(tri.noofSide())
print(sq.noofSide())