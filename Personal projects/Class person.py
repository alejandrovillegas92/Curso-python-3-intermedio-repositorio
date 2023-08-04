#Class person

class Presentation:
  def __init__(self, nombre, edad, sexo, nacionalidad, peso, altura):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.nacionalidad =nacionalidad
    self.peso = peso
    self.altura = altura

  def saludo(self):
    return f"Hola! me llamo {self.nombre}, encantado de conocerte."

  def datos(self):
    return f"Tengo {self.edad} años de edad, soy del sexo {self.sexo} y soy {self.nacionalidad} de nacionalidad."

  def datos_salud(self):
    return f"Mi peso es de {self.peso} kilos y mido {self.altura} centimentros."

  def diccionario(self):
    return {'Nombre': self.nombre, 'Edad': self.edad, 'Sexo': self.sexo, 'Nacionalidad': self.nacionalidad, 'Peso': self.peso, 'Altura': self.altura}


persona=Presentation (input('Ingresa tu nombre: '), input('Ingresa tu edad: '), input('Ingresa tu sexo: '), input('Ingresa tu nacionalidad: '), input('Ingresa tu peso: '), input('Ingresa tu altura: '))

print(persona.saludo())

print(persona.datos())

print(persona.datos_salud())

print(persona.diccionario())
