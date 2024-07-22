# Projeto de Redes: Jogo de Perguntas e Respostas

## Descrição

Este projeto foi desenvolvido na disciplina de Redes da Universidade Presbiteriana Mackenzie. O objetivo do projeto é implementar um protocolo de comunicação para troca de informações entre dois nós utilizando o protocolo Socket. A aplicação desenvolvida é um jogo de perguntas e respostas onde dois jogadores competem para adivinhar a imagem do adversário antes que sua própria imagem seja descoberta.

## Objetivo do Jogo

O jogo consiste em fazer perguntas ao adversário sobre características visuais de uma imagem. Cada jogador possui uma imagem oculta e deve tentar adivinhar a imagem do oponente com base nas respostas às suas perguntas. O primeiro jogador a adivinhar corretamente a imagem do adversário vence o jogo.

## Funcionalidades

- Comunicação em tempo real entre dois jogadores utilizando o protocolo Socket.
- Interface gráfica desenvolvida com Pygame para escolha de características e imagens.
- Sistema de perguntas e respostas com diferentes características visuais.

## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

- **main.py**: Contém a lógica principal do jogo.
- **cliente.py**: Implementa o cliente que se conecta ao servidor.
- **host.py**: Implementa o servidor que aceita conexões de clientes.
- **pygamevisual.py**: Contém a interface gráfica para seleção de características e imagens.
- **figura.py**: Contém a geração das imagens e suas características.

## Como Executar

### Pré-requisitos

- Python 3.x
- Bibliotecas: pygame

### Passos para Executar

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone <URL do repositório>

2. Navegue até o diretório do projeto:
3. Instale as dependências necessárias: pip install pygame
4.Configure os endereços IP no cliente.py e host.py de acordo com a sua rede.
5.Execute o servidor:python host.py
Execute o cliente em outro terminal ou máquina: python cliente.py
