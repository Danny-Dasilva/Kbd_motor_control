
import keyboard

values = {1 : "a", 2 : "d", 3 : "w", 4: "s"}




def angle_gen(length):
    angle = 360 / length
    return(angle)

while True:
    for key, value in values.items():
        if keyboard.is_pressed(value):
            mult = angle_gen(len(values))
            print(key * mult, "is pressed")
    if keyboard.read_key() == "p":
        print("You pressed p")
        break

