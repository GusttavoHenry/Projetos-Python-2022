print("Inicio da aula 3 (09/11/2023)")

contador = 1

 #Exibir de 1 até 1000 repetidamente
while (contador<=1000):
    print(contador)
    contador = contador+1

# Laço for (python for each)   
fruta ="morango"
print(fruta)

fruta1 = "Limão"
fruta2 = "Abacaxi"
fruta3 = "pêra"

#Lista
frutas = ["jabuticaba", "laranja" , "abacate"]

#quero exibir apenas a 3ª fruta(abacate)
print(frutas[2])

#Exibir quantas frutas possuem em minha lista
print(len(frutas)) #lenght = tamanho

#Quero incluir uma fruta nova
frutas.append("manga") 
print(len(frutas))
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

i= 0
while (i<4):
    print(frutas[i])
    i= i+1

    print("Exemplo das frutas com while...")
    frutas.append("uva")

    i= 0 #(i de index)
    while (i<len(frutas)):
        print(frutas[i])
        i= i+1
    
    print("Exemplo da frutas com FOR ")
    for fruta in frutas:
     print(frutas)
