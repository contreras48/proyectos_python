import random 
tablero = [
   [" ", " ", " "],
   [" ", " ", " "],
   [" ", " ", " "]
]

f = 0 # fila
c = 0 # columna

turno = "X" if random.randint(0,1) == 0 else "O"

def dibujar_tablero(tablero):
  for i, fila in enumerate(tablero):
    print(f" {fila[0]} | {fila[1]} | {fila[2]} ")
    if (i < 2):
        print("---+---+---")

def validar_ganador(tablero):
  for i in range(3):
    if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
      return tablero[i][0]
    if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
      return tablero[0][i]
  if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
    return tablero[0][0]
  if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
    return tablero[0][2]
  return None

def empate(tablero):
  for fila in tablero:
    for casilla in fila:
      if casilla == " ":
        return False
  return True

while True:
  dibujar_tablero(tablero)
  print(f"Turno de {turno}")
  f = int(input("Fila (0-2): "))
  c = int(input("Columna (0-2): "))
  if tablero[f][c] == " ":
     tablero[f][c] = turno
     turno = "x" if turno == "O" else "O"
  else:
      print("Casilla ocupada")

  ganador = validar_ganador(tablero)

  if ganador:
    dibujar_tablero(tablero)
    print(f"Ganador: {ganador}")
    break

  if empate(tablero):
    dibujar_tablero(tablero)
    print("Empate")
    break
