# 🍔 Sistema de Pedidos - Lanchonete

## 📌 Descrição

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de simular um sistema simples de pedidos de uma lanchonete utilizando a linguagem Python.

O sistema permite ao usuário selecionar produtos, informar quantidades e visualizar o valor total do pedido, além de exibir um resumo completo ao final da execução.

---

## 🎯 Objetivos

* Praticar lógica de programação
* Utilizar estruturas condicionais (`if`, `elif`, `else`)
* Trabalhar com estruturas de repetição (`while`)
* Utilizar listas e dicionários
* Desenvolver interação com o usuário via terminal

---

## ⚙️ Funcionalidades

* Exibição de menu de produtos
* Seleção de itens pelo usuário
* Validação de opção inválida
* Entrada de quantidade de produtos
* Cálculo automático do valor por item
* Acúmulo do valor total do pedido
* Repetição do sistema até o usuário encerrar
* Exibição final com:

  * Lista de itens
  * Quantidade de cada produto
  * Valor por item
  * Total geral do pedido

---

## 🧠 Lógica do Programa

O sistema utiliza um loop `while` para manter o programa em execução até que o usuário escolha sair.

As decisões são controladas por estruturas condicionais (`if/elif/else`), permitindo validar a opção escolhida.

Os pedidos são armazenados em uma lista contendo dicionários, onde cada item guarda:

* Nome do produto
* Quantidade
* Valor total

O valor total do pedido é acumulado em uma variável separada.

---

## 💻 Tecnologias Utilizadas

* Python 3

---

## ▶️ Como Executar

1. Instale o Python 3 na sua máquina
2. Clone este repositório:

   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
3. Acesse a pasta do projeto:

   ```
   cd nome-do-projeto
   ```
4. Execute o arquivo:

   ```
   python nome_do_arquivo.py
   ```

---

## 📷 Exemplo de Saída

```
Escolha uma das opções de produto:
1 - Hambúrguer
2 - Pizza
3 - Refrigerante
0 - Sair do sistema

Você escolheu Hambúrguer - qtd: 2 Valor total: R$ 40.00

Seu pedido foi encerrado com sucesso!

Os itens do seu pedido são:
Hambúrguer - qtd: 2 Valor total: R$ 40.00
Pizza - qtd: 1 Valor total: R$ 15.00
Refrigerante - qtd: 3 Valor total: R$ 15.00

Valor total: R$ 70.00
```

---

## 👩‍💻 Autora

Gabrielli Cabral

---

## 📚 Observações

Este projeto foi desenvolvido para fins educacionais, com foco na prática de lógica de programação e fundamentos da linguagem Python.
