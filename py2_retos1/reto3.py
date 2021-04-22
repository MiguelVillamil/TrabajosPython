from termcolor import colored
def menu():
  print(colored("Deseas entrar a la calcualdora? \n","yellow"))
  print(colored("1. si\n","green"))
  print(colored("2. no\n","red"))
  respuesta= input("")
  return respuesta

def menu2():
  print(colored("Que deseas hacer?\n","yellow"))
  print(colored("1. suma\n","green"))
  print(colored("2.resta\n","green"))
  print(colored("3. multiplicacion\n","green"))
  print(colored("4.division\n","green"))
  print(colored("5.salir\n","red"))
  respuesta= input("")
  return respuesta


def suma():
  num1= float(input(colored("ingrese el primer numero\n","cyan")))
  num2= float(input(colored("ingrese el segundo numeroo\n","cyan")))
  return num1+num2

def resta():
  num1= float(input(colored("ingrese el primer numero\n","cyan")))
  num2= float(input(colored("ingrese el segundo numeroo\n","cyan")))
  return num1-num2

def mult():
  num1= float(input(colored("ingrese el primer numero\n","cyan")))
  num2= float(input(colored("ingrese el segundo numeroo\n","cyan")))
  return num1*num2

def div():
  num1= float(input(colored("ingrese el primer numero\n","cyan")))
  num2= float(input(colored("ingrese el segundo numeroo\n","cyan")))
  return num1/num2

def muestrares(num):
  print(colored("La respuesta es: ","green"),num,"\n")

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      salida2=False
      while(salida2==False):
        opcion=menu2()
        if(opcion=="1"):
          muestrares(suma())
          continuar()
        else:  
          if(opcion=="2"):
            muestrares(resta())
            continuar()
          else:
            if(opcion=="3"):
              muestrares(mult())
              continuar()
            else:
              if(opcion=="4"):
                muestrares(div())
                continuar()
              else:
                if(opcion=="5"):
                  salida2=True
                  continuar()
                else:
                  print(colored("No ha ingresado una opcion correcta","red") )
                  continuar()  
    else:
      if(opcion=="2"):
        salida=True
        print(colored("Gracias por usar el programa","red") )
      else:   
        print(colored("No ha ingresado una opcion correcta","red") )
        continuar() 


main()

