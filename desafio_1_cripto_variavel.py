#Letras para criptografia
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#chave screta
chave = int(input("Insira uma chave: "))

letra = input("Por favor, entre com uma letra para criptografar: ")

#encontre a posição da letra em alfabeto
posicao = alfabeto.find(letra)

#some a chave secreta para encontrar a letra criptografada
# '%26' volta para o 0 ao chegar em 26
novaPosicao = (posicao + chave) % 26

#a letra criptog. está no alfabeto na nova posição
letraCripto = alfabeto[novaPosicao]

print("Sua letra criptografada é" ,letraCripto)

#chave screta
chave = int(input("Insira uma chave: "))

letra = input("Por favor, entre com uma letra para decriptografar: ")

#encontre a posição da letra em alfabeto
posicao = alfabeto.find(letra)

#some a chave secreta para encontrar a letra criptografada
# '%26' volta para o 0 ao chegar em 26
novaPosicao = (posicao + chave) % 26

#a letra criptog. está no alfabeto na nova posição
letraCripto = alfabeto[novaPosicao]

print("Sua letra decriptografada é" ,letraCripto)
