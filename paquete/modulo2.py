def fifaa():
    futbolistas = []

    while True:
        jugador = input("Ingresa el nombre de un futbolista favorito (o escribe 'salir' para terminar): ")
        if jugador.lower() == 'salir':
            break
        futbolistas.append(jugador)

    if not futbolistas:
        print("No has ingresado jugadores en tu top.")
    else:
        print("Tu top de jugadores favoritos:")
        for i, jugador in enumerate(futbolistas, start=1):
            print(f"{i}. {jugador}")
            
