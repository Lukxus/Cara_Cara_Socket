import Front.pygamevisual

def play(value):
    my_turn = value
    if my_turn == 1: #ask a question
        ask()
    else:
        answer()


def ask(caras):
    print("Deseja perguntar sobre o que?")
    print("[1] - Cor do cabelo\n[2] - Corte do cabelo\n[3] - Barba\n[4] - Óculos\n[5] - Fazer palpite")
    escolha1 = int(input("Deseja perguntar sobre o que? -> "))
    escolha2 = 0
    match escolha1:
        case 1:
            print("[1] - Cabelo Preto\n[2] - cabelo Marrom\n[3] - Cabelo Cinza")
            escolha2 = int(input("Escolha uma cor -> "))
        case 2:
            print("[1] - Calvo\n[2] - Raspado\n[3] - Liso\n[4] - Baixo")
            escolha2 = int(input("Escolha um corte -> "))
        case 3:
            print("[1] - Verdadeiro\n[2] - Falso")
            escolha2 = int(input("Escolha uma condição -> "))
        case 4:
            print("[1] - Verdadeiro\n[2] - Falso")
            escolha2 = int(input("Escolha uma condição -> "))
        case 5:
            #print("- Luba\n- Kishimoto\n- Orlando\n- Gustavo\n- Jamilson\n- Leonardo")
            escolha2 = (Front.pygamevisual.escolhaCaras(caras, "Escolha a cara do seu adversario")).getNome()
    return((escolha1, escolha2))

def answer(dados, cara): #dados[0] - contexto ; dados[1] - valor
    match dados[0]:
        case 1:
            return dados[1] == cara.getCorCabelo()
        case 2:
            return dados[1] == cara.getTipoCorteCabelo()
        case 3:
            return dados[1] == cara.getTemBarba()
        case 4:
            return dados[1] == cara.getUsaOculos()
        case 5:
            return dados[1].upper() == cara.getNome().upper()

#play()