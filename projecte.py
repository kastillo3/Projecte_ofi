from sense_hat import SenseHat
import time
import random

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
black = (0,0,0)
pink = (255,105,180)
pell = (171,128,55)
purple = (255,0,255)

def base():
    G = green
    Y = yellow
    B = blue
    O = black
    W = white
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo

def fallo_1():
    G = green
    R = red
    O = black
    W = white
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo

def fallo_2():
    W = white
    O = black

    logo = [
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo

def cabeza():
    O = black
    W = white
    C = pell
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, C, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo
    
def torso():
    O = black
    W = white
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, C, O, O,
    O, O, W, O, O, B, O, O,
    O, O, W, O, O, B, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo
    
def bras_1():
    O = black
    W = white
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, C, O, O,
    O, O, W, O, C, B, O, O,
    O, O, W, O, O, B, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo
    
def bras_2():
    O = black
    W = white
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, C, O, O,
    O, O, W, O, C, B, C, O,
    O, O, W, O, O, B, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo
    
def cama_1():
    O = black
    W = white
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, C, O, O,
    O, O, W, O, C, B, C, O,
    O, O, W, O, O, B, O, O,
    O, O, W, O, C, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo
    
def cama_2():
    O = black
    W = white
    C = pell
    B = blue
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, C, O, O,
    O, O, W, O, C, B, C, O,
    O, O, W, O, O, B, O, O,
    O, O, W, O, C, O, C, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo
    
def muerto():
    O = black
    W = white
    C = pell
    R = red
    L = purple
    logo = [ 
    O, O, O, O, O, O, O, O,
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, L, O, O,
    O, O, W, O, R, R, R, O,
    O, O, W, O, O, R, O, O,
    O, O, W, O, R, O, R, O,
    O, O, W, O, O, O, O, O,
    O, W, W, W, O, O, O, O,
    ]
    return logo

images = [base, fallo_1, fallo_2, cabeza, torso, bras_1, bras_2, cama_1, cama_2, muerto]
#Dins de la llista "images" emmagatzem totes les funcions definides. 

MAX_WRONG = len(images) 
#Emmagatzemem la llargada de la llista.
print "Bienvenido al ahorcado. Buena suerte :)"
WORDS = input("Escriba una palabra: ")
#Demanem la paraula a encertar.
LIST_WORDS=[]
LIST_WORDS+=[WORDS]
#Hem creat una llista de la paraula que ha introduit el usuari.
word = random.choice(LIST_WORDS)
#Elegim la paraula de la llista, com dins la llista nomes hi ha la paraula del usuari, sempre la agafara.
so_far = "-" * len(word)
#Canviem la longitud de la paraula per "-".
wrong = 0
used = []
#Iniciem el contador d'errors i la llista de paraules utilitzades.

while wrong < MAX_WRONG and so_far != word:
#Quan el contador sigui menor de la cantitat de les fincions creades que hi han en la llista
  s.set_pixels(images[wrong % len(images)]())
#Amb això mostre els pixels que hem definit a la funcio  
  print "Has usado las siguientes letras", used
#Imprimeix la llista que conte les lletres que has fet servir
  print "De momento, la palabra es: ", so_far
#Sustitueix la longitud de la paraula per guions.
  guess = input("Introduzca una letra: ")
#Et demana que introdueixis una lletra
  while guess in used:
    print "Ya habia introducido esta letra", guess
    guess = input("Introduzca una letra")
#Mentres la lletra estigui a la llista used,et diu que ja has introduit la lletra i et demana que introdueixis una altre

  used.append(guess)
#Afegeix la lletra de la paraula a la llista used
  if guess in word:
    print "Si", guess, "esta en la palabra"
#Et diu que la lletra esta en la paraula 
    new = ""
    for i in range (len(word)):
      if guess == word[i]:
        new += guess
      else:
        new +=so_far[i]
    so_far = new
#Si la lletra es igual a un dels caracters que forma la paraula introduida per el jugador 1.
#afegeix la lletra a una llista anomenada new.
#Despres diu que so_far es igual a la llista new,obviament es així perquè so_far es la longitud de la paraula escollida per el jugador1.
  else:
    print "Lo siento", guess, "no esta en la palabra"
    wrong += 1
#Sino imprimeix per pantalla que la lletra introduïda no esta en la paraula escollida per el jugador1 i incrementa el contador wrong.
if wrong == MAX_WRONG:
  print "Has perdido"
  print "La palabra era", word
#si el contador es  igual al numero de imatges que hi han a la llista MAX_WRONG,has perdut i t'imprimeix la paraula que era.
else:
  print "Has ganado!"
  print "La palabra era", word
#Sino has guanyat i t'imprimeix la paraula resultant.
