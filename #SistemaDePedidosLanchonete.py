#====================================================
#           Sistema de pedidos Lanchonete           |
#====================================================

#Gabrielli Cabral de Sousa - BS - Noite 

# Atribuindo os preços aos produtos
hamburguer = 10.00
pizza = 25.00
refrigerante = 11.00

# Lista que vai armazenar todos os pedidos feitos (parte do desafio extra)
# Essa lista vai guardar vários itens (pedidos), cada um com suas informações
pedidos = []

# Variável que armazena o total geral do pedido (inicia em 0 e vai acumulando os valores)
total_geral = 0

# Loop principal (fica repetindo até o usuário decidir sair do sistema)
while True:

    # Exibe o menu de opções para o usuário escolher um produto
    print("\nEscolha uma das opções de produto:")
    print("1 - Hambúrguer")
    print("2 - Pizza")
    print("3 - Refrigerante")
    print("0 - Sair do sistema")

    # Recebe a opção do usuário e converte o valor digitado para inteiro (int)
    opcao = int(input("Digite a opção: "))

    # Condicionais IF, ELIF e ELSE (usadas para tomar decisões no programa)

    # Se escolher 0, encerra o sistema
    if opcao == 0:
        print("\nSeu pedido foi encerrado com sucesso!")
        break  # encerra o loop e finaliza o programa

    # Verifica qual produto foi escolhido
    # A variável 'produto' guarda o nome do item (tipo string/texto)
    # A variável 'preco' recebe o valor correspondente ao produto escolhido
    elif opcao == 1:
        produto = "Hambúrguer"
        preco = hamburguer

    elif opcao == 2:
        produto = "Pizza"
        preco = pizza

    elif opcao == 3:
        produto = "Refrigerante"
        preco = refrigerante

    # Caso o usuário digite uma opção inválida (diferente de 0, 1, 2 ou 3)
    else:
        print("Opção inválida! Tente novamente.")
        continue  # volta para o início do loop sem continuar o restante do código

    # Pergunta ao usuário a quantidade desejada do produto escolhido
    quantidade = int(input(f"Você escolheu {produto}. Qual a quantidade desejada? "))

    # Calcula o valor total daquele item (preço multiplicado pela quantidade)
    total_item = preco * quantidade

    # Soma o valor do item ao total geral do pedido
    total_geral += total_item

    # Armazena o pedido na lista usando um dicionário
    # Cada item terá: nome do produto, quantidade e valor total daquele item
    pedidos.append({
        "produto": produto,
        "quantidade": quantidade,
        "total": total_item
    })

    # Mensagem de confirmação para o usuário
    print(f"{produto} adicionado ao pedido!\n")


# EXIBIÇÃO FINAL DO PEDIDO

print("\nOs itens do seu pedido são:")

# Percorre a lista de pedidos (usando um laço for)
# Cada "item" representa um pedido feito anteriormente
for item in pedidos:
    print(f"{item['produto']} - qtd: {item['quantidade']} Valor total: R$ {item['total']:.2f}")

# Mostra o valor total final de todos os itens somados
print(f"\nValor total: R$ {total_geral:.2f}")