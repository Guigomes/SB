import pyfiglet
import os
ascii_banner = pyfiglet.figlet_format("BOT DO GOMES")
print(ascii_banner)

value = 0; 

while value != "1" and value != "2" and value != "3":
    print("Escolha sua opção")
    print("1 - Scanner")
    print("2 - Comprar Token Específico")
    print("3 - Comprar Token Específico quando sair liquidez")

    value = input()
  
    if value == "1":
        print("scanner")
        os.system("python BSCTokenSniper1.2/BSCTokenSniper.py")
    elif value == "2": 
        print("c1")
    elif value == "3":
        print("ce")
    else:
        print("Argumento inválido. Informe 1, 2 ou 3")


