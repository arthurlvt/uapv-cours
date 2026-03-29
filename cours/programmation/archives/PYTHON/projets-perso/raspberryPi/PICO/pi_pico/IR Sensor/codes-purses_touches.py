from machine import Pin
from ir_rx import NEC_16

led_1 = Pin(16, Pin.OUT)

ir_key = {
    0x16: '*',
    0x0d: '#',
    0x1c: 'Ok',
    0x18: '↑',
    0x5a: '→',
    0x52: '↓',
    0x08: '←',
    0x19: '0',
    0x45: '1',
    0x46: '2',
    0x47: '3',
    0x44: '4',
    0x40: '5',  # Code pour le bouton "5"
    0x43: '6',
    0x07: '7',
    0x15: '8',
    0x09: '9'    
}

def callback(data, addr, ctrl):
    if data > 0:  # Le protocole NEC envoie des codes de répétition.
        # Vérifie si le code reçu correspond au bouton "5"
        if data == 0x40:
            print("Le bouton 5 a été pressé !")
            if led_1.value() == 0:
                led_1.value(1)
            else:
                led_1.value(0)
        else:
            return;

ir = NEC_16(Pin(15, Pin.IN), callback)
