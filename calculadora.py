class Calculadora:
    def __init__(self):
        """
        Inicializa la calculadora
        """
        self.historial = []

    def suma(self, num1, num2):
        """
        Realiza la suma de dos números
        """
        resultado = num1 + num2
        self.guardar_operacion('suma', num1, num2, resultado)
        return resultado

    def resta(self, num1, num2):
        """
        Realiza la resta de dos números
        """
        resultado = num1 - num2
        self.guardar_operacion('resta', num1, num2, resultado)
        return resultado

    def multiplicacion(self, num1, num2):
        """
        Realiza la multiplicación de dos números
        """
        resultado = num1 * num2
        self.guardar_operacion('multiplicación', num1, num2, resultado)
        return resultado

    def division(self, num1, num2):
        """
        Realiza la división de dos números
        """
        if num2 == 0:
            raise ValueError("No es posible dividir entre cero")
        resultado = num1 / num2
        self.guardar_operacion('división', num1, num2, resultado)
        return resultado

    def potencia(self, num1, num2):
        """
        Calcula la potencia de un número
        """
        resultado = num1 ** num2
        self.guardar_operacion('potencia', num1, num2, resultado)
        return resultado

    def raiz_cuadrada(self, num):
        """
        Calcula la raíz cuadrada de un número
        """
        if num < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        resultado = num ** 0.5
        self.guardar_operacion('raíz cuadrada', num, None, resultado)
        return resultado

    def guardar_operacion(self, operacion, num1, num2, resultado):
        """
        Guarda la operación en el historial
        """
        if num2 is not None:
            self.historial.append(f"{operacion}: {num1} y {num2} = {resultado}")
        else:
            self.historial.append(f"{operacion} de {num1} = {resultado}")

    def mostrar_historial(self):
        """
        Muestra el historial de operaciones
        """
        print("\n=== Historial de Operaciones ===")
        for operacion in self.historial:
            print(operacion)

def obtener_numero(mensaje):
    """
    Obtiene y valida un número ingresado por el usuario
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Por favor ingrese un número válido")

def mostrar_menu():
    """
    Muestra el menú de opciones
    """
    print("\n=== CALCULADORA AVANZADA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Ver Historial")
    print("8. Salir")

def main():
    """
    Función principal del programa
    """
    calc = Calculadora()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una operación (1-8): ")
        
        if opcion == '8':
            print("¡Gracias por usar la calculadora!")
            break
            
        try:
            if opcion in ['1', '2', '3', '4', '5']:
                num1 = obtener_numero("Ingrese el primer número: ")
                num2 = obtener_numero("Ingrese el segundo número: ")
                
                if opcion == '1':
                    resultado = calc.suma(num1, num2)
                    print(f"\n{num1} + {num2} = {resultado}")
                elif opcion == '2':
                    resultado = calc.resta(num1, num2)
                    print(f"\n{num1} - {num2} = {resultado}")
                elif opcion == '3':
                    resultado = calc.multiplicacion(num1, num2)
                    print(f"\n{num1} * {num2} = {resultado}")
                elif opcion == '4':
                    resultado = calc.division(num1, num2)
                    print(f"\n{num1} / {num2} = {resultado}")
                elif opcion == '5':
                    resultado = calc.potencia(num1, num2)
                    print(f"\n{num1} ^ {num2} = {resultado}")
                    
            elif opcion == '6':
                num = obtener_numero("Ingrese el número: ")
                resultado = calc.raiz_cuadrada(num)
                print(f"\nLa raíz cuadrada de {num} = {resultado}")
                
            elif opcion == '7':
                calc.mostrar_historial()
                
            else:
                print("\nOpción no válida. Por favor intente de nuevo.")
                
        except ValueError as e:
            print(f"\nError: {str(e)}")
        except Exception as e:
            print(f"\nError inesperado: {str(e)}")

if __name__ == "__main__":
    main()