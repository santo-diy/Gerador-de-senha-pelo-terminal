from tqdm import tqdm
import time
from menu import menu
from gerador_de_senha import gerador
from duvida import Duvidas_senha
# SantoDiy

while True:
 menu()
 res = input(">")
 
 if res == "1":
     per = int(input("quantos caracter? >"))
     gerador(per)

 elif res == "2":
     Duvidas_senha()
 elif res == "3":
    print("tchau 👋..")
    for i in tqdm(range(2)):
       time.sleep(1)
    break
    
