import Front.pygamevisual
import Objetos.figuras
import Jogo.main


def main():
    #bloco de seleção da sua cara
    objetos = Objetos.figuras.gerando_caras()
    escolhido = Front.pygamevisual.escolhaCaras(objetos)
    #print(escolhido.getCorCabelo())
    ask = Jogo.main.ask()
    print(ask)
    print(Jogo.main.answer(ask, escolhido))

    
main()