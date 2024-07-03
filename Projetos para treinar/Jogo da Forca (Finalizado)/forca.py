# Jogo da Forca
import os
ganhou = False

def troca_letra(letra_tentativa):
    index = 0
    posicao_letras_tentativa = []
    resultado = -2

    while resultado != -1:
        
        if resultado != -2:
            posicao_letras_tentativa.append(resultado)

        # print(posic_letras_tentativa)

        resultado = resposta.find(tentativa, index)

        index = resultado + 1
        
        texto_aux = ""

        for posicao_letra_resposta in range(0, len(resposta)): # começa em zero e vai até o tamanho da palavra -1

            if posicao_letra_resposta in posicao_letras_tentativa:
                texto_aux += tentativa

            else: # X
                texto_aux += resp_vazia[posicao_letra_resposta]
    return texto_aux 
    

def limpa_tela(mensagem=""):
    # os.system('cls')
    print(mensagem)
    print(resp_vazia)

# Entrada da Palavra ou Resposta
resposta = input("Digite a palavra do jogo: ")
resp_vazia = ""

for letra in resposta:
    resp_vazia += "_"

max_letras = len(resposta)
# for num_posic in range(0, len(resposta)):
    # print(numero)

print(f"A palavra possui {len(resposta)} letras!")
palavra_exibida = resp_vazia
os.system('cls')

# Roda a repetição do Jogo
while(ganhou == False):
    # print(resp_vazia)
    # print("")    
    # Entrada das letras ou Palavra

    tentativa = input("Digite uma letra ou a palavra: ")
    if tentativa == "2":
        ganhou = True

    if len(tentativa) == 1 : # Digitou uma letra
        if tentativa in resposta: # Digitou uma Letra e essa letra está na palavra!
            # print("A palavra possui essa letra!")
            if tentativa in resp_vazia:
                print("Está Letra já está na palavra!")

            else:
                resp_vazia = troca_letra(tentativa)
                limpa_tela("A palavra possui essa letra!")
        else:
            limpa_tela("A palavra não possui essa letra!")
            # print("A palavra não possui essa letra!")

    elif len(tentativa) == len(resposta): # Digitou uma palavra
        if tentativa.lower() == resposta.lower(): # Verifica se é a resposta
            print("Parabéns!!! Você acertou")
            ganhou = False
        else:
            limpa_tela()
            print("Opss não é essa resposta")
    else:
        limpa_tela()
        print("A palavra não possui essa quantidade de letras!")

    if resp_vazia == resposta:
        print("Parabéns você ganhou!!")
        ganhou = True
        



