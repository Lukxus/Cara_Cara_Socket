import Front.pygamevisual
import Objetos.figuras
import Jogo.main
import connectionFactory.ClienteTCP
import socket


TCP_IP = '192.168.15.17' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024


def main():


    # Jogo
    escolhido = None
    objetos = Objetos.figuras.gerando_caras()

    while escolhido == None:
        #bloco de seleção da sua cara
        escolhido = Front.pygamevisual.escolhaCaras(objetos)


    while 1:
        # Inicia comunicação

        # Criação de socket TCP do cliente
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conecta ao servidor em IP e porta especifica 
        cliente.connect((TCP_IP, TCP_PORTA))
        ask = Jogo.main.ask()
        #print(ask)
        #print(str(ask))
        connectionFactory.ClienteTCP.envia_cliente(cliente, str(ask))
        cliente.close()

        #recebe
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        cliente.bind((TCP_IP, TCP_PORTA))

        recebe_resp = connectionFactory.ClienteTCP.recebe_cliente(cliente)
        print(f"A resposta dada foi {bool(recebe_resp)}")
        #print(escolhido.getCorCabelo())
        recebe_pergunta = str(connectionFactory.ClienteTCP.recebe_cliente(cliente))
        answer = Jogo.main.answer(eval(recebe_pergunta), escolhido)
        #eval converte uma string em tupla
        cliente.close()

        #envia
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conecta ao servidor em IP e porta especifica 
        cliente.connect((TCP_IP, TCP_PORTA))
        connectionFactory.ClienteTCP.envia_cliente(cliente, str(answer))
        cliente.close() # fecha a conexao

    
main()