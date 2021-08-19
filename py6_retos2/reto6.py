import random
from termcolor import colored 

def NumRand():
  random.seed()
  x=random.randint(1,120)
  
  return x


def finalizar():
  print(colored("Programa finalizado","red") )

def intervalos1_120(n):
  i=""
  if(n>=1 and n<10):
    i="(1,10)"
  elif(n>=10 and n <50):
    i="[10,50)"
  elif(n>=50 and n<100):
   i="[50,100)"
  elif(n>=100 and n<=120):
   i="[100,120]"
  else:
    i="fuera de [1,120]" 

  return i  




def menu():
  print(colored("Ejercicio intervalos\n","yellow"))
  print(colored("que deseas hacer? \n","yellow"))
  print(colored("1. intervalos numero aleatorio entre 0 y 120\n","green"))
  print(colored("2. salir\n","red"))
  respuesta= input("")
  return respuesta



def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
        x=NumRand()
        print(colored("su numero aleatorio es: ","yellow") )
        print(colored(str(x) + "\n","green") )
        print(colored("el intervalo de su numero es:\n ","yellow") )
        print(colored(intervalos1_120(x) + "\n","green") )

        continuar()
      
    
    elif(opcion=="2"):   
        salida=True
        print(colored("Gracias por usar el programa\n","red") )
        finalizar()
    else:
      print(colored("No ha ingresado una opcion correcta\n","red") )
      continuar()    

main()        