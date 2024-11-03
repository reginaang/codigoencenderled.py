import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Configura el LED en el pin 2

while True:
    led.on()   # Enciende el LED
    time.sleep(2)  # Espera 1 segundo
    led.off()  # Apaga el LED
    time.sleep(2)  # Espera 1 segundo
