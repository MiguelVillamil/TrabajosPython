from termcolor import colored 

def lista_ejem2(A,B): #crea una lista resultante de ((A[i+1]^2)*B[2*i])+B[n+i] la devuelve como string
  n= len(A)//2
  C=[((A[i+1]**2)*B[2*i])+B[n+i]for i in range(n)]
  
  return str(C)

def Crea_lista(n): #permite crear una lista que contiene datos tipo float, el parametro n es la cantidad de datos que posee la lista
  lista=[]
  for i in range(int(n)):
    istr=str(i+1)
    numapro=False
    while(numapro==False):
      try:
        lista.append(float(input(colored("ingrese el valor #"+istr+": \n","yellow"))))
        numapro=True
      except ValueError:
        print(colored("el cararcter ingresado no es un numero ingrese el valor nuevamente","red"))
        numapro=False

  return lista  


def finalizar():
  print(colored("Programa finalizado","red") )



def menu():
  print(colored("Ejercicio Crear lista \n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. crear lista ejemplo 2\n","green"))
  print(colored("2. crear lista 2 valores personalizados\n","green"))
  print(colored("3. salir\n","red"))
  respuesta= input("")
  return respuesta



def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      
      A=[1,2,3,4]
      B=[5,6,7,8]
      
      print("A= ",A,"\n")
      print("B= ",B,"\n")

      print(colored("resultado C= ","green"),colored(lista_ejem2(A,B)+"\n","cyan"))
      continuar()
    elif(opcion=="2"):
      n=input(colored("ingrese el tamaño de sus listas: \n","yellow"))
      print(colored("lista A\n","green"))
      A=Crea_lista(n)
      print(colored("lista B\n","green"))
      B=Crea_lista(n)
      print("A= ",A,"\n")
      print("B= ",B,"\n")
      
      print(colored("resultado C= ","green"),colored(lista_ejem2(A,B)+"\n","cyan"))
      continuar()
    elif(opcion=="3"):   
      salida=True
      print(colored("Gracias por usar el programa","red") )
      finalizar()
    else:
      print(colored("No ha ingresado una opcion correcta","red") )
      continuar()         

main()