import os
import random

def validacionmenu(op):
    while(True):
        try:
            op=int(input("Elija la opción deseada: "))
            if(op>=1 and op<=5):
                break
            else:
                print("La opción debe ser entre 1 y 5, vuela a intentarlo.")
        except ValueError:
            print("Debe ser un número entero")
    return op

def llenarmatriz(m):
    q=1
    os.system("cls")
    for i in range(10):
        for j in range(4):
            m[i,j]=q
            q+=1

def mostrarDepaDisponible(depa):
    os.system("cls")
    print("         A       B       C       D ")
    for i in range(10):
        print("\t")
        for j in range(4):
            if(j==1):
                print("\t",depa[i,j],end="    ")
            else:
                print("\t",depa[i,j],end="    ")
    print("  ")

def validarDepartamento():
    departamento=0
    while(True):
        try:
            departamento=int(input("Ingrese el departamento deseado del A1 hasta el D40: "))
            if (departamento>=1 and departamento<=40):
                break
            else:
                print("Error, por favor ingrese un departamento del A1 al D40....")
        except ValueError:
            print("Error, por favor ingrese un departamento del A1 al D40....")
    return departamento

def BuscarDepaDisponible(depa,departamento):
    for b in range(10):
        for x in range(4):
            if(departamento==depa[b,x]):
                return True
    return False

def comprarDepa(depa,departamento):
    for b in range(10):
        for x in range(4):
            if(depa[b,x]==departamento):
                depa[b,x]=x
                if (x==0):
                    pagar=3800
                elif (x==1):
                    pagar=3000
                elif (x==2):
                    pagar=2800
                elif (x==3):
                    pagar=3500
    return pagar


            
def validarRut(rut):
    
    while(True):
        try:
            ru=int(input("Por favor ingrese su rut para la compra: "))
            if(ru>8):
                print("Error.... debe ingresar un rut sin codigo verificador y solo 8 caracteres...")
            else:
                print("Debe ingresar un rut positivo ")
        except ValueError:
            print("Error ingrese un rut valido")
        rut.append(ru)
    


def totalDepaComprados(depa):
    suma=0
    for b in range(10):
        for x in range(4):
            if(depa[b,x]==0):
                if(x==0):
                    suma+=3800
                if(x==1):
                    suma+=3000
                if(x==2):
                    suma+=2800
                if(x==3):
                    suma+=3500
    return suma