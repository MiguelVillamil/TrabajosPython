from termcolor import colored
def menu():
  print(colored("Deseas elevar numeros al cuadrado? \n","yellow"))
  print(colored("1. si\n","green"))
  print(colored("2. no\n","red"))
  respuesta= input("")
  return respuesta

def menu2():
  print(colored("Que deseas hacer?\n","yellow"))
  print(colored("1. hacer prueba (-10 hasta 10)\n","green"))
  print(colored("2.ingresar numero\n","green"))
  print(colored("3.salir\n","red"))
  respuesta= input("")
  return respuesta

def ingresar_num():
  num1= float(input(colored("ingrese el numero\n","cyan")))
  return num1


def elev2(num):
  num1=num
  num2= 2.0
  print(num1,colored(" al cuadrado ","green"),"\n")
  return num1**num2

def ciclo_prueba():
  i=-10
  while (i<11):
    muestrares(elev2(i))
    i=i+1

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))


def muestrares(num):
  print(colored("La respuesta es: ","green"),num,"\n")

def finalizar():
  print(colored("Programa finalizado","red") )

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if(opcion=="1"):
      salida2=False
      while(salida2==False):
        opcion=menu2()
        if(opcion=="1"):
          ciclo_prueba()
          continuar()
        else:  
          if(opcion=="2"):
            muestrares(elev2(ingresar_num()))
            continuar()
          else:
            if(opcion=="3"):
              salida2=True
              continuar()
            else:
              print(colored("No ha ingresado una opcion correcta","red") )
              continuar()
    else:
      if(opcion=="2"):
        salida=True
        print(colored("Gracias por usar el programa \n","red") )
        finalizar()
      else:   
        print(colored("No ha ingresado una opcion correcta","red") )
        continuar()         

main()