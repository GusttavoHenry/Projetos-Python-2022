#criação de funções

preco = 1999.98

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela 

imposto= preco * 0.05
print(imposto)

preco2= 100
imposto2= preco2 * 0.05
print(imposto2)

#Criar uma função calcular imposto() que calcula um imposto de 5% e retonar o que foi pedido
def calcular_imposto(preco_produto):
    imposto = preco_produto * 0.05
    return imposto

# Aqui é o uso.... aqui é imposto a calcular e .. exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função (7%)") 

#Variavel local x global
print(preco)
preco_produto = 100
print(preco_produto)

#agora calcular imposto a aliquota agora é 7%

valores =[1.99, 24.50, 78.27, 1515.5]

#se eu quiser calcular o imposto destes valores ... e exibir na tela assim: "o imposto de ... é ... " (io. preço, 2a. imposto)

for valor in valores:
    print(f"o imposto de {valor} é {calcular_imposto(valor)}")


#Delcarar uma fução calcular_imposto_aliquota que recebe dois parâmetros: o preço do produto e a aliquota de imposto a ser aplicada e retorna o imposto calculado. se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota=7):
    imposto = valor * aliquota /100
    return imposto
    
    for valor in valores:
        print(f"o imposto de{valor} é {calcular_imposto_aliquota(valor, 7)}")


        #E se for 10%?
        for valor in valores:
             print(f"o imposto de{valor} é {calcular_imposto_aliquota(valor, 10)}")