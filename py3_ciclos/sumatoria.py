from termcolor import colored 

def sumatoria_ejem1(A,B,C):
  n= len(A)
  sumatoria=0
  for i in range(n):
    ab=A[i]*B[i]
    sumatoria+=(ab+C[i])
  return str(sumatoria + n**2)

def Crea_lista(n):
  lista=[]
  for i in range(int(n)):
    istr=str(i+1)
    lista.append(float(input(colored("ingrese el valor #"+istr+": \n","yellow"))))
  return lista  


def finalizar():
  print(colored("Programa finalizado","red") )



def menu():
  print(colored("Ejercicio sumatoria \n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. sumatoria ejemplo\n","green"))
  print(colored("2. sumatoria valores personalizados\n","green"))
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