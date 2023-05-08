from datetime import datetime
from flask import Flask, make_response, jsonify, request
from dadosjsonpy import rotas
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/rotas', methods=['GET'])
def get_rotas():
    return make_response(jsonify(rotas))

@app.route('/rotas_saida', methods=['POST'])
def get_rotas_saida():
    if request.headers['Content-Type'] == 'application/json':
        content = request.json
        value1 = content['local']
        value2 = content['horario']

        aprovados = []
        for rota in rotas:
            saida_datetime = datetime.strptime(rota["saida"], "%H:%M:%S")  # Convert "saida" string to datetime object
            x_datetime = datetime.strptime(value2, "%H:%M:%S")  # Convert "x" string to datetime object
            if saida_datetime < x_datetime:
                aprovados.append(rota)

    return make_response(jsonify(aprovados))

@app.route('/rotas_completa', methods=['POST'])
def get_rotas_completa():
    if request.headers['Content-Type'] == 'application/json':
        content = request.json
        value1 = content['local_saida']
        value2 = content['local_chegada']

        aprovados = []
        for rota in rotas:
            if rota["local_saida"] == value1 and rota["local_chegada"] == value2:
                aprovados.append(rota)

    return make_response(jsonify(aprovados))

@app.route('/rotas_tipo', methods=['POST'])
def get_rotas_tipo():
    if request.headers['Content-Type'] == 'application/json':
        content = request.json
        value1 = content['tipo']

        aprovados = []
        for rota in rotas:
            if rota["tipo"] == value1:
                aprovados.append(rota)

    return make_response(jsonify(aprovados))

@app.route('/origens', methods=['GET'])
def get_origens():
    aprovados = []
    for rota in rotas:
        aprovados.append(rota["origem"])

    return make_response(jsonify(aprovados))

@app.route('/destino_origens', methods=['POST'])
def get_destino_origens():
    if request.headers['Content-Type'] == 'application/json':
        content = request.json
        value1 = content['origem']

        aprovados = []
        for rota in rotas:
            print(rota)
            if rota['origem'] == value1:
                aprovados.append(rota)

    return make_response(jsonify(aprovados))



def create_app():
   return app

#START ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#START ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#START ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    print("A")
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()