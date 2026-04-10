# 🛡️ Criptografia OTP com XOR (Projeto APS)

Este projeto foi desenvolvido como parte de um trabalho acadêmico (APS). Ele consiste em um programa em Python que realiza a **criptografia** e **descriptografia** de mensagens (até 128 caracteres) utilizando a operação lógica **XOR** e conversão para **Hexadecimal**.

## 🧠 Como funciona a lógica?
O programa utiliza o conceito de **One-Time Pad (OTP)**, que é um dos métodos de criptografia mais seguros que existem. A lógica funciona assim:
1. Uma **chave aleatória** é gerada com o mesmo tamanho da mensagem.
2. É feita uma operação **XOR** bit a bit entre a mensagem e a chave.
3. O resultado (a cifra) é exibido em **Hexadecimal** para facilitar a leitura e o transporte.



## 🛠️ Tecnologias
* **Linguagem:** Python 3
* **Bibliotecas:** `os` (geração de chave), `binascii` (conversão hex) e `sys`.

## 🚀 Como usar
1. Execute o arquivo `main.py`:
   ```bash
   python main.py

2. Escolha a opção 1 para criptografar. Digite sua mensagem e guarde a Chave e a Cifra geradas.

3. Para ler a mensagem de volta, escolha a opção 2 e cole a Chave e a Cifra nos campos indicados.

     
