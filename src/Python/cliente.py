import Front.pygamevisual
import Objetos.figuras
import Jogo.main
import connectionFactory.ClienteTCP
import socket #importa modulo socket


TCP_IP = '192.168.15.17' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024


def main():

    
    # Jogo

    #bloco de seleção da sua cara
    objetos = Objetos.figuras.gerando_caras()
    escolhido = None
    while escolhido == None:
        escolhido = Front.pygamevisual.escolhaCaras(objetos)

    while 1:
        # Inicia comunicação

        # Criação de socket TCP do cliente
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conecta ao servidor em IP e porta especifica 
        cliente.bind((TCP_IP, TCP_PORTA))
        #print(escolhido.getCorCabelo())
        recebe_pergunta = str(connectionFactory.ClienteTCP.recebe_cliente(cliente))
        recebe_pergunta = recebe_pergunta[2:-1]
        cliente.close()

        #envia
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conecta ao servidor em IP e porta especifica 
        cliente.connect((TCP_IP, TCP_PORTA))
        answer = Jogo.main.answer(eval(recebe_pergunta), escolhido)
        #eval converte uma string em tupla
        connectionFactory.ClienteTCP.envia_cliente(cliente, str(answer))
        ask = Jogo.main.ask()
        connectionFactory.ClienteTCP.envia_cliente(cliente, str(ask))
        cliente.close()

        #recebe
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conecta ao servidor em IP e porta especifica 
        cliente.bind((TCP_IP, TCP_PORTA))
        recebe_resp = connectionFactory.ClienteTCP.recebe_cliente(cliente)
        print(f"A resposta dada foi {recebe_resp}")
        cliente.close() # fecha a conexao
    

main()