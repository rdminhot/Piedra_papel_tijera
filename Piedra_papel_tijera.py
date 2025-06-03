
turno= 0

while turno < 3:
    jugador_1=input('Hola jugador uno. Que elijes? Piedra, papel o tijera?: ').lower()
    jugador_2=input('Hola jugador dos. Que elijes? Piedra, papel o tijera?: ').lower()

    if jugador_1==jugador_2:
        print('Empate')
    elif jugador_1 == ('tijera') and jugador_2 ==('papel'):
        print('gana jugador 1')
    elif jugador_1 == ('piedra') and jugador_2 == ('tijera'):
        print('Gana jugador 1')
    elif jugador_1== ('papel') and jugador_2== ('piedra'):
        print('GGana jugador 1')
    else:
        print('Gana jugador 2')
    turno +=1
    print(jugador_1)
    print(jugador_2)
print('Terminaron los intentos')