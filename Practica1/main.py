from handlers import *

#menu principal de la aplicacion 
def menu():
    print("========= ETL ========== ")
    print("a) Borrar modelo\nb) Crear modelo\nc) Extraer info\nd) Cargar info\ne) Realizar consultas")
    print("f) Salir")
    opc = input()
    return opc

def main():
    opc = ""
    while opc != 'f':
        opc = menu()
        if opc == 'a':
            print("-borrando")
            borrar()
        elif opc == 'b':
            print("-creando")
            crear()
        if opc == 'c':
            print("-extrayendo")
            extraer("./Airline Dataset Updated - v2.csv")
        elif opc == 'd':
            print("-cargando")
            #cargar()
        elif opc == 'e':
            print("-consultando")
            #consultar()
        elif opc == 'f':
            break


main()