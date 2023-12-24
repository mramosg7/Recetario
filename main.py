import os
from pathlib import Path

#Primero le damos la bienvenida al usuario
print("Bienvenido al Recetario de mramosg7")

#despues le decimos donde se encuentra la ruta de las recetas
ruta = Path(Path(os.getcwd()), 'Recetas')
print(f'Las recetas se encuentran en: {ruta}')

totalRecetas = 0

for txt in Path(ruta).glob('**/*.txt'):
    totalRecetas+=1
# Ahora le ponemos cuantas recetas tenemos en total
print(f'hay un total de {totalRecetas} recetas')
input('')

def elejirCategoria():
    #Esta funcion sirve para mostrar un menu con todas las categorias que hay
    numeroMax = 0
    categoriaSelecionada = 0
    print('[--------Categorías--------]')
    for index, categoria in enumerate(os.listdir(ruta)):
        #Mientras las imprimimos tenemos que sacar el numero maxiomo de categorias que hay
        numeroMax = index
        print(f'[{index + 1}] - {categoria}')

    #Ahora preguntamos que categoria quiere, esto lo hacemos con un bucle para que el usuario no pueda meter numeros incorrectos
    while categoriaSelecionada < 1 or categoriaSelecionada > numeroMax + 1:
        categoriaSelecionada = int(input("Elije una categoria: "))

    #Finalmente returnamos la categoria
    return categoriaSelecionada

def elejirReceta(categoriaSelecionada):
    #Esta funcion sirve para sacar un menu de recetas de una categoria que te pasan por parametro y seleccionar una
    numeroMax = 0
    recetaSelecionada = 0
    print('[--------Recetas--------]')
    recetas = []

    #Recorremos todos los txt de el directorio que nos han pasado
    for index, receta in enumerate(Path(ruta, os.listdir(ruta)[categoriaSelecionada - 1]).glob('*.txt')):

        #Guardamos todas las recetas en una lista para un uso mas facil
        recetas.append(receta)
        numeroMax = index
        print(f'[{index + 1}] - {receta.stem}')

    #Ahora igual que categorias preguntamos la receta que quiere con un bucle while
    while recetaSelecionada < 1 or recetaSelecionada > numeroMax + 1:
        recetaSelecionada = int(input("Elije una receta: "))

    #Por ultimo returnamos el path
    return recetas[recetaSelecionada - 1]
def menu():
    #Esta funcion simplemente es el menu contextual
    os.system('cls')
    print('[--------Recetario--------]')
    print('[1] - Leer receta')
    print('[2] - Crear receta')
    print('[3] - Crear categoría')
    print('[4] - Eliminar receta')
    print('[5] - Eliminiar Categoría')
    print('[6] - Finalizar Programa')

def leerReceta():
    #Esta funcion sirve para la opcion uno de el menu
    os.system('cls')

    #Primero obtenemos el input del menu de categoria
    categoriaSelecionada = elejirCategoria()


    os.system('cls')

    #Y despues obtenemos la receta del menu de recetas
    recetaSelecionada = elejirReceta(categoriaSelecionada)


    os.system('cls')

    #Por último leemos la receta
    print(Path(recetaSelecionada).read_text())
    input('')


def crearReceta():
    #Esta funcion sirve para crear una receta
    os.system('cls')

    #primero le damos al usuario una seleccion de categorias para que elija
    categoriaSelecionada = elejirCategoria()

    os.system('cls')

    #Despues le pedimos el nombre de la receta y su contenido
    nombre = input('Dime el nombre de la receta: ')
    contenido = input('Escribe el contenido de la receta: ')

    #Por ultimo creamos el archivo y escribimos el contenido
    archivo = open(Path(ruta, os.listdir(ruta)[categoriaSelecionada - 1],f'{nombre}.txt'),'w')
    archivo.write(contenido)
    archivo.close()

    print('La receta se ha añadido correctamente.')
    input('')

def crearCategoria():
    #Esta funcion sirve para crear una categoria
    os.system('cls')

    #Simplemente le pedimos el nombre que le quiere dar a la categoria y la creamos
    nombre = input('Dime el nombre de la categoria: ')
    os.makedirs(Path(ruta, nombre))

    print('La categoria se ha creado correctamente')
    input('')

def eliminarReceta():
    #Este metodo sirve para eliminar una receta
    os.system('cls')

    # Primero obtenemos el input del menu de categoria
    categoriaSelecionada = elejirCategoria()

    os.system('cls')

    # Y despues obtenemos la receta del menu de recetas
    recetaSelecionada = elejirReceta(categoriaSelecionada)

    #por último eliminamos esta
    Path(recetaSelecionada).unlink()

    print('Receta eliminada correctamente')
    input('')

def eliminarCategoria():
    #Esta funcion sirve para eliminar la categoria
    os.system('cls')

    #Hacemos que el usuario elija una categoria para eliminar
    categoriaSelecionada = elejirCategoria()

    #y eliminamos la categoria
    os.rmdir(Path(ruta, os.listdir(ruta)[categoriaSelecionada - 1]))

    print('Categoria eliminada correctamente')
    input('')

#Aqui va a ir nuestro bucle con el menu
while True:
    menu()
    opcion = int(input('Elije una opción: '))

    match opcion:
        case 1:
            leerReceta()
        case 2:
            crearReceta()
        case 3:
            crearCategoria()
        case 4:
            eliminarReceta()
        case 5:
            eliminarCategoria()
        case 6:
            break




