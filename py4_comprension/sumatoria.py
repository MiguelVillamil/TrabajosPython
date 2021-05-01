from termcolor import colored 

def sumatoria_ejem1(A,B,C): #Hace la operacion sumatoria(A_i*B_i+C_i) devuelve el resulta en string
  n= len(A)
  sumatoria=sum((A[i]*B[i])+C[i] for i in range(n))+n**2
  
  return str(sumatoria)

def Crea_lista(n):#permite crear una lista que contien datos float, el parametro n es el numero de datos que contiene la lista 
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
  print(colored("Ejercicio sumatoria \n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. sumatoria ejemplo 2\n","green"))
  print(colored("2. sumatoria 2 valores personalizados\n","green"))
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
      C=[-1,-2,-3,-4]
      print("A= ",A,"\n")
      print("B= ",B,"\n")
      print("C= ",C,"\n")
      print(colored("resultado = ","green"),colored(sumatoria_ejem1(A,B,C)+"\n","cyan"))
    elif(opcion=="2"):
      n=input(colored("ingrese el tamaño de su lista: \n","yellow"))
      print(colored("lista A\n","green"))
      A=Crea_lista(n)
      print(colored("lista B\n","green"))
      B=Crea_lista(n)
      print(colored("lista C\n","green"))
      C=Crea_lista(n)
      print("A= ",A,"\n")
      print("B= ",B,"\n")
      print("C= ",C,"\n")
      print(colored("resultado = ","green"),colored(sumatoria_ejem1(A,B,C)+"\n","cyan"))
    elif(opcion=="3"):   
      salida=True
      print(colored("Gracias por usar el programa","red") )
      finalizar()
    else:
      print(colored("No ha ingresado una opcion correcta","red") )
      continuar()         

main()