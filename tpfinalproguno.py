Musica = [["Time to pretend", "MGMT", "Yeah I'll miss the boredom \nAnd the freedom and the time spent alone"],
          ["Starman", "David Bowie","Let the children lose it \nLet the children use it \nLet all the children boogie"],
          ["Lago en el Cielo","Gustavo Cerati","Sos el pasaje más soñado \ny sacudiste las más sólidas tristezas\ny respondiste cada vez que te he llamado"],
          ["Infinito","Ainda/Perota Chingó","El miedo confesado ya no es miedo\ncompartido es más liviano\nson palabras en el cielo \ninfinito amor ♥"],
          ["Sol de Invierno","Javiera Mena","Cuando te miro \ncámara lenta \nTus movimientos me dan este sitio \néste silencio \ncomtemplantivo \nCuando consigo a tu lado percibo \nLos diferentes caminos para llegar a tus ojos"]
          ]


def textoMenu():
    print ('Seleccione la opción deseada:\n1:Artistas y Canciones disponibles\n2:Buscar una canción\n3:Almacenar una nueva canción\n4:Modificar canción\n5:Salir\n\nIngrese numero de opción:')
    seleccionar = input()
    return (seleccionar)


def artistasycancionesdisponibles():
    for i in range(len(Musica)):
        print(Musica[i][0] +" - "+ Musica[i][1]+":")
        print(Musica[i][-1])
        print("\n")


def buscarcancion():
    find = None
    busqueda = input("¿Alguna canción que quieras buscar?:\n")
    for cancion in Musica:
        if (busqueda == cancion[0]):
            print("Resultadode la búsqueda: ")
            print(cancion[0] +" - "+ cancion[1]+":")
            print(cancion[-1])
            find = True

    if (not find):
        print("No se encontró, Ingrese una nueva canción")


def almacenarunanuevacancion():
    artista = input("Nombre de la canción que quieras almacenar:")
    cancion = input("Nombre del Artista que quieras agregar:")
    letra = input("La frase que más te guste de la canción que elegiste:")

    Musica.append([artista, cancion, letra])

    print("\n¡Gracias por almacenar una nueva canción a la Lista!")


def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                if matrix[i][j] == element:
                    return (i, j)

seleccionar = ""
while seleccionar != "5":
    seleccionar = textoMenu()

    if seleccionar == '1':
        artistasycancionesdisponibles()
        print("----------------------------\n")
        continue
    if seleccionar == '2':
        buscarcancion()
        print("----------------------------\n")
        continue
    if seleccionar == '3':
        almacenarunanuevacancion()
        print("----------------------------\n")
        continue
    if seleccionar == '4':
        modificarcancion()
        print("----------------------------\n")
        continue
    if seleccionar == '5':
        print('¡Hasta Lueguis!')
        break

    print('Selección incorrecta')
