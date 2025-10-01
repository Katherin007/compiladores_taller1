 # numero = input("Ingrese un número: ") 
 #if numero % 2 == 0 : 
  #print("El número es par") 
#else: 
  #print("El número es impar")//
  
  # 1. Solicita la entrada y la guarda como cadena.
entrada = input("Ingrese un número: ")

# 2. Convierte la cadena a un número entero (int) para poder usar el operador %.
try:
    numero = int(entrada)
except ValueError:
    print("Error: No ingresó un número válido.")
else:
    # 3. La condición del 'if' debe terminar con dos puntos (:)
    #    y la operación de módulo debe ser 'numero % 2 == 0'.
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")