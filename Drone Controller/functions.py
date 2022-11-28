from djitellopy import Tello
tello = Tello()
try:
    tello.connect()
except:
    print("Check Connexion Tello Drone")
# functions
def moveRight():
    tello.move_right(50)

def moveLeft():
    tello.move_left(50)

def moveForward():
    tello.move_forward(50)

def moveBack():
    tello.move_back(50)
