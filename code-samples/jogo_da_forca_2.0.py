import requests
import random
from unidecode import unidecode

url = "https://www.ime.usp.br/~pf/dicios/br-utf8.txt"

response = requests.get(url)

if response.status_code == 200:
    lista_de_palavras = response.text.split("\n")
else:
    print("Falha ao obter a lista de palavras.")

while True:
    tamanho_maximo = 0
    tamanho_minimo = 0
    while tamanho_maximo < 3 and tamanho_minimo < 3:
        tamanho_minimo = int(input("Entre com o tamanho mínimo da palavra secreta: "))
        tamanho_maximo = int(input("Entre com o tamanho máximo da palavra secreta: "))

    palavra_secreta = random.choice(lista_de_palavras)

    if tamanho_minimo < len(palavra_secreta) > tamanho_maximo:
        palavra_secreta = random.choice(lista_de_palavras)
        
        
    palavra_secreta = unidecode(palavra_secreta)
        
    letras_acertadas = ["_" for _ in palavra_secreta]

    header = """'******************************************'
    '*** Bem-vindo ao jogo da Forca 2.0! ***'\n'******************************************'
    """

    print(header)

    enforcado = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcado and not acertou:
        
        tentativa = input("Qual letra? ").lower()
        
        while not tentativa.isalpha() or len(tentativa) > 1:
            print("Digite apenas uma letra!")
            tentativa = input("Qual letra? ").lower()
        
        if tentativa in palavra_secreta:
            posicao = 0
            
            for letra in palavra_secreta:
                if tentativa == letra:
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1
            if erros == 6:
                enforcado = True
            
        print(letras_acertadas)
        
        if "_" not in letras_acertadas:
            acertou = True
            
    if acertou:
        print("Você ganhou!")
    else:
        print(f"Você perdeu! A palavra era {palavra_secreta.upper()}")       

    
    opcao = input("Deseja continuar? S/N: ").lower()
    
    while opcao != "s" and opcao != "n":
        print("Digite apenas S ou N.")
        opcao = input("Deseja continuar? S/N: ").lower()
    
    if opcao == "n":
        input("Pressione Enter para sair")
        break
