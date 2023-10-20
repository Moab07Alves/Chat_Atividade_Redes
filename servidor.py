from flask import Flask, request, jsonify

app = Flask(__name__)

mensagens = []
id_contador = 1

@app.route('/enviar', methods=['POST'])
def enviar():
    global id_contador
    msg = request.json.get('mensagem')
    nome = request.json.get('nome')
    if msg:
        mensagem = {
            'id': id_contador,
            'mensagem': msg,
            'nome': nome
        }
        id_contador += 1
        mensagens.append(mensagem)
        print(f" - {mensagem['nome']} : {mensagem['mensagem']} ({mensagem['id']})")
        return jsonify({'status': 'Mensagem enviada', 'id': mensagem['id']}), 200
    return jsonify({'status': 'Erro ao enviar mensagem'}), 400

@app.route('/receber', methods=['GET'])
def receber():
    last_id = int(request.args.get('last_id', 0))
    mensagens_a_enviar = [mensagem for mensagem in mensagens if mensagem['id'] > last_id]
    return jsonify({'mensagens': mensagens_a_enviar})

if __name__ == '__main__':
    app.run(debug=True, port=5555)

