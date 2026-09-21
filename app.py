"""
Campanha de conscientização ambiental - Companhia de Saneamento
Classifica o perfil de consumo de água dos imóveis e emite alertas educativos.
"""

LIMITE_ECONOMICO = 10.0   # m3
LIMITE_RESIDENCIAL = 25.0  # m3


def ler_tipo_imovel():
    """Lê e valida o tipo do imóvel."""
    validos = ("comercial", "casa", "apartamento")
    while True:
        tipo = input("Tipo do imóvel (comercial / casa / apartamento): ").strip().lower()
        if tipo in validos:
            return tipo
        print("Opção inválida. Digite: comercial, casa ou apartamento.")


def ler_consumo():
    """Lê e valida o consumo mensal em metros cúbicos."""
    while True:
        try:
            consumo = float(input("Consumo mensal de água (m3): ").replace(",", "."))
        except ValueError:
            print("Valor inválido. Informe um número decimal, ex.: 12.5")
            continue
        if consumo < 0:
            print("O consumo não pode ser negativo.")
            continue
        return consumo


def classificar(tipo, consumo):
    """Aplica as regras de negócio e devolve a mensagem correspondente."""
    if tipo == "comercial":
        return "Tarifa comercial aplicada - consulte o plano corporativo."

    if tipo == "apartamento" and consumo < LIMITE_ECONOMICO:
        return "Consumo econômico - excelente controle de água!"

    if tipo in ("apartamento", "casa") and consumo <= LIMITE_RESIDENCIAL:
        return "Consumo moderado - dentro do padrão residencial."

    return "Consumo excessivo - adote medidas de economia e verifique vazamentos."


def main():
    print("=== Classificação de Consumo de Água ===")
    tipo = ler_tipo_imovel()
    consumo = ler_consumo()

    print("\n--- Resultado ---")
    print(f"Imóvel: {tipo.capitalize()}")
    print(f"Consumo: {consumo:.2f} m3")
    print(classificar(tipo, consumo))


if __name__ == "__main__":
    main()