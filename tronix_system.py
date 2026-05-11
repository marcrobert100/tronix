#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tronix System - Sistema de Saudação para Pizzaria
"""

# Dicionário com 5 sabores de pizza e seus preços
cardapio = {
    1: {"nome": "Calabresa", "preco": 29.90},
    2: {"nome": "Mussarela", "preco": 27.90},
    3: {"nome": "Portuguesa", "preco": 31.90},
    4: {"nome": "Frango com Catupiry", "preco": 33.90},
    5: {"nome": "Quatro Queijos", "preco": 35.90}
}

def saudacao():
    """Exibe uma mensagem de saudação da pizzaria."""
    print("🍕 Bem-vindo à Tronix Pizzaria! 🍕")
    print("O melhor sabor da cidade, feito com amor e tecnologia.")
    print("Como podemos ajudar você hoje?")

def exibir_menu():
    """Exibe o cardápio de forma organizada."""
    print("\n--- 📋 Cardápio Tronix ---")
    for numero, info in cardapio.items():
        print(f"{numero}. {info['nome']} - R$ {info['preco']:.2f}")
    print("------------------------\n")

def escolher_pizza():
    """Permite ao usuário escolher uma pizza pelo número."""
    exibir_menu()
    try:
        escolha = int(input("Digite o número da pizza desejada: "))
        if escolha in cardapio:
            pizza_escolhida = cardapio[escolha]
            print(f"\n✅ Você escolheu: {pizza_escolhida['nome']}")
            print(f"💰 Preço: R$ {pizza_escolhida['preco']:.2f}")
        else:
            print("❌ Opção inválida! Por favor, escolha um número de 1 a 5.")
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números.")

if __name__ == "__main__":
    saudacao()
    escolher_pizza()
