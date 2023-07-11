import os
import numpy as np
import Funciones_casa_feliz as fcf

depa=np.empty([10,4],type(object))
fcf.llenarmatriz(depa)
os.system("cls")
op=0
departamento=0
rut=0

while(op!=5):
    os.system("cls")
    print("******************Casa Feliz******************    \n"
    "----------------------------------------------  \n"
    "1.Comprar departamento         \n"
    "2.Mostrar departamentos disponibles   \n"
    "3.Ver listado de compradores    \n"
    "4.Mostrar ganancias totales   \n"
    "5.Salir     ")
    op=fcf.validacionmenu(op)

    if(op==1):
        os.system("cls")
        fcf.mostrarDepaDisponible(depa)
        departamento=fcf.validarDepartamento()
        comprobar=fcf.BuscarDepaDisponible(depa,departamento)
        if(comprobar):
            print("El departamento elegido esta disponible.... ")
            pagar=fcf.comprarDepa(depa,departamento)
            print(" Usted va a pagar: ", pagar)
        else:
            print("El departamento elegido no esta disponible...")
        os.system("pause")

    if(op==2):
        os.system("cls")
        fcf.mostrarDepaDisponible(depa)
        os.system("pause")



    if(op==4):
        suma=0
        suma=fcf.totalDepaComprados(depa)
        if(suma==0):
            print("No hay departamentos vendidos...")
        else:
            print("El total vendido de los departamentos es $",suma)
        os.system("pause")
    
    if(op==5):
        print("Hasta luego...")
        print("Fabian Dominguez 11/7/2023")
