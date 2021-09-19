# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']
    
    lista_digit = [int(x) if x.isdigit() else 0 for x in list_numeros_str]
    print(lista_digit)

    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?
    
    list_numeros_str2 = ['5', '2', '-3', '', '7', 'NaN']
    lista_digit2 = [int(x) if x.isdigit() else 0 for x in list_numeros_str2]
    print(lista_digit2)
        
    def is_numero(num):
        numero = False
        try: 
            int(num)
            numero = True
        except ValueError:
            numero = False #Sé que no es buena práctica manejar una excepción así pero para la finalidad de la función no necesitaba más.
        return numero
      
    list_numeros_str3 = ['5', '2', '-3', '', '7', 'NaN']            
            
    lista_numeric = [int(x) if is_numero(x) == True else 0 for x in list_numeros_str3]
    print(lista_numeric)

    print("terminamos")
