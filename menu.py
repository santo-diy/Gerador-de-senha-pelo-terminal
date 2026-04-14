from tqdm  import tqdm
from rich import print
import string
import time
import random
import os
#SantoDiy
def menu():
 os.system('cls' if os.name == "nt" else "clear" )
 print("[red]\n ===== MENU =====[/red]")
 print("1   [green] - Gerar senha[/green]")
 print("2   [green] - Duvidas[/green]")
 print("3   [green] - Sair[/green]")
 time.sleep(1)

 print("[bold red]qual opção você quer utlizar? 1, 2 e 3 [/bold red]")
