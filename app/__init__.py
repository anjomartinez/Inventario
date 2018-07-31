import os.path
from app.articulo import Articulo

if __name__ == "__main__":

    while True:
        art = []

        print('\nREGISTRO DE INVENTARIO')
        print("1. Ver Inventario")
        print("2. Agregar Articulo")
        print("3. Modificar Articulo")
        print("4. Eliminar Articulo")
        print("5. Salir")

        try:
            opcion = int(input("Opcion: "))
        except:
            opcion = -1

        if opcion == 1:
            print('\n--Inventario--')

            os.path.isfile("invnt")

            while True:

                    f = open("inventario.txt", "r")
                    linea = f.readline()
                    while linea:
                        data = linea.split(",")
                        print(" Producto: " + data[0] + ", Descripcion: " + data[1] + ", Cantidad: " + data[2]
                              + ", Categoria: " + data[3])
                        linea = f.readline()
                    f.close()
                    break

        elif opcion == 2:
            print("\n--Agregar Articulo--")
            while True:
                n = input("\nNombre: ")


                e = input("Descripcion: ")

                while True:

                    try:
                        p = int (input("Cantidad: "))
                    except:
                        p = -1
                    if p > 0:
                        break
                    else:
                        print("ERROR: Entrada Invalida")

                ca = input ("Categoria: ")
                art.append(Articulo(n, e, p, ca))
                while True:
                    seguir = input("Desea continuar? (S/N): ").upper()
                    if seguir != "N" and seguir != "S":
                        print("Opcion Invalida")
                    else:
                        break
                if seguir == "N":
                    break
                elif seguir == "S":
                    pass
            while True:

                    f = open( "inventario.txt", "a")
                    for elart in art:
                        f.write(str(elart.nombre) + "," + str(elart.descripcion)
                                + "," + str(elart.cantidad) + "," + str(elart.categoria) + "\n")
                    f.close()
                    break

        elif opcion == 3:
            articulo_temp = []
            print('MODIFICAR ARTICULO')
            while True:
                try:
                    f = open("inventario.txt", "r")
                    linea = f.readline()
                    i = 1

                    while linea:
                        articulo_temp.append(linea)
                        data = linea.split(",")
                        print(str(i) + ". " + data[0])
                        linea = f.readline()
                        i += 1

                    f.close()
                    break
                except:
                    print("ERROR: Articulo No Existe.")

            while True:
                try:
                    cambio = int(input("Indique el numero del articulo: "))
                except:
                    cambio = -1
                if cambio > 0:
                    break
                else:
                    print("ERROR: Numero de Articulo Invalido")

            #n = input("\nNombre: ")
            e = input("\nDescripcion: ")
            while True:
                try:
                    p = int(input("Cantidad: "))
                except:
                    p = -1
                if p > 0:
                    break
                else:
                    print("ERROR: Cantidad Invalida")
            ca = input("Categoria: ")
            #articulo_temp[cambio - 1] = str(n) + "," + str(e) + "," + str(p) + "," + str(ca) + "\n"
            articulo_temp[cambio - 1] = str(n) + "," + str(e) + "," + str(p) + "," + str(ca) + "\n"
            while True:
                    f = open("inventario.txt", "w")
                    for articulo in articulo_temp:
                        f.write(articulo)
                    f.close()
                    break

        elif opcion == 4:
            articulo_temp = []
            print('ELIMINAR ARTICULO')
            while True:

                    f = open("inventario.txt", "r")
                    linea = f.readline()
                    i = 1
                    while linea:
                        articulo_temp.append(linea)
                        data = linea.split(",")
                        print(str(i) + ". " + data[0])
                        linea = f.readline()
                        i += 1
                    f.close()
                    break
            while True:
                try:
                    cambio = int(input("Indique el numero del Articulo: "))
                except:
                    cambio = -1
                if cambio > 0:
                    break
                else:
                    print("ERROR: Numero de Articulo Invalido")

            articulo_temp.pop(cambio - 1)

            while True:
                    f = open("inventario.txt", "w")
                    for articulo in articulo_temp:
                        f.write(articulo)
                    f.close()
                    break

        elif opcion == 5:
            exit(0)
        else:
            print("Opcion invalida")
