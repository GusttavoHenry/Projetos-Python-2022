# Comando input(): quero permitir o usuario digitar algo
nome = input("Digite o seu nome: ")
print(nome)

#Comando de saida..exibir na tela
print(f"boa noite! meu nome é: {nome}")

#exibir minha idade
idade = int (input("digite sua idade:"))
print(f"minha idade é: {idade}")

#exibir o dobro da idade informada
dobro = idade *2
print(f"o dobro da idade informada é: {dobro}")

#Estrutura condicionalo famoso“se”(if)
#Se a pessoa for maior de idade, Bom mostre“você é maior de idade,ótimo!Já pode beber ou dirigir”
if idade >= 18: 
    print("Você é maior de idade, otimo! você ja pode tomar umas ou dirigir")
else:
    print("Você é menor de idade, portanto não pode consumir bebiadas alcoolicas ou dirigir")

# E se eu quisessem perguntar o genero (M= masculino e F= feminino)    
# mostre (...e voce tambem precisa/precisou prestar o serviço militar pbrogatorio)
genero = input(f"informe seu genero: M=masculino, F=Feminino, O=Outros")

if idade >= 18 and genero == "M":
 print("então você precisa/ prestou o serviço militar obrigatorio")
if idade >= 18 and genero == "F":
     print("então você precisa/ prestou o serviço militar obrigatorio")
if idade >= 18 and genero == "O:":
    print("então você precisa/ prestou o serviço militar obrigatorio")
else:
    print("então você ainda não possui idade sufciente para prestar o serviço militar obrigatorio")    
  






