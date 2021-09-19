# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas para filtrar

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # La lista accesso contiene los números de ID de personal
    # que ingresaron por ese molinete

    # 1)
    # Generar una lista por comprensión de la lista "accesos"
    # una lista que solo contenga (filtrado) los ID de personal
    # entre 1 al 10 inclusive, se desea separar del grupo de accesos
    # los ID entre el 1 y 10.
    # De la lista resultante informar cuantas personas/personal
    # comprendido en dicho rango pasó por ese molinete

    # personal_1_10 = [.....]
    print("EJERCICIO 1:\n")
    
    # SOLUCIÓN 1:
    personal_1_10 = [x for x in accesos if x in range(1,11)]
    print(f"S1. ACCESOS POR MOLINETE: {personal_1_10}, {len(personal_1_10)} personas.\n")
    
    # SOLUCIÓN 2:
    personal_1_10_a = list(filter(lambda x: (x in range(1,11)),accesos))
    
    print(f"S2. Han pasado por el molinete un total de {len(personal_1_10_a)} personas; {personal_1_10_a}.\n")
    
    # SOLUCIÓN 3:
    accesos_filtrados = accesos.copy()
    def filtrar(x,lista):
        lista.remove(x)
        return x
    personal_1_10_b = [filtrar(x,accesos) for x in accesos_filtrados if x in range(1,11)]
    print(f"S3. ACCESOS POR MOLINETE: {personal_1_10_b}, {len(personal_1_10_b)} personas.\n")
    
    print(f"ACCESOS FILTRADOS: {accesos}\n")
    
    print("EJERCICIO 2:\n")
    
    # 2)
    # Generar una lista por comprensión de la listas "accesos"
    # cuyo ID de personal esté dentro de los ID válidos para ingresar
    # por ese molinete:
    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]
    id_validos = [3, 4, 7, 8, 15]
    # Debe generar una nueva lista basada en "accesos" filtrada por los ID
    # aprobados en "id_validos".
    # TIP: Utilizar el operador "in" para chequear si un ID de accesos está
    # dentro de "id_validos"

    # personal_valido = [.....]
    personal_valido = [x for x in accesos if x in id_validos]
    print(f"PERSONAL VÁLIDO: {personal_valido}\n")
    print("terminamos")
