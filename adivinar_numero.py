import random # Importamos el módulo random para generar números aleatorios

# Inicializo la clase JuegoAdivinanza la cual maneja todas funciones del juego
class JuegoAdivinanza:
  def __init__(self):
    self.numero_random = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 10
    self.numeros_ingresados = []  # Lista para almacenar los números ingresados por el usuario
    self.intentos = 5  # Número máximo de intentos permitidos

  # Método para comparar el número ingresado por el usuario con el número aleatorio generado
  def comparar_numeros(self, numero_ingresado):
    if numero_ingresado == self.numero_random:
      print("Felicidades, has ganado")  # Mensaje de felicitación si el número es correcto
      return True  # Retorna True indicando que el juego ha terminado
    elif len(self.numeros_ingresados) == 5:
      print("Has perdido")  # Mensaje de juego perdido si se alcanza el límite de intentos
      print(f"El número correcto era {self.numero_random}.")  # Muestra el número correcto
      return True  # Retorna True indicando que el juego ha terminado
    return False  # Retorna False si el juego no ha terminado

  # Método para mostrar la cantidad de intentos restantes al usuario
  def validar_intentos(self):
    if len(self.numeros_ingresados) == 1:
      print(f"Has intentado 1 vez, aún te quedan {self.intentos} intentos")
    elif len(self.numeros_ingresados) < 5:
      print(f"Has intentado {len(self.numeros_ingresados)} veces, aún te quedan {self.intentos} intentos")
    else:
      print("Has alcanzado el máximo de intentos.")

  # Método para validar si el número ingresado por el usuario es válido
  def validar_numero_ingresado(self, numero_ingresado):
    if numero_ingresado.isdigit():
      numero_ingresado = int(numero_ingresado)
      if 1 <= numero_ingresado <= 10:
        return True, numero_ingresado  # Retorna True y el número ingresado si es válido
      else:
        print("El número que acabas de ingresar no es válido. Debe estar entre 1 y 10.")
        return False, None  # Retorna False si el número no está dentro del rango válido
    else:
      print("El valor ingresado no es un número válido. Debe ser un dígito entre 1 y 10.")
      return False, None  # Retorna False si el valor ingresado no es un dígito

  # Método para reiniciar el juego si el usuario lo desea
  def reiniciar_juego(self):
    reiniciar = input("¿Desea reiniciar el juego? (s/n): ")
    if reiniciar.lower() == 's':
      self.numero_random = random.randint(1, 10)  # Genera un nuevo número aleatorio
      self.intentos = 5  # Reinicia el número de intentos
      self.numeros_ingresados.clear()  # Limpia la lista de números ingresados
      return True  # Retorna True para reiniciar el juego
    else:
      print("Gracias por jugar, vuelva pronto :)")  # Mensaje de despedida si no se reinicia el juego
      return False  # Retorna False para terminar el juego

  # Método principal para ejecutar el juego
  def jugar(self):
    while True:
      numero_ingresado = input("Ingrese un número entre 1 y 10: ")
      valido, numero_ingresado = self.validar_numero_ingresado(numero_ingresado)
      if not valido:
        continue  # Vuelve a solicitar un número si el ingresado no es válido

      self.numeros_ingresados.append(numero_ingresado)  # Agrega el número ingresado a la lista
      self.intentos -= 1  # Reduce en uno la cantidad de intentos restantes

      self.validar_intentos()  # Llama al método para mostrar los intentos restantes

      if self.comparar_numeros(numero_ingresado):  # Comprueba si se ha adivinado el número o se han agotado los intentos
        if not self.reiniciar_juego():  # Pregunta al usuario si desea reiniciar el juego
          break  # Termina el bucle y el juego si no se reinicia

# Función principal que inicializa la ejecución del programa
def main(): 
  juego = JuegoAdivinanza()  # Crea una instancia de la clase JuegoAdivinanza
  juego.jugar()  # Llama al método jugar para iniciar el juego

main()  