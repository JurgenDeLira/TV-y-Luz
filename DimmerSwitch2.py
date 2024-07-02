# Clase DimmerSwitch
class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False    # Indica si el interruptor está encendido o apagado
        self.brightness = 0        # Nivel de brillo actual

    def turnOn(self):
        self.switchIsOn = True     # Enciende el interruptor

    def turnOff(self):
        self.switchIsOn = False    # Apaga el interruptor

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1    # Aumenta el nivel de brillo en 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1    # Reduce el nivel de brillo en 1

    # Método adicional para depuración (debugging)
    def show(self):
        print('¿El interruptor está encendido?', self.switchIsOn)    # Muestra el estado del interruptor
        print('El nivel de brillo es:', self.brightness)    # Muestra el nivel de brillo actual

# Crear el primer DimmerSwitch, encenderlo y aumentar el nivel dos veces
objeto_Dimmer1 = DimmerSwitch('Dimmer1')
objeto_Dimmer1.turnOn()
objeto_Dimmer1.raiseLevel()
objeto_Dimmer1.raiseLevel()

# Crear el segundo DimmerSwitch, encenderlo y aumentar el nivel tres veces
objeto_Dimmer2 = DimmerSwitch('Dimmer2')
objeto_Dimmer2.turnOn()
objeto_Dimmer2.raiseLevel()
objeto_Dimmer2.raiseLevel()
objeto_Dimmer2.raiseLevel()

# Crear el tercer DimmerSwitch, usando la configuración predeterminada
objeto_Dimmer3 = DimmerSwitch('Dimmer3')

# Pedir a cada interruptor que se muestre a sí mismo
objeto_Dimmer1.show()
objeto_Dimmer2.show()
objeto_Dimmer3.show()