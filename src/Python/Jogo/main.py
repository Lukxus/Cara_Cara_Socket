def play(value):
    my_turn = value

    if my_turn == 1: #ask a question
        ask()
    else:
        answer()


def ask():
    print("Deseja perguntar sobre o que?")
    print("[1] - Cor do cabelo\n[2] - Corte do cabelo\n[3] - Barba\n[4] - Óculos")
    escolha1 = int(input("Deseja perguntar sobre o que? -> "))
    escolha2 = 0
    match escolha1:
        case 1:
            print("[1] - Cabelo Preto\n[2] - cabelo Marrom\n[3] - Cabelo Cinza")
            escolha2 = int(input("Escolha uma cor -> "))
        case 2:
            print("[1] - Calvo\n[2] - Raspado\n[3] - Liso\n[4]-Baixo")
            escolha2 = int(input("Escolha um corte -> "))
        case 3:
            print("[1] - True\n[2] - False")
            escolha2 = int(input("Escolha uma condição -> "))
        case 4:
            print("[1] - True\n[2] - False")
            escolha2 = int(input("Escolha uma condição -> "))
    return((escolha1, escolha2))

def answer(tupla, cara): #tupla[0] - contexto ; tupla[1] - valor
    if tupla[1] == 



play()