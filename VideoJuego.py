class Videojuego():
  def __init__(self):
    self.isOn = False
    self.salud = 3
    self.SALUD_MINIMUM = 0
    self.SALUD_MAXIMUM = 6
    self.puntos = 0
    self.PUNTOS_MINIMUM = 0
    self.PUNTOS_MAXIMUM = 100

  def power(self):
    self.isOn = not self.isOn

  def saludUp(self):
    if not self.isOn:
      return
    if self.salud < self.SALUD_MAXIMUM:
      self.salud = self.salud + 1

  def saludDown(self):
    if not self.isOn:
      return
    if self.salud > self.SALUD_MINIMUM:
      self.salud = self.salud - 1
    if self.salud == 0:
      self.scoreReset()

  def scoreUp(self):
    if not self.isOn:
      return
    if self.salud == 0:
      return
    if self.puntos < self.PUNTOS_MAXIMUM:
      self.puntos = self.puntos + 10

  def scoreReset(self):
    self.puntos = 0

  def showInfo(self):
    print('Estado del Videojuego:')
    if self.isOn:
      print('    La consola está: Encendida')
      if self.salud == 0:
        print('    Tu partida ha terminado')
      else:
        print('    Tu barra de salud esta en:', self.salud)
        print('    Tu puntaje es de :', self.puntos)
    else:
      print('    La consola está: Apagada')


# Código principal
objeto_Videojuego = Videojuego()  

objeto_Videojuego.power()
objeto_Videojuego.showInfo()

objeto_Videojuego.power()
objeto_Videojuego.showInfo()

objeto_Videojuego.power()
objeto_Videojuego.saludUp()
objeto_Videojuego.saludUp()
objeto_Videojuego.saludUp()
objeto_Videojuego.showInfo()

objeto_Videojuego.saludDown()
objeto_Videojuego.saludDown()
objeto_Videojuego.saludDown()
objeto_Videojuego.saludDown()
objeto_Videojuego.showInfo()

objeto_Videojuego.scoreUp()
objeto_Videojuego.scoreUp()
objeto_Videojuego.scoreUp()
objeto_Videojuego.scoreUp()
objeto_Videojuego.showInfo()

objeto_Videojuego.saludDown()
objeto_Videojuego.saludDown()
objeto_Videojuego.showInfo()

objeto_Videojuego.saludUp()
objeto_Videojuego.saludUp()
objeto_Videojuego.saludUp()
objeto_Videojuego.showInfo()










"""

class TV():
  def __init__(self):
    self.isOn = False
    self.isMuted = False
    # Algunos canales predeterminados
    self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
    self.nChannels = len(self.channelList)
    self.channelIndex = 0
    self.VOLUME_MINIMUM = 0    # constante
    self.VOLUME_MAXIMUM = 10   # constante
    self.volume = self.VOLUME_MAXIMUM // 2

  def power(self):
    self.isOn = not self.isOn   # toggle

  def volumeUp(self):
    if not self.isOn:
      return
    if self.isMuted:
      self.isMuted = False     # cambiar el volumen mientras está silenciado reactiva el sonido
    if self.volume < self.VOLUME_MAXIMUM:
      self.volume = self.volume + 1

  def volumeDown(self):
    if not self.isOn:
      return
    if self.isMuted:
      self.isMuted = False     # cambiar el volumen mientras está silenciado reactiva el sonido
    if self.volume > self.VOLUME_MINIMUM:
      self.volume = self.volume - 1

  def channelUp(self):
    if not self.isOn:
      return
    self.channelIndex = self.channelIndex + 1
    if self.channelIndex >= self.nChannels:   # si el índice del canal excede el número de canales
      self.channelIndex = 0   # volver al primer canal

  def channelDown(self):
    if not self.isOn:
      return
    self.channelIndex = self.channelIndex - 1
    if self.channelIndex < 0:    # si el índice del canal es menor que cero
      self.channelIndex = self.nChannels - 1    # volver al último canal

  def mute(self):
    if not self.isOn:
      return
    self.isMuted = not self.isMuted

  def setChannel(self, newChannel):
    if newChannel in self.channelList:
      self.channelIndex = self.channelList.index(newChannel)
    # si el nuevo canal no está en nuestra lista de canales, no hace nada

  def showInfo(self):
    print('Estado del TV:')
    if self.isOn:
      print('    La TV está: Encendida')
      print('    El canal es:', self.channelList[self.channelIndex])
      if self.isMuted:
        print('    El volumen es:', self.volume, '(el sonido está silenciado)')
      else:
        print('    El volumen es:', self.volume)
    else:
      print('    TV está: Apagado')


# Clase TV con código de prueba
# --- Aquí se omite el código de la clase TV ---

# Código principal
objeto_tv = TV()  # crear el objeto TV
# Encender el TV y mostrar el estado
objeto_tv.power()
objeto_tv.showInfo()

# Cambiar el canal dos veces hacia arriba, aumentar el volumen dos veces, mostrar estado
objeto_tv.channelUp()
objeto_tv.channelUp()
objeto_tv.volumeUp()
objeto_tv.volumeUp()
objeto_tv.showInfo()

# Apagar el TV, mostrar estado, encender el TV, mostrar estado
objeto_tv.power()
objeto_tv.showInfo()
objeto_tv.power()
objeto_tv.showInfo()

# Bajar el volumen, silenciar el sonido, mostrar estado
objeto_tv.volumeDown()
objeto_tv.mute()
objeto_tv.showInfo()

# Cambiar el canal a 11, silenciar el sonido, mostrar estado
objeto_tv.setChannel(11)
objeto_tv.mute()
objeto_tv.showInfo()
"""