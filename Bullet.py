"""
class Bullet:
#@author: Your name here. 

Parameters:
damage : int #exactly what you think it is
speed : int #how fast the bullet moves.
vX, vY : float #velocity in x and y.
target : Enemy #for homing bullets
image : ?? #image. how does one use pygame? 
type : string #homing, splash etc. 

Methods:
__init__(self, damage, speed, image, type)

setDest (self, x : int, y : int) -> None:
    "Adjusts target to those coordinates"

setTarget (self, target : Enemy) -> None:
    "Picks the target"

update (self) -> None:
    "Moves bullet."
