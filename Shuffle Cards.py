## se baraja el mazo de cartas
## El mazo tiene 13 cartas cada uno de 4 palos llamesen corazones, picas, diamantes, tréboles.
## Se construye el maso de cartas desarmado constituido de dos listas una por cada palo de cartas 
## y otra para cada valor de las cartas
## Se baraja el mazo de cartas repitiendo cada carta utilizando sus respectivos indicadores 
## y se intercambian los exponentes con otros exponentes aleatorios
import random
 
suits = ["♠", "♥", "♦", "♣"]
cardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
 
## se iniacializa el mazo de cartas vacío
deck = []
 
## Aquí construimos un mazo de cartas con los respectivos palos de las cartas y sus valores
for suit in suits:
    for value in cardValues:
        deck.append(value + suit)
## se imprime el mazo de cartas desordenado
print("El Mazo Original de Cartas :\n\n", deck)
 
 
## Se repiten todas las cartas una por una utilizando sus respectivos exponentes, 
## mezclando los índices con otros índices aleatorios.
for index in range(0, len(deck)):
    randomCardForSwitching = random.randrange(len(deck))   
    ## Se intercambian los índices
    temporaryIndex = deck[index]
    deck[index] = deck[randomCardForSwitching]
    deck[randomCardForSwitching] = temporaryIndex
## se imprime la baraja de las cartas
print("\nEl Mazo de Cartas barajado:\n\n", deck)



