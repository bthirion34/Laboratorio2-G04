"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 * Andres Rodriguez - Última version
 """

import sys
import App.logic as logic


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_logic():
    """
    Se crea una instancia de la logica
    """
    control = logic.new_logic()
    return control


def print_menu():
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")
    print("3- Cargar Book-Tags!!!...")
    print("0- Salir")


def load_books(control):
    """
    Carga los libros
    """
    books = logic.load_books(control,
                                  "GoodReads/books-small.csv")
    return books


def load_tags(control):
    """
    Carga los Tags
    """
    tags = logic.load_tags(control,
                                "GoodReads/tags.csv")
    return tags


def load_books_tags(control):
    """
    Cargar los Tags de libros
    """
    # TODO: Mods de Est-1 en el Lab 2
    pass


def first_book(control):
    """
    Devuelve el primer libro del catalogo
    """
    # TODO: Mods de Est-1 en el Lab 2
    pass


def last_book(control):
    # TODO: Mods de Est-2 en el Lab 2
    """
    Devuelve el último libro cargado
    """
    pass


# Se crea el controlador asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    # ciclo del menu
    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n")
        if int(inputs[0]) == 1:
            print("Cargando información de libros....")
            books = load_books(control)
            print("Total de libros cargados: " + str(books) + "\n")

            # TODO: Mods de Est-1 en el Lab 2
            first = None

            # TODO: Mods de Est-2 en el Lab 2
            last = None

        elif int(inputs[0]) == 2:
            print("Cargando información de tags....")
            tags = load_tags(control)
            print("Total de tags cargados: " + str(tags) + "\n")

        elif int(inputs[0]) == 3:
            print("Cargando información de book-tags...")
            booktags = load_books_tags(control)
            print("Total de book-tags cargados: "+ str(booktags))
        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            print("Opcion erronea, vuelva a elegir.\n")
    sys.exit(0)
