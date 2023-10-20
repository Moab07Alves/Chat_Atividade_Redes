import requests
import os

SERVIDOR_URL = 'http://127.0.0.1:5555'


def enviar_mensagem():
    nome_usuario = input("Digite o seu nome de usuário: ")
    msg = input("Digite sua mensagem: ")
    resposta = requests.post(f'{SERVIDOR_URL}/enviar', json={'nome': nome_usuario, 'mensagem': msg})
    print(resposta.json()['status'])
    os.system('clear' if os.name == 'posix' else 'cls')
    receber_mensagens()


def receber_mensagens():
    print("------------------------------------------------")
    resposta = requests.get(f'{SERVIDOR_URL}/receber')
    mensagens = resposta.json()['mensagens']
    print("Conversa:")
    for msg in mensagens:
        print(f"- {msg['nome']}: {msg['mensagem']}")
    print("------------------------------------------------\n")

if __name__ == '__main__':
    while True:
        print("1. Enviar mensagem")
        print("2. Receber mensagens")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            os.system('clear' if os.name == 'posix' else 'cls')
            enviar_mensagem()
        elif escolha == '2':
            os.system('clear' if os.name == 'posix' else 'cls')
            receber_mensagens()
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")
