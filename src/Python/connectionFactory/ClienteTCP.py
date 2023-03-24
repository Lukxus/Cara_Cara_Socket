import socket #importa modulo socket

TCP_IP = '192.168.100.14' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024
MENSAGEM = ''
count = 0

while 1:
    while count == 0:
        MENSAGEM = input("Digite sua mensagem para o servidor: ")

        # Criação de socket TCP do cliente
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conecta ao servidor em IP e porta especifica 
        cliente.connect((TCP_IP, TCP_PORTA))

        # envia mensagem para servidor 
        cliente.send(MENSAGEM.encode('UTF-8'))

        # recebe dados do servidor 
        data, addr = cliente.recvfrom(1024)
        print ("received data:", data)
        
        # fecha conexão com servidor
        cliente.close()
        count = 1

    while count == 1:
        clienteRecebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clienteRecebe.bind((TCP_IP, TCP_PORTA))
        clienteRecebe.listen(1)
        # Aceita conexão 
        conn, addr1 = clienteRecebe.accept()
        print ('Endereço conectado:', addr1)
        #dados retidados da mensagem recebida
        info = conn.recv(TAMANHO_BUFFER)
        if info: 
            print ("Mensagem recebida:", info)
            conn.send(info.upper())

        clienteRecebe.close()
        count = 0
