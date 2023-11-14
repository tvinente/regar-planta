#Por último o robô deve regar os vasos na ordem decrescente, seguindo a organização original:

#0 - Tomate / 1 - Batata / 2 - Cenoura / 3 - Tomate / 4 - Batata / 5 - Cenoura

for i in range(5, -1, -1):
    planta_atual = str(i)
    print("Regar a planta " + planta_atual)

