
import keyboard

values = {1 : "a", 2 : "d", 3 : "w", 4: "s"}



while True:
    for key, value in values.items():
        if keyboard.is_pressed(value):
            print(value, "is pressed")
    
    if keyboard.read_key() == "p":
        print("You pressed p")
        break

