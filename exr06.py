
lista = [20, 21, 22, 23, 24, 25]
print("Inicio da lista: ", lista)


numero = int(input("Coloque um número para verificar se está na lista: "))

if numero in lista:
    print("Número {} existe na lista!".format(numero))
else:
    print("Número {} não existe na lista!".format(numero))


add = int(input("Adicione um número a lista: "))
lista.append(add)
print("Número {} adicionado com sucesso a lista: ".format(add), lista)


rmv = int(input("Coloque um número para ser removido da lista: "))
lista.remove(rmv)
print("Número {} removido com sucesso da lista: ".format(add), lista)