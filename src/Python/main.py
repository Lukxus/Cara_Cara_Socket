import Front.pygamevisual
import Objetos.figuras


def main():
    #bloco de seleção da sua cara
    objetos = Objetos.figuras.gerando_caras()
    escolhido = Front.pygamevisual.escolhaCaras(objetos)
    print(escolhido.getCorCabelo())

    
main()