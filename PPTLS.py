import random
import time
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si el sistema es Windows, se usa cls
        command = 'cls'
    os.system(command)

clearConsole()

cont_maq = 0
cont_jug = 0
juego = int(input("cuantas partidas quieres jugar ?"))
lista=["piedra","papel","tijera","lagarto","spock"]
winer = juego / 2     #saber quien ha ganado la 1/2 + 1 (por tanto gana)

while juego != 0:
    clearConsole()
    jugador = input("Elige tu jugada: ")
    contrario=lista[random.randint(0,4)]
# Versión original, luego lo mejoramos con la lista[]
#    maquina = random.randint(1, 5)
#    if maquina == 1:
#        contrario = "piedra"
#    elif maquina == 2:
#        contrario = "papel"
#    elif maquina == 3:
#        contrario = "tijera"
#    elif maquina == 4:
#        contrario = "lagarto"
#    elif maquina == 5:
#        contrario = "spock"
    
    if contrario == jugador:
        print("Empate!!! Los dos habéis sacado:", jugador)
    elif jugador == "papel":
        if contrario == "piedra" or contrario == "spock":
            print("Has ganado!!!")
            cont_jug += 1
        else:
            print("Has perdido!!!")
            cont_maq += 1
    elif jugador == "piedra":
        if contrario == "tijera" or contrario == "lagarto":
            print("Has ganado!!!")
            cont_jug += 1
        else:
            print("Has perdido!!!")
            cont_maq += 1
    elif jugador == "tijera":
        if contrario == "papel" or contrario == "lagarto":
            print("Has ganado!!!")
            cont_jug += 1
        else:
            print("Has perdido!!!")
            cont_maq += 1
    elif jugador == "lagarto":
        if contrario == "spock" or contrario == "papel":
            print("Has ganado!!!")
            cont_jug += 1
        else:
            print("Has perdido!!!")
            cont_maq += 1
    elif jugador == "spock":
        if contrario == "tijera" or contrario == "piedra":
            print("Has ganado!!!")
            cont_jug += 1
        else:
            print("Has perdido!!!")
            cont_maq += 1
    else:
        print("Introduce bien tu jugada")
        juego += 1
    
    print(contrario)
    juego -= 1

    time.sleep(3)

    if cont_jug > winer:
        juego = 0
        resultado = "Partida GANADA"
    elif cont_maq > winer:
        juego = 0
        resultado = "Partida PERDIDA"

clearConsole()
print(resultado)
print("El resultado final es:")
print("Máquina :", cont_maq, "Jugador :", cont_jug)
