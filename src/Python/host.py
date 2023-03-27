import Front.pygamevisual
import Objetos.figuras
import Jogo.main
import connectionFactory.ClienteTCP
import socket


TCP_IP = '192.168.15.17' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024


def main():

    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    escolhido = None
    objetos = Objetos.figuras.gerando_caras()
    while escolhido == None:
        escolhido = Front.pygamevisual.escolhaCaras(objetos)

    while 1:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.connect((TCP_IP, TCP_PORTA))
        conexao.listen(1) 
        conn, addr1 = conexao.accept()
        ask = Jogo.main.ask()
        connectionFactory.ClienteTCP.envia_cliente(conexao, str(ask))
        recebe_resp = connectionFactory.ClienteTCP.recebe_cliente(conexao)
        print(f'Resposta: {recebe_resp}')
        recebe_pergunta = str(connectionFactory.ClienteTCP.recebe_cliente(conexao))
        answer = Jogo.main.answer(eval(recebe_pergunta), escolhido)
        connectionFactory.ClienteTCP.envia_cliente(conexao, str(answer))

    conexao.close() # fecha a conexao

main()