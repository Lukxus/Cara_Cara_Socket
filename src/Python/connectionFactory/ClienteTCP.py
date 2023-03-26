#import socket #importa modulo socket

TCP_IP = '192.168.15.17' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024
MENSAGEM = ''
count = 0

def envia_cliente(conexao, valor): #valor tem que ser uma string
    while count == 0:
        """# Criação de socket TCP do cliente
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conecta ao servidor em IP e porta especifica 
        cliente.connect((TCP_IP, TCP_PORTA))"""

        # envia mensagem para servidor 
        conexao.send(valor.encode('UTF-8'))

        # recebe dados do servidor 
        data, addr = conexao.recvfrom(1024)
        print ("received data:", data)
        
        # fecha conexão com servidor
        """conexao.close()
        count = 1"""

def recebe_cliente(conexao):
    while count == 1:
        """clienteRecebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clienteRecebe.bind((TCP_IP, TCP_PORTA))"""
        conexao.listen(1)
        # Aceita conexão 
        conn, addr1 = conexao.accept()
        print ('Endereço conectado:', addr1)
        #dados retidados da mensagem recebida
        info = conn.recv(TAMANHO_BUFFER)
        if info: 
            print ("Mensagem recebida:", info)
            conn.send(info.upper())

        """conexao.close()
        count = 0"""
