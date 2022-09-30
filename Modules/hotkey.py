
# xiloume

from pynput import keyboard

from helpers import CONFIG


class hotkey:

    def __init__(self):
        self.keyboard_controller = keyboard.Controller()
        self.keys_pressed = set()
        print("keyboard active")

    def _on_press(self, key):
        print('{0} press'.format(key))
        # verifie la touche F1 lance l'activation des bateau
        if key == keyboard.Key.f1:
            self.switchparam("SHIPS_ENABLED")
        elif key == keyboard.Key.f2:
            self.switchparam("CREWS_ENABLED")
        # verifie la touche F1 lance l'activation des Item
        elif key == keyboard.Key.f3:
            self.switchparam("CHEST_ENABLED")
        elif key == keyboard.Key.f4:
            self.switchparam("PLAYER_ENABLED")
        # verifie la touche F5 lance l'activation des worldevent
        elif key == keyboard.Key.f5:
            self.switchparam("WORLDEVENT_ENABLED")
    
    def _on_release(self, key):
        print('{0} release'.format(
        key))
        #if key == Key.esc:
        #     Stop listener
        #    return False

    #fonction qui change la valeur CONFIG de vraie a faux et vice versa
    def switchparam(self, valuename):
        Value = CONFIG.get(valuename)
        if Value:
            CONFIG.update({valuename: False})
        elif Value == False:
            CONFIG.update({valuename: True})
