import os       # os é usado para gerar números aleatórios(usado para criar a chave na parte de criptografia)
import binascii # binascii usado para converter bytes em hexadecimal e vice-versa
import sys      # sys usado só para encerrar o programa

def xor_bytes(a,b): # função que faz a operação XOR entre dois conjuntos de bytes(xor é a base do one time pad)
    return bytes(x ^ y for x, y in zip(a, b))

def para_hexadecimal(b): # converte bytes para texto hexadecimal
    return binascii.hexlify(b).decode()

def de_hexadecimal(h): # converte texto hexadecimal para bytes de volta
    return binascii.unhexlify(h)

def main(): # função principal do programa
    while True: 
        print("\n1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            mensagem = input("Digite a mensagem (máx 128 caracteres): ")
            if len(mensagem) > 128:
                print("Erro: mensagem muito longa(máx 128).")
                continue

            chave = os.urandom(len(mensagem.encode("utf-8"))) # gera uma chave aleatoria do mesmo tamanho da mensagem
            print("Chave gerada (HEX):", para_hexadecimal(chave))

            cifra = xor_bytes(mensagem.encode("utf-8"), chave) # criptografa a mensagem com xor entre mensagem e chave
            print("Cifra (HEX): ", para_hexadecimal(cifra))

        elif opcao == "2":
            chave_hex = input("Cole a chave em HEX: ")
            cifra_hex = input("Cole a cifra em HEX: ")

            try: 
                cifra = de_hexadecimal(cifra_hex) # converte hex devolta pra bytes
                chave = de_hexadecimal(chave_hex)
            except ValueError:
                print("Erro: valor HEX inválido.")
                continue

            if len(chave) != len(cifra): # compara se a chave e cifra tem o mesmo tamanho
                print("Erro: chave e cifra devem ter o mesmo tamanho.")
                continue

            mensagem = xor_bytes(cifra, chave) # descriptografa usando xor denovo
            try: 
                print("Mensagem descriptografada:", mensagem.decode("utf-8")) # tenta mostrar a mensagem original do texto
            except ValueError:
                print("Mensagem descriptogradada (bytes):", mensagem)# caso não consiga decodificar
        
        elif opcao == "3":
            print("Saindo do programa.")
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente!")


if __name__ == ("__main__"):
    main()