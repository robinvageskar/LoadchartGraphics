import cairo
import math

class Geometry():
  def __init__(self) -> None:
    pass
  
  def draw(self, context:cairo.Context):
    print()
    pass
    

class TelescopeGeometry(Geometry):

  def __init__(self, boom:float, telescope:float, minAngle:float, maxAngle:float) -> None:
    """
    boom: Length of boom in m
    telescope: Length of telescope in m
    minAngle: Minimum anlge of boom relative to horisontal plane in degrees
    maxAngle: Maximum anlge of boom relative to horisontal plane in degrees
    """

    super().__init__()
    self.boom = boom
    self.telescope = telescope
    self.minAngle = math.radians(minAngle)
    self.maxAngle = math.radians(maxAngle)

class KnuckleBoomGeometry(Geometry):
    
  def __init__(self, boom:float, knuckle:float, boomAngleMin:float, boomAngleMax:float, knuckleAngleMin:float, knuckleAngleMax:float) -> None:
    """
    boom: Length of boom in m
    knuckle: Length of knuckle in m
    boomAngleMin: Minimum anlge of boom relative to horisontal plane in degrees
    boomAngleMax: Maximum anlge of boom relative to horisontal plane in degrees
    knuckleAngleMin: Minimum anlge of knuckle relative to boom plane in degrees
    knuckleAngleMax: Maximum anlge of knuckle relative to boom plane in degrees
    """

    super().__init__()
    self.boom = boom
    self.knuckle = knuckle
    self.boomAngleMin = math.radians(boomAngleMin)
    self.boomAngleMax = math.radians(boomAngleMax)
    self.knuckleAngleMin = math.radians(knuckleAngleMin)
    self.knuckleAngleMax = math.radians(knuckleAngleMax)


class Loadchart():
  
  def __init__(self, name:str, geometry:Geometry) -> None:
    self.name = name
    self.geometry = geometry
      

    