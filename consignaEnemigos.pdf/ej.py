##Thiago Gomez PREP 4to

## Escribir una funcion que reciba un archivo
## e intente leer los datos del siguiente enemigo
##Si no hay mas enemigos debe devolver None
##Si hay más enemigos devuelve una lista de 
## 4 valores: Nombre, vida, daño, probabilidad
## de daño golpe, menos el nombre los otros valores
## deben ser ints
import random 
def leerEnemigo(a):
    nombre = a.readline().strip()
    
    if not nombre:
        return None
    
    vida = int(a.readline().strip())
    fuerza = int(a.readline().strip())
    probabilidad = int(a.readline().strip())
    
    return [nombre, vida, fuerza, probabilidad]

def cacularAtaque(probabilidad, fuerza, vida):
    ataque = random.randint(1, 100)
    if ataque <= probabilidad:
        print(f"Ataque éxitoso. Hace {fuerza} de daño.")
        vida -= fuerza
    else:
        print(f"Ataque errado. ")
    return max(vida, 0)

a = open("enemigos.txt", "r")


##

##
##  Vida: 30
##  Esqueleto (vida: 10)
##
enemigo = leerEnemigo(a)
vida = 30
probabilidad=80
fuerza=3
print(f"vida: {vida}")
while enemigo != None and vida > 0:
    print(f"\nvida: {vida}")
    print(f"Enemigo: {enemigo[0]}, vida: {enemigo[1]}")
    
    ## Turno del jugador: elegir acción
    accion = ""
    while accion not in ["1", "2"]:
        print("\nTu turno: ")
        print("1. Atacar")
        print("2. Curarse")
        accion = input("Elige una acción (1/2): ")
    
    ## Se ejecuta la habilidad elegida del jugador
    if accion == "1":
        enemigo[1] = cacularAtaque(probabilidad, fuerza, enemigo[1])
        if enemigo[1] <= 0:
            print(f"{enemigo[0]} fue derrotado!")
            
     # Cargar siguiente enemigo o anunciar victoria
            enemigo = leerEnemigo(a)
            if enemigo is not None:
                print(f"\n¡Se aproxima un {enemigo[0]}!")
            else:
                print("\n¡Ganaste! Derrotaste a todos los enemigos.")
            continue
    elif accion == "2":
        cura = random.randint(3, 8)
        vida += cura
        print(f"Te curaste {cura} puntos de vida. Ahora tienes {vida}.")
    
    ## Si el enemigo todavía no fue derrotado, ataca
    if enemigo != None and enemigo[1] > 0:
        print(f"\n{enemigo[0]} ataca!")
        vida = cacularAtaque(enemigo[3], enemigo[2], vida)
        if vida <= 0:
            print("Has sido derrotado...")
            break
    
    #enemigo = leerEnemigo(a)

a.close()
