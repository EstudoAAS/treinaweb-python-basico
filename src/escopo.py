def teste():
    global mensagem
    mensagem = "Agora estou dentro da função"
    print(id(mensagem))
    print(mensagem)
    def funcao_Aninhada():
        nonlocal x
        x = "Estou dentro da função interna"
        print(id(x))
    x = "Estou fora da função interna"
    funcao_Aninhada()
    print(x)
    print(id(x))


mensagem = "Agora estou fora da função"
print(id(mensagem))
print(mensagem)
teste()
print(mensagem)