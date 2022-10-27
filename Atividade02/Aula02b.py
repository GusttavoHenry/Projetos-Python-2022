#pedindo nome do aluno e sua nota ( de 0 a 10), e se ele tirou nota 10, mostra "{nome} você é o cara"
nome = input("Informe seu nome:")
nota = float( input("Digite sua nota:"))

if (nota==10):
    print(f"{nome}, você é o cara!")
elif( nota >=6 and nota <10):
 print(f"{nome}bom trabalho, mas precisa estudar mais")
else: # é sempre automaticamente o que as duas condições não tratamento
    print(f"{nome}Infelizmente, você não tirou 10, burro")