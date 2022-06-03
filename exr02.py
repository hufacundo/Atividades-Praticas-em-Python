from typing import List

def main():
    stack: List[int] = [2025, 2024, 2023, 2022, 2021, 2020]
    placa = int(input("Digite o número da placa: "))
    print(conseguir_sair(stack, placa))

def conseguir_sair(stack, placa):
    carros_para_retirar = 0
    for element in stack[::-1]:
        if element != placa:
            carros_para_retirar += 1
        elif element == placa:
            return carros_para_retirar

    return 'Não possui carro com essa placa!!!'

main()