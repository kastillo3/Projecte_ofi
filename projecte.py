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


MAX_WRONG = len(images)
print "Bienvenido al ahorcado. Buena suerte :)"
WORDS = input("Escriba una palabra: ")
LIST_WORDS=[]
LIST_WORDS+=[WORDS]
word = random.choice(LIST_WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

while wrong < MAX_WRONG and so_far != word:
  s.set_pixels(images[wrong % len(images)]())
  print "Has usado las siguientes letras", used
  print "De momento, la palabra es: ", so_far
  guess = input("Introduzca una letra: ")

  while guess in used:
    print "Ya habia introducido esta letra", guess
    guess = input("Introduzca una letra")

  used.append(guess)
  
  if guess in word:
    print "Si", guess, "esta en la palabra"
    new = ""
    for i in range (len(word)):
      if guess == word[i]:
        new += guess
      else:
        new +=so_far[i]
    so_far = new
  else:
    print "Lo siento", guess, "no esta en la palabra"
    wrong += 1
if wrong == MAX_WRONG:
  print "Has perdido"
  print "La palabra era", word
else:
  print "Has ganado!"
  print "La palabra era", word
  
