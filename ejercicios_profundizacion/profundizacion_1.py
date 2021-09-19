# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Empecemos a jugar con las listas y su métodos, el objetivo
es realizar el código lo más simple, ordenado y limpio posible,
no utilizar bucles donde no haga falta, no "re inventar" una función
que ya dispongamos de Python. El objetivo es:

1) Generar una lista 3 numéros aleatorios con random (pueden repetirse),
    que estén comprendidos entre 1 y 10 inclusive
    (NOTA: utilizar comprension de listas tal como se hizo en clase)
2) Luego de generar la lista sumar los números y ver si el resultado
    de la suma es menor o igual a 21
    a) Si el número es menor o igual a 21 se imprime en pantalla
        la suma y los números recoletados
    b) Si el número es mayor a 21 se debe informar al usuario que perdio
'''
from random import choices, randint,randrange, choice
if __name__ == '__main__':
    print('Comenzamos a divertirnos!\n')
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

    lista_rand = [randint(1,10) for x in range(3)]
    print(lista_rand,"\n")
    print("SOLUCION 1:")
    def suma_21(lista:list) -> str:
        rta = ""
        total = sum(lista)
        if total <= 21:
            rta = f"SUMA TOTAL: {total} - NUMEROS RECOLECTADOS: {lista}"
        else:
            rta = f"LA SUMA TOTAL ES: {total}. PERDIÓ PORQUE SE HA PASADO DE 21."
        
        return rta
    
    print(suma_21(lista_rand))
    print("\n")
    
    # NOTA: Podría no haber usado una función, para hacer el código más "corto", 
    # pero no sería escalable o reutilizable, y por lo tanto, a la larga sería más largo e ineficiente.
    # También podría hacerse una función que devuelva un bool, para simplemente evaluar si se pasa o no de 21:
    
    print("SOLUCION 2:")
    
    def se_paso(lista:list)->bool:
        perdio = False
        if sum(lista)>21:
            perdio = True
        
        return perdio
        
    if se_paso(lista_rand)==True:
        print(f"LA SUMA TOTAL ES: {sum(lista_rand)}. PERDIÓ PORQUE SE HA PASADO DE 21.")
    else:
        print(f"SUMA TOTAL: {sum(lista_rand)} - NUMEROS RECOLECTADOS: {lista_rand}")
    
    
    
    print("\n")
    print("terminamos")
