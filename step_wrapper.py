from step.API import GrblComm

import keyboard
class Step:

    def __init__(self):
        #Initialize variables
        self.comm = GrblComm("COM10", 250000,  True)

    def set_angle(self, input_ang):
        if input_ang > 180:
            angle = 4 - (input_ang/360)
        if input_ang < 180:
            angle = 4 + (input_ang/360)
        self.comm.rapidMovement("X" + angle + "F4")





values = {1 : "q", 2 : "w", 3 : "e", 4: "r"}



def angle_gen(length):
    angle = 360 / length
    return(angle)

while True:
    for key, value in values.items():
        if keyboard.is_pressed(value):
            mult = angle_gen(len(values))
            angle = key * mult
            print(angle, "is pressed")
            # Step.set_angle(angle)
    if keyboard.read_key() == "p":
        print("You pressed p")
        break
#comm.closeSer()