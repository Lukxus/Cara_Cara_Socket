import socket #importa modulo socket
 

def iniciaConexao():
    """TCP_IP = '192.168.100.14' # endereço IP do servidor 
    TCP_PORTA = 24000       # porta disponibilizada pelo servidor
    TAMANHO_BUFFER = 1024     # definição do tamanho do buffer"""
    count = 0
    while count == 0:
            # Criação de socket TCP
            # SOCK_STREAM, indica que será TCP.
            servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # IP e porta que o servidor deve aguardar a conexão
            servidor.bind((TCP_IP, TCP_PORTA))

            #Define o limite de conexões. 
            servidor.listen(1)
            # Aceita conexão 
            conn, addr = servidor.accept()
            print ('Endereço conectado:', addr)
            #dados retidados da mensagem recebida
            data = conn.recv(TAMANHO_BUFFER)
            if data: 
                print ("Mensagem recebida:", data)
                servidor.close()
                count = 1
                conn.send(data.upper())  # envia dados recebidos em letra maiuscula




    

    print("Servidor dispoivel na porta 5005 e escutando.....") 

    while 1:
        while count == 0:
            # Criação de socket TCP
            # SOCK_STREAM, indica que será TCP.
            servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # IP e porta que o servidor deve aguardar a conexão
            servidor.bind((TCP_IP, TCP_PORTA))

            #Define o limite de conexões. 
            servidor.listen(1)
            # Aceita conexão 
            conn, addr = servidor.accept()
            print ('Endereço conectado:', addr)
            #dados retidados da mensagem recebida
            data = conn.recv(TAMANHO_BUFFER)
            if data: 
                print ("Mensagem recebida:", data)
                servidor.close()
                count = 1
                conn.send(data.upper())  # envia dados recebidos em letra maiuscula

        while count == 1:
            MENSAGEM = input("Digite sua mensagem para o cliente: ")

            mensagemServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Conecta ao servidor em IP e porta especifica 
            mensagemServidor.connect((TCP_IP, TCP_PORTA))
            
            # envia mensagem para cliente 
            mensagemServidor.send(MENSAGEM.encode('UTF-8'))

            data1, addr = mensagemServidor.recvfrom(1024)

            mensagemServidor.close()
            count = 0
