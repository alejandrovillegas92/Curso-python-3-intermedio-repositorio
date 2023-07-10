#Calculator
print('Bienvenido a tu calculadora!')
operacion=int(input("""Elija la operacion a realizar:
                            1: Suma
                            2: Resta
                            3: Multiplicacion
                            4: Division: """))
if operacion == 1:
  print('Has elejido suma')
  def suma_numeros():
    numeros=[]

    while True:
      numero = input("Ingresa los numeros a sumar o presiona z para finalizar: ")

      if numero.lower() =='z':
        print("Gracias")
        break

      numeros.append(int(numero))

    suma=sum(numeros)

    return suma

  resultado=suma_numeros()

  print('La suma de los numeros es: ', resultado)


if operacion == 2:
  print('Has elegido resta')
  def resta_numeros():
    numeros=[]

    while True:
      numero = input("Ingresa los numeros a restar o presiona z para finalizar: ")

      if numero.lower() =='z':
        print("Gracias")
        break

      numeros.append(int(numero))

    resultado = numeros[0] - sum(numeros[1:])

    return resultado

  resultado=resta_numeros()

  print('La resta de los numeros es: ', resultado)


if operacion == 3:
  print('Has elegido multiplicacion')
  def multiplicar_numeros():
    numeros=[]

    while True:
      numero = input("Ingresa los numeros a multiplicar o presiona z para finalizar: ")
      resultado=1
      if numero.lower() =='z':
        print("Gracias")
        break

      numeros.append(int(numero))

    for num in numeros:
      resultado *= num

    return resultado

  resultado=multiplicar_numeros()

  print('La multiplicacion de los numeros es: ', resultado)



if operacion == 4:
  print('Has elegido division')
  def dividir_numeros():
    numeros=[]

    while True:
      numero = input("Ingresa los numeros a dividir o presiona z para finalizar: ")

      if numero.lower() =='z':
        print("Gracias")
        break

      numeros.append(int(numero))

    resultado= numeros[0]
    for num in numeros[1:]:
      resultado /= num

    return resultado

  resultado=dividir_numeros()

  print('La dividir de los numeros es: ', resultado)

else:
  print('Operacion no valida')