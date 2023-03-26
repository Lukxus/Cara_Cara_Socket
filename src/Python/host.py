import Front.pygamevisual
import Objetos.figuras
import Jogo.main
import connectionFactory.ClienteTCP
import socket


TCP_IP = '192.168.100.14' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024


def main():

    # Inicia comunicação

    # Criação de socket TCP do cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta ao servidor em IP e porta especifica 
    cliente.connect((TCP_IP, TCP_PORTA))

    # Jogo

    #bloco de seleção da sua cara
    objetos = Objetos.figuras.gerando_caras()
    escolhido = Front.pygamevisual.escolhaCaras(objetos)
    ask = Jogo.main.ask()
    connectionFactory.ClienteTCP.envia_cliente(ask)
    recebe_resp = connectionFactory.ClienteTCP.recebe_cliente(cliente)
    print(f"A resposta dada foi {bool(recebe_resp)}")
    #print(escolhido.getCorCabelo())
    recebe_pergunta = connectionFactory.ClienteTCP.recebe_cliente(cliente)
    answer = Jogo.main.answer(eval(recebe_pergunta), escolhido)
    #eval converte uma string em tupla
    connectionFactory.ClienteTCP.envia_cliente(answer)


    cliente.close() # fecha a conexao

    
main()