import Front.pygamevisual
import Objetos.figuras
import Jogo.main
import socket

#luiz:  192.168.15.14
#leornardo: 192.168.100.14

TCP_IP = '192.168.15.14' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024
caras = Objetos.figuras.gerando_caras()
escolhido = Front.pygamevisual.escolhaCaras(caras)


def main():
    host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host.bind((TCP_IP, TCP_PORTA))
    host.listen(1)
    conn, addr = host.accept()
    print(f"A sua cara é {escolhido.getNome()}")
    while addr:
        pergunta = Jogo.main.ask()
        conn.send(str(pergunta).encode())
        resposta = conn.recv(1024)
        print(f"\n A resposta para a sua pergunta foi:{resposta}")
        pergunta_cliente = conn.recv(1024)
        print(pergunta_cliente)
        conn.send(str(Jogo.main.answer(eval(pergunta_cliente), escolhido)).encode())
            
    host.close()
    
main()
