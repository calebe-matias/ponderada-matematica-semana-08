def main():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    operacao = input(
        "Digite a operacao (SOMA, SUBTRACAO, MULTIPLICACAO ou DIVISAO): "
    ).strip().upper()

    if operacao == "SOMA":
        resultado = numero1 + numero2
    elif operacao == "SUBTRACAO":
        resultado = numero1 - numero2
    elif operacao == "MULTIPLICACAO":
        resultado = numero1 * numero2
    elif operacao == "DIVISAO":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Nao e possivel dividir por zero.")
            return
    else:
        print("Operacao invalida.")
        return

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
