from flask import Flask, request, jsonify
from flask_cors import CORS
import resend
import traceback

app = Flask(__name__)
CORS(app)

resend.api_key = "re_WiVtwy4L_6DxvdwUudyrpfiDXsK7rmdTx"
@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    dados = request.json
    nome = dados.get('nome')
    email = dados.get('email')

    try:
        email_enviado = resend.Emails.send({
            "from": "Equipe do projeto <onboarding@resend.dev>",
            "to": [email],
            "subject": "Confirmação de Cadastro",
            "html": f"<h2>Olá, {nome}!</h2><p>Seu cadastro foi realizado com sucesso</p>"
        })
        return jsonify({"mensagem": "Email enviado com sucesso!"}), 200
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"Erro": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)

