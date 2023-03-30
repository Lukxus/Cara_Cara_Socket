import Front.pygamevisual
import Objetos.figuras
import Jogo.main
import socket #importa modulo socket

#luiz:  192.168.15.14
#leonardo: 192.168.100.14

TCP_IP = '192.168.100.14' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024
caras = Objetos.figuras.gerando_caras()
escolhido = Front.pygamevisual.escolhaCaras(caras)

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((TCP_IP, TCP_PORTA))
    print(f"A sua cara é {escolhido.getNome()}")
    while cliente:
        data, addr = cliente.recvfrom(1024)
        #print(data.decode())
        data = data.decode()
        resposta_host = (str(Jogo.main.answer(eval(data), escolhido)))
        cliente.send(resposta_host.encode())
        if (resposta_host == "True" and data[1] == "5"):
            print("\nVoce perdeu!!!")
            break
        elif(resposta_host == "False" and data[1] == "5"):
            print("\nVoce ganhou!!!")
            break
        pergunta = Jogo.main.ask(caras)
        cliente.send(str(pergunta).encode())
        resposta = cliente.recv(1024).decode()
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
    cliente.close()
        
main()