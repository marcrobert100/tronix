#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tronix System - Sistema de SaudaÃ§Ã£o para Pizzaria
"""

# DicionÃ¡rio com 5 sabores de pizza e seus preÃ§os
cardapio = {
    1: {"nome": "Calabresa", "preco": 29.90},
    2: {"nome": "Mussarela", "preco": 27.90},
    3: {"nome": "Portuguesa", "preco": 31.90},
    4: {"nome": "Frango com Catupiry", "preco": 33.90},
    5: {"nome": "Quatro Queijos", "preco": 35.90}
}

def saudacao():
    """Exibe uma mensagem de saudaÃ§Ã£o da pizzaria."""
    print("ðŸ• Bem-vindo Ã  Tronix Pizzaria! ðŸ•")
    print("O melhor sabor da cidade, feito com amor e tecnologia.")
    print("Como podemos ajudar vocÃª hoje?")

def exibir_menu():
    """Exibe o cardÃ¡pio de forma organizada."""
    print("\n--- ðŸ“‹ CardÃ¡pio Tronix ---")
    for numero, info in cardapio.items():
        print(f"{numero}. {info['nome']} - R$ {info['preco']:.2f}")
    print("------------------------\n")

def escolher_pizza():
    """Permite ao usuÃ¡rio escolher uma pizza pelo nÃºmero."""
    exibir_menu()
    try:
        escolha = int(input("Digite o nÃºmero da pizza desejada: "))
        if escolha in cardapio:
            pizza_escolhida = cardapio[escolha]
            print(f"\nâœ… VocÃª escolheu: {pizza_escolhida['nome']}")
            print(f"ðŸ’° PreÃ§o: R$ {pizza_escolhida['preco']:.2f}")
        else:
            print("âŒ OpÃ§Ã£o invÃ¡lida! Por favor, escolha um nÃºmero de 1 a 5.")
    except ValueError:
        print("âŒ Entrada invÃ¡lida! Digite apenas nÃºmeros.")

if __name__ == "__main__":
    saudacao()
    escolher_pizza()
#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
 
def saudacao(): 
    print("?? Bem-vindo … Tronix Pizzaria! ??") 
 
if __name__ == "__main__": 
    saudacao() 
