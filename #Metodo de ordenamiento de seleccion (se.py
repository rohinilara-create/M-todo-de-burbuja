#Metodo de ordenamiento de seleccion (selectioesport)

from random import sample

lista = list(range(100))

vectotorselect = sample(lista,8)

def selectionsort(vectorselect):
    """Esta funcion ordenara el vectorr que le pase con argumento con el Metododo selection sort"""

    print ("el vector a ordenar es:",vectorselect)

    largo = 0

    for _ in vectorselect:
        largo += 1

        for i in range(largo):

            minimo = 1
            for j in range(i+1, largo):
                if vectorselect[minimo] > vectorselect[j]:
                    minimo = j
            vectorselect[i], vectorselect[minimo] = vectorselect[minimo], vectorselect[i]

        print("El vector ordenado es;",vectorselect)

selectionsort(vectotorselect)