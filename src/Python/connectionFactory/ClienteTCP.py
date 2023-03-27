#import socket #importa modulo socket
"""
TCP_IP = '192.168.15.17' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
MENSAGEM = ''
count = 0"""
TAMANHO_BUFFER = 1024

def envia_cliente(conexao, valor): #valor tem que ser uma string
    conexao.sendall(valor.encode("UTF-8"))


def recebe_cliente(conexao):
    while True:
        data = conexao.recv(1024)
        if data:
            return data
