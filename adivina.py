import random

def adivinar_numero():
    jugando = True
    
    while jugando:
        # Se elige el número aleatorio entre 1 y 100
        numero = random.randint(1, 100)

        # Variables para guardar los intentos del jugador y la CPU
        intentos_usuario = []
        intentos_computadora = []
        
        # Control de los turnos (True es el usuario y False es la computadora)
        turno = True
        partida_en_curso = True
        
        print("\n¡Comienza una nueva partida!")
        
        # Ciclo del juego
        while partida_en_curso:
            if turno:
                # Turno del usuario
                try:
                    intento_usuario = int(input("Es tu turno, adivina un número entre 1 y 100: "))
                except ValueError:
                    print("Por favor, introduce un número válido.")
                    continue
                
                if intento_usuario < 1 or intento_usuario > 100:
                    print("El número debe estar entre 1 y 100.")
                    continue

                intentos_usuario.append(intento_usuario)

                if intento_usuario == numero:
                    print(f"¡Lo has adivinado! El número era {numero}")
                    print(f"Intentos del usuario: {intentos_usuario}")
                    print(f"Intentos de la computadora: {intentos_computadora}")
                    partida_en_curso = False
                elif intento_usuario < numero:
                    print("El número es mayor.")
                else:
                    print("El número es menor.")

                turno = False
            
            if not turno and partida_en_curso:
            # Turno de la CPU
                intento_computadora = random.randint(1, 100)
                print(f"Es mi turno, elijo el número: {intento_computadora}")
                intentos_computadora.append(intento_computadora)

                if intento_computadora == numero:
                    print(f"¡He adivinado el número! Era {numero}")
                    print(f"Intentos del usuario: {intentos_usuario}")
                    print(f"Intentos de la computadora: {intentos_computadora}")
                    partida_en_curso = False
                elif intento_computadora < numero:
                    print("El número es mayor.")
                else:
                    print("El número es menor.")
                
                turno = True # Turno del usuario
        
        # Preguntar si el usuario quiere jugar otra vez
        while True:
            jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if jugar_de_nuevo == 's':
                break # Inicia otra partida
            elif jugar_de_nuevo == 'n':
                jugando = False
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
            else:
                print("Por favor, responde con 's' para sí o 'n' para no.")

# Ejecutar el juego
adivinar_numero()
