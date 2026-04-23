#Metodo de Ordenamientode la Burbuja asendente(BubbleSort)
from random import sample
lista = list(range(100))
vectorbs = sample(lista,8)
def bubblesort(vectorbs):
    #"""Esta funcion ordenara el vector que le pases como argumento con el metodo de bubble sort"""

    print("El vector a ordenar  es:",vectorbs)
    n = 0

    for _ in vectorbs:
        n += 1

    for i in range(n-1):

        for j in range(0, n-i-1):
                
            if vectorbs[j] > vectorbs[j+1] :
                vectorbs[j], vectorbs[j+1] = vectorbs[j+1], vectorbs[j]

    print ("el vector vector ordenamiento es: ",vectorbs)

bubblesort(vectorbs)                   