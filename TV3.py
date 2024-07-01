# Clase TV
class TV():
  def __init__(self, marca, ubicacion):  # se pasa una marca y ubicación para el TV
    self.marca = marca
    self.ubicacion = ubicacion
    # --- se omite el resto de la inicialización del TV ---
    # ...
objeto_tv1 = TV('Samsung', 'Sala')
objeto_tv2 = TV('Sony', 'Cuarto')
def showInfo(self):
  print()
  print('Marca de la TV:', self.marca)
  print('    Ubicación:', self.ubicacion)
  if self.isOn:
    print('    La TV está: Encendida')
    print('    El canal es:', self.channelList[self.channelIndex])
    if self.isMuted:
      print('    El volumen es:', self.volume, '(el sonido está silenciado)')
    else:
      print('    El volumen es:', self.volume)
  else:
    print('    TV está: Apagado')

"""La salida al ejecutar este código tendría que ser la siguiente:
 Marca de la TV: Sony
      Ubicación: Sala
      TV esta: On
      Canal es: 2
      Volumen es: 7
  Marca de la TV: Samsung
      Ubicación: Cuarto
      TV esta: On
      Canal es: 44
      Volumen es: 10 (el sonido está silenciado)"""
