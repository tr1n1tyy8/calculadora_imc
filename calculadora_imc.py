"""
CALCULADORA DEL IMC
"""

def calculadora_imc():

    print("\nCALCULADORA DEL IMC\n")

    while True: # Hacemos este bucle para que continúe ejecutándose el programa en caso de introducir valores no permitidos

        try:

            peso = float(input("Introduzca su peso en kilogramos (con decimales): "))  # Los decimales deben estar separados por un punto. EJ: 60.5
            altura = float(input("Introduzca su altura en metros (con decimales): "))  # Los decimales deben estar separados por un punto. EJ: 1.72

            if peso <= 0 or altura <= 0:
                print("\nHa introducido valores no permitidos, vuelva a intentarlo\n")  # No se puede pesar ni medir 0 o menos, así que esto comprueba que no se introduzcan esos valores
                continue

            break

        except ValueError:
            print("ERROR: Ha introducido un caracter distinto a un número") # Usamos un bloque try-except para verificar que la entrada de datos sea numérica. Si no lo es, lanzará un error

    resultado = round(peso / (altura ** 2), 2)  # Implementamos la fórmula del IMC y la almacenamos en una variable que redondeamos en un máximo de 2 decimales
    return (f"Su IMC es de:  {resultado}")
    
imc = calculadora_imc()
print(imc)
