import os
from rich import print
import pyfiglet
import time

def Duvidas_senha():
 while True:
     DUvidas = pyfiglet.figlet_format("\n== DUVIDAS ==")
     print(f"[bold cyan]{DUvidas}[/bold cyan]")
     time.sleep(1)
     print(f"[bold red][/bold red]")
     print(f"[bold green][/ bold green]")
     print(f"[bold green]1 - senhas fortes e seguras, tem letras Maiúsculas e minúsculas, caracter especiais e numeros, tudo aleatorio.[/bold green]")
     print(f"[bold red]2 - sua conta foi hackeada? eu não me responsabilizo.[/bold red]")
     print(f"[bold green]3 - esse site foi feito pensando em ajuda a fazer senhas fortes e rapidas.[/ bold green]")
     print(f"[bold red]4 - guarde a sua senha ou memorize, o site não armazena sua senha.[/bold red]")
     print(f"[bold green]5- esse site foi feito para ser facil de usar, não tem banco de dados para armazenar suas senhas.[/ bold green]")

     print(f"[bold cyan]EM BREVE[/bold cyan]")

     print(f"[bold red]6 - o site disponibiliza a opção de você escolher quantos Letras quiser, mas o minimo é 8 e o maximo é 24 letras.[/bold red]")
     print(f"[bold green]7 - o site disponibiliza a opção de você escolher 1 a 24 caracter especiais.[/ bold green]")
     print(f"[bold red]8 - o site disponibiliza a opção de escolher 1 a 24 numeros inteiros.[/bold red]")
  
     print(f"[bold cyan]ó numero 0 volta para o menu principal[/bold cyan]")
     volta = input(">")
     if volta == "0":
      os.system("cls" if os.name =="nt" else "clear")
      return
     else:
       os.system("cls" if os.name =="nt" else "clear")
    
   