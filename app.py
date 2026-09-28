def calcular_consumo():
    print("=" * 45)
    print("  CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE")
    print("=" * 45)
    
    # Coleta de dados
    nome_aparelho = input("\nDigite o nome do aparelho (ex.: Geladeira): ").strip()
    
    while True:
        try:
            potencia = float(input("Digite a potência do aparelho em Watts (W): "))
            if potencia <= 0:
                print("A potência deve ser um número maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    while True:
        try:
            horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))
            if horas_dia < 0 or horas_dia > 24:
                print("As horas diárias devem estar entre 0 e 24. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    # Processamento / Cálculo
    consumo_mensal = (potencia * horas_dia * 30) / 1000

    # Exibição dos resultados
    print("\n" + "-" * 35)
    print("      RESULTADO DO CÁLCULO")
    print("-" * 35)
    print(f"Aparelho: {nome_aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print("-" * 35)

if __name__ == "__main__":
    calcular_consumo()
