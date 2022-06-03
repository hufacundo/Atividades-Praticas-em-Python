class Aviao:

    def __init__(self, num_voo, companhia, destino):
        self.num_voo = num_voo
        self.companhia = companhia
        self.destino = destino

class Fila:

    def __init__(self):
        self.elementos = []


    def vazia(self):
        return self.elementos == []


    def enfileirar(self, elemento):
        self.elementos.insert(0, elemento)


    def desenfileira(self):
        return self.elementos.pop()


    def tamanho(self):
        return len(self.elementos)


    def listar_elementos(self):
        for i in range(self.tamanho() - 1, -1, -1):
            print("Número do Voo: {0}".format(self.elementos[i].num_voo))
            print("Companhia: {0}".format(self.elementos[i].companhia))
            print("Destino: {0}".format(self.elementos[i].destino))
            print("----------------------------------")


    def retornar_frente(self):
        if self.vazia():
            return None
        else:
            return self.elementos[self.tamanho() - 1]


def main():

    fila = Fila()


    while (True):
        print("\n---------- CONTROLE DE DECOLAGENS ----------\n")
        print("1. Listar o número de aviões aguardando na fila de decolagem")
        print("2. Autorizar a decolagem do primeiro avião da fila")
        print("3. Adicionar um avião à fila de espera")
        print("4. Listar todos os aviões na fila de espera")
        print("5. Listar as características do primeiro avião da fila")
        print("6. Sair")

        opcao = int(input("Sua opção: "))

        if (opcao == 1):
            print("\nNeste momento há {0} aviões na fila de espera.".format(fila.tamanho()))

        elif (opcao == 2):
            if not fila.vazia():
                aviao = fila.desenfileira()
                print("\nDecolagem autorizada do voo n. {0}".format(aviao.num_voo))
            else:
                print("\nFila de decolagem está vazia.")

        elif (opcao == 3):
            voo = input("\nNúmero do Voo: ")
            companhia = input("Nome da Companhia: ")
            destino = input("Destino: ")


            aviao = Aviao(voo, companhia, destino)
            fila.enfileirar(aviao)

            print("\nO avião foi colocado na fila com sucesso.")

        elif (opcao == 4):
            if fila.vazia():
                print("\nA fila está vazia")
            else:
                print("\nAVIÕES NA FILA DE ESPERA:\n")
                print("----------------------------------")
                fila.listar_elementos()

        elif (opcao == 5):
            aviao = fila.retornar_frente()
            if aviao != None:
                print("\n-------- PRIMEIRO AVIÃO NA FILA ----------")
                print("Número do Voo: {0}".format(aviao.num_voo))
                print("Companhia: {0}".format(aviao.companhia))
                print("Destino: {0}".format(aviao.destino))
            else:
                print("\nA fila está vazia")

        elif (opcao == 6):
            break


if __name__ == "__main__":
    main()