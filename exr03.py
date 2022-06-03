def soldadoCirculo(soldado, step=2):
    if step <= 1:
        print("Digite um valor maior que 1 !")
    else:
        step -= 1
        kill = step
        while len(soldado) > 1:
            print("O Soldado",soldado.pop(kill),"não sobreviveu!")
            kill = (kill + step) % len(soldado)
        print("\nO Soldado",soldado[0], "escapou para chamar ajuda!!!")


num = int(input("Digite o número de Soldados:  "))
soldados = [i for i in range(1, num + 1)]
soldadoCirculo(soldados)