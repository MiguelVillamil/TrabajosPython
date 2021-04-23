from termcolor import colored
def menu():
  print(colored("Deseas consultar un indice de masa corporal(imc)? \n","yellow"))
  print(colored("1. si\n","green"))
  print(colored("2. no\n","red"))
  respuesta= input("")
  return respuesta

def imc():
  peso=float(input(colored("ingrese el peso en Kg\n","yellow")))
  estatura=float(input(colored("ingrese la estatura en m\n","yellow")))
  return (peso/(estatura**2))

def mostrarimc(imc):
  if(imc<18.5):
    print(colored("su imc es de: ","green"),imc,colored("lo que significa que su peso es bajo","green"))
  else:
    if(imc>=18.5 and imc<25.5):
      print(colored("su imc es de: ","green"),imc,colored("lo que significa que su peso es normal","green"))
    else:
      if(imc>=25.5 and imc<30):
        print(colored("su imc es de: ","green"),imc,colored("lo que significa que su peso es alto","green"))
      else:
        if(imc>30):
          print(colored("su imc es de: ","green"),imc,colored("lo que significa que Tiene Sobrepeso","green"))
        


def finalizar():
  print(colored("Programa finalizado","red") )

def continuar():
  input(colored("Presiona Enter para continuar...","yellow"))

def main():
  salida=False
  while (salida==False):
    opcion=menu()
    if (opcion=="1"):
      mostrarimc(imc())
    else:
      if(opcion=="2"):
        salida=True
        print(colored("Gracias por usar el programa","red") )
        finalizar()
      else:   
        print(colored("No ha ingresado una opcion correcta","red") )
        continuar()         

main()