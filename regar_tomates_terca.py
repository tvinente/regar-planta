#É terça-feira e os tomates precisam ser regados. A ordem dos vasos mudaram:

#0 - Tomate / 1 - Tomate / 2 - Batata / 3 - Batata / 4 - Tomate / 5 - Tomate

for i in range(0, 6):
  if i not in[2, 3]:
    planta_atual = str(i)
    print("Regar a planta " + planta_atual)