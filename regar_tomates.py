#Nesse cenário só existem Batatas e tomates. As batatas já foram regadas, restam os tomates. Deve-se imprimir mensagem para o robô regá-las.

#0 - Tomate / 1 - Batata / 2 - Tomate / 3 - Batata / 4 - Tomate / 5 - Batata

for i in range(6):
  planta_atual = str(i)
  if(i % 2 == 0):
    print("regue o tomate " + planta_atual)