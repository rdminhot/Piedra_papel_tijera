jugador_1=input('Hola jugador uno. Que elijes? Piedra, papel o tijera?: ')
jugador_2=input('Hola jugador dos. Que elijes? Piedra, papel o tijera?: ')
if jugador_1==jugador_2:
    print('Empate')
elif jugador_1 == ('Tijera') and jugador_2 ==('Papel'):
    print('gana jugador 1')
elif jugador_1 == ('Piedra') and jugador_2 == ('Tijera'):
    print('Gana jugador 1')
elif jugador_1== ('Papel') and jugador_2== ('Piedra'):
    print('GGana jugador 1')
else:
    print('Gana jugador 2')

