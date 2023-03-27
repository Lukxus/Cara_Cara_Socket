import Front.pygamevisual
import Objetos.figuras
import Jogo.main
import connectionFactory.ClienteTCP
import socket #importa modulo socket


TCP_IP = '192.168.15.17' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024


def main():

    
    objetos = Objetos.figuras.gerando_caras()
    escolhido = None
    while escolhido == None:
        escolhido = Front.pygamevisual.escolhaCaras(objetos)

    while 1:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        cliente.connect((TCP_IP, TCP_PORTA))
        recebe_pergunta = str(connectionFactory.ClienteTCP.recebe_cliente(cliente))
        #recebe_pergunta = recebe_pergunta[2:-1]
        answer = Jogo.main.answer(eval(recebe_pergunta), escolhido)
        connectionFactory.ClienteTCP.envia_cliente(cliente, str(answer))
        ask = Jogo.main.ask()
        connectionFactory.ClienteTCP.envia_cliente(cliente, str(ask))
        cliente.close()
        recebe_resp = connectionFactory.ClienteTCP.recebe_cliente(cliente)
        
    cliente.close() # fecha a conexao

main()