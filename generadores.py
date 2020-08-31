# Funciones generadoras
# Estas nos sirven para iterar elementos de una coleccion
# sin la necesidad de obtener todos los resultados.

"""
# Forma tradicional
def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num * 2)
        num += 1
    return miLista

limite = int(input("Digite cuantos numeros pares desea: "))
print(generaPares(limite))
"""

# Forma generador
def generaPares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1

def siguientePar(generador):
    print(next(generador))

limite = int(input("Digite cuantos numeros pares desea: "))
devuelvePares = generaPares(10)
#
#for numeroPar in devuelvePares:
#    print(f"Numero par: {numeroPar}")
#
#print("Se ha recorrido la lista")

while True:
    opcion = int(input("Digite un numero: "))
    if opcion == 1:
        siguientePar(devuelvePares)

# Yield From
# Simplificación de los bucles anidados
def devuelveLetrasCiudades(*ciudades): #Un * indica que no está determinado el numero de elementos
    for ciudad in ciudades:
        #for letra in ciudad:
        #    yield letra
        yield from ciudad