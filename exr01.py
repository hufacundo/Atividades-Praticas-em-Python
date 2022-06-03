from typing import List

def main():
    stack: List[int] = [21, 22, 23, 24, 25]
    imprimir_numeros_reais(stack)

def imprimir_numeros_reais(stack):
    for element in stack[::-1]:
        if element > 0:
            print(element)

main()