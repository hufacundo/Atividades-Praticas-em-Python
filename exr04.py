class FilaPrioridade(object):

    def __init__(self):
        self.queue = []


    def vazia(self):
        return len(self.queue) == 0


    def enfileirar(self, elemento):
        self.queue.append(elemento)


    def desenfileirar(self):
        try:
            max_valor = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_valor]:
                    max_valor = i

            elemento = self.queue[max_valor]
            del self.queue[max_valor]
            return elemento
        except IndexError:
            print("Erro")


def main():

    fila = FilaPrioridade()


    fila.enfileirar(1)
    fila.enfileirar(4)
    fila.enfileirar(11)
    fila.enfileirar(7)


    while not fila.vazia():
        print("Componente desenfileirado: ", fila.desenfileirar())


if __name__ == "__main__":
    main()