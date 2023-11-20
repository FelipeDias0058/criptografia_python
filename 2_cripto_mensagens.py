#Letras para criptografia
alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave = int(input("Insira uma chave: "))

mensagem = input("Por favor, entre com uma mensagem para decriptografar: ")
msgCripto = ""

for char in mensagem:
    if char in alfabeto:
        posicao = alfabeto.find(letra)
        novaPosicao = (posicao + chave) % 26
        msgCripto = msgCripto + alfabeto[novaPosicao]
    else:
        msgCripto = msgCripto + char

print("Sua mensagem decriptografada é" ,msgCripto)
