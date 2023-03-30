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
        pergunta = Jogo.main.ask(caras)
        conn.send(str(pergunta).encode())
        resposta = conn.recv(1024).decode()
        if (pergunta[0] == 5 and resposta == "True"):
            print("\nVoce ganhou!!!")
            break
        elif(pergunta[0] == 5 and resposta == "False"):
            print("\nVoce perdeu!!!")
            break
        if resposta == "True":
            print(f"\nA resposta para a sua pergunta foi: Verdadeiro")
        elif resposta == "False":
            print(f"\nA resposta para a sua pergunta foi: Falso")
        pergunta_cliente = conn.recv(1024).decode()
        reposta_cliente = str(Jogo.main.answer(eval(pergunta_cliente), escolhido))
        conn.send(reposta_cliente.encode())
        if (reposta_cliente == "True" and pergunta_cliente[1] == "5"):
            print("\nVoce perdeu!!!")
            break
        elif(reposta_cliente == "False" and pergunta_cliente[1] == "5"):
            print("\nVoce ganhou!!!")
            break
    host.close()
    
main()