cardfaces = []
suits = ["♠", "♥", "♦", "♣"]
royals = ["J", "Q", "K", "A"]
deck = []

## se utiliza método append al final de la lista para agregar nuevos objetos. 

## en este arreglo lo que hace es unir los números del 2 al 11
for i in range(2,11):
    cardfaces.append(str(i))

## este arreglo lo que hace es recorrer los royals y es definido por range(rango) de 4
for j in range(4):
    cardfaces.append(royals[j])


#este arreglo lo que hace es unir los números con los suits y también con sus respectivos royals
for k in range(4):
    for l in range(13):
        card = (cardfaces[l] + suits[k])
        deck.append(card)


for m in range(52):
    print(deck[m])
pick=input('Toma una carta 1-52 :')