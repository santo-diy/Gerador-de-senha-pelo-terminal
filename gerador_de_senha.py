from tqdm import tqdm
from rich import print
import secrets
import time
import random
import pyfiglet
import string
import os

#Santodiy

def gerador(valor):
  os.system('cls' if os.name == "nt" else "clear")
  Get = pyfiglet.figlet_format("\nGERADOR DE SENHA")
  print(f"[bold red] {Get} [/bold red]")
  time.sleep(1)
  while True:
    letras = string.ascii_letters
    numeros = string.digits
    caracter = string.punctuation

    tudo = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(tudo) for _ in range(valor))
    print("[bold green] _ [/bold green]" * 20)
    print("")
    print("[bold green] senha: [/bold green]", senha )
    print("[bold green] _ [/bold green]" * 20)
    print("")
    print(f"[bold cyan]ó numero 0 volta para o menu principal[/bold cyan]")
    print("[bold cyan]usar qualquer outro numero, fará que  gere outra senha [/bold cyan]")
    print("")

    volta2 = input(">")
    for i in tqdm(range(3)):
      time.sleep(1)
      
    if volta2 == "0":
       
       os.system("cls" if os.name =="nt" else "clear")
       return
    else:
      os.system('cls' if os.name =="nt" else "clear")
      print(f"[bold red] {Get} [/bold red]")
      print("")
      print("")
      print(f"[bold cyan] nova senha foi gerada[/bold cyan]")
    

