
from flask import Flask, request, abort, make_response
from flask_jsonpify import jsonify
from flask_cors import CORS
from collections import namedtuple
import json
import os
import ImovelRegister
import ImobiliariaRegister

version = '1.0'
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

def isNullOrEmpty(mystring):
    return not (mystring and mystring.strip())

#----------------- Imóveis -------------------------------#

@app.route("/api/v{0}/imoveis".format(version), methods=['GET'])
def get_imoveis():
    imoveis = ImovelRegister.list_imovel()
    return jsonify({'imoveis':imoveis})

@app.route("/api/v{0}/imoveis/<int:id>".format(version), methods=['GET'])
def get_imovel(id):
    imoveis = ImovelRegister.list_imovel(id)
    return jsonify({'imoveis':imoveis})

@app.route("/api/v{0}/imoveis/nome/<nome>".format(version), methods=['GET'])
def get_imovel_nome(nome):
    imoveis = ImovelRegister.list_imovel(id)
    return jsonify({'imoveis':imoveis})

@app.route("/api/v{0}/imoveis".format(version), methods=['POST'])
def create_imovel():    
    if not request.json or \
    (not 'nome' in request.json or isNullOrEmpty(str(request.json['nome']))) or \
    (not 'endereco' in request.json or isNullOrEmpty(str(request.json['endereco']))) or \
    (not 'descricao' in request.json or isNullOrEmpty(str(request.json['descricao']))) or \
    (not 'status' in request.json or isNullOrEmpty(str(request.json['status']))) or \
    (not 'tipo' in request.json or isNullOrEmpty(str(request.json['tipo']))) or \
    (not 'id_imobiliaria' in request.json or isNullOrEmpty(str(request.json['id_imobiliaria']))):
        fields = ['nome', 'endereco', 'descricao', 'status', 'tipo', 'id_imobiliaria']
        #fieldsInPost = [key for key, value in request.json]
        #fieldsNotFound = list(set(fields) - set(fieldsInPost))
        return make_response(jsonify({'erro': 'Os campos [{0}], são obrigatórios.'.format(', '.join(fields))}), 400)
    if not str(request.json['status']).lower() in ['ativo', 'inativo']:
        return make_response(jsonify({'erro': 'O campo [status] pode conter apenas os valores [ativo, inativo].'}), 400)
    if not str(request.json['tipo']).lower() in ['apartamento', 'casa']:
        return make_response(jsonify({'erro': 'O campo [tipo] pode conter apenas os valores [apartamento, casa].'}), 400)
    if 'finalidade' in request.json and (not str(request.json['finalidade']).lower() in ['residencial', 'escritório']):
        return make_response(jsonify({'erro': 'O campo [finalidade] pode conter apenas os valores [residencial, escritório].'}), 400)

    imovel = {
        'id': 0,
        'nome': request.json['nome'], 
        'endereco': request.json['endereco'], 
        'descricao': request.json['descricao'], 
        'status': request.json['status'].lower().capitalize(), 
        'caracteristicas': request.json.get('caracteristicas',"").lower().capitalize(), 
        'tipo': request.json['tipo'].lower().capitalize(), 
        'finalidade': request.json.get('finalidade',"").lower().capitalize(), 
        'id_imobiliaria': request.json['id_imobiliaria']
    }
    d_imovel = namedtuple("Imovel", imovel.keys())(*imovel.values())
    imovel['id'] = ImovelRegister.insert_imovel(d_imovel)
    return jsonify({'imovel': imovel}), 201

@app.route("/api/v{0}/imoveis".format(version), methods=['PUT'])
def update_imovel():
    if not request.json or \
    (not 'id' in request.json or isNullOrEmpty(str(request.json['id']))) or \
    (not 'nome' in request.json or isNullOrEmpty(str(request.json['nome']))) or \
    (not 'endereco' in request.json or isNullOrEmpty(str(request.json['endereco']))) or \
    (not 'descricao' in request.json or isNullOrEmpty(str(request.json['descricao']))) or \
    (not 'status' in request.json or isNullOrEmpty(str(request.json['status']))) or \
    (not 'tipo' in request.json or isNullOrEmpty(str(request.json['tipo']))) or \
    (not 'id_imobiliaria' in request.json or isNullOrEmpty(str(request.json['id_imobiliaria']))):
        fields = ['id', 'nome', 'endereco', 'descricao', 'status', 'tipo', 'id_imobiliaria']
        #fieldsInPost = [key for key, value in request.json]
        #fieldsNotFound = list(set(fields) - set(fieldsInPost))
        return make_response(jsonify({'erro': 'Os campos [{0}], são obrigatórios.'.format(', '.join(fields))}), 400)

    if not str(request.json['status']).lower() in ['ativo', 'inativo']:
        return make_response(jsonify({'erro': 'O campo [status] pode conter apenas os valores [ativo, inativo].'}), 400)
    if not str(request.json['tipo']).lower() in ['apartamento', 'casa']:
        return make_response(jsonify({'erro': 'O campo [tipo] pode conter apenas os valores [apartamento, casa].'}), 400)
    if 'finalidade' in request.json and (not str(request.json['finalidade']).lower() in ['residencial', 'escritório']):
        return make_response(jsonify({'erro': 'O campo [finalidade] pode conter apenas os valores [residencial, escritório].'}), 400)
    imovel = {
        'id': request.json['id'],
        'nome': request.json['nome'], 
        'endereco': request.json['endereco'], 
        'descricao': request.json['descricao'], 
        'status': request.json['status'], 
        'caracteristicas': request.json.get('caracteristicas',""), 
        'tipo': request.json['tipo'], 
        'finalidade': request.json.get('finalidade',""), 
        'id_imobiliaria': request.json['tipo']
    }
    d_imovel = namedtuple("Imovel", imovel.keys())(*imovel.values())
    # se não encontrar abort(404)
    imoveis = ImovelRegister.list_imovel(int(d_imovel.id))
    if imoveis == None or imoveis == []:
        abort(404)
    d_imovel = ImovelRegister.update_imovel(d_imovel)
    return jsonify({'imovel': imovel})

@app.route("/api/v{0}/imoveis/<int:id>".format(version), methods=['DELETE'])
def delete_imovel(id):
    imoveis = ImovelRegister.list_imovel(id)    
    if imoveis == None or imoveis == []:
        abort(404)
    idReturned = ImovelRegister.delete_imovel(id)
    return jsonify({
        'id': '{0}'.format(id),
        'excluido': '{0}'.format(bool(id == idReturned))
        })

#----------------- Imobiliária -------------------------------#

@app.route("/api/v{0}/imobiliaria".format(version), methods=['GET'])
def get_imobiliarias():
    imobiliarias = ImobiliariaRegister.list_imobiliaria()
    return jsonify({'imobiliarias':imobiliarias})

@app.route("/api/v{0}/imobiliaria/<int:id>".format(version), methods=['GET'])
def get_imobiliaria(id):
    imobiliarias = ImobiliariaRegister.list_imobiliaria(id)
    return jsonify({'imobiliarias':imobiliarias})

@app.route("/api/v{0}/imobiliaria/nome/<nome>".format(version), methods=['GET'])
def get_imobiliaria_nome(nome):
    imobiliarias = ImobiliariaRegister.list_imobiliaria(nome=nome)
    return jsonify({'imobiliarias':imobiliarias})

@app.route("/api/v{0}/imobiliaria".format(version), methods=['POST'])
def create_imobiliaria():    
    if not request.json or \
    (not 'nome' in request.json or isNullOrEmpty(str(request.json['nome']))):
        fields = ['nome']
        return make_response(jsonify({'erro': 'Os campos [{0}], são obrigatórios.'.format(', '.join(fields))}), 400)

    imobiliaria = {
        'id': 0,
        'nome': request.json['nome'], 
        'endereco': request.json['endereco']
    }
    d_imobiliaria = namedtuple("Imobiliaria", imobiliaria.keys())(*imobiliaria.values())
    imobiliaria['id'] = ImobiliariaRegister.insert_imobiliaria(d_imobiliaria)
    return jsonify({'imobiliaria': imobiliaria}), 201

@app.route("/api/v{0}/imobiliaria".format(version), methods=['PUT'])
def update_imobiliaria():
    if not request.json or \
    (not 'nome' in request.json or isNullOrEmpty(str(request.json['nome']))):
        fields = ['nome']
        return make_response(jsonify({'erro': 'Os campos [{0}], são obrigatórios.'.format(', '.join(fields))}), 400)

    imobiliaria = {
        'id': request.json['id'],
        'nome': request.json['nome'], 
        'endereco': request.json['endereco']
    }
    d_imobiliaria = namedtuple("Imobiliaria", imobiliaria.keys())(*imobiliaria.values())
    # se não encontrar abort(404)
    imobiliarias = ImobiliariaRegister.list_imobiliaria(int(d_imobiliaria.id))
    if imobiliarias == None or imobiliarias == []:
        abort(404)
    d_imobiliaria = ImobiliariaRegister.update_imobiliaria(d_imobiliaria)
    return jsonify({'imovel': imobiliaria})

@app.route("/api/v{0}/imobiliaria/<int:id>".format(version), methods=['DELETE'])
def delete_imobiliaria(id):
    imoveis = ImobiliariaRegister.list_imobiliaria(id)    
    if imoveis == None or imoveis == []:
        abort(404)
    idReturned = ImobiliariaRegister.delete_imobiliaria(id)
    return jsonify({
        'id': '{0}'.format(id),
        'excluido': '{0}'.format(bool(id == idReturned))
        })

#-------------------- Comuns ---------------------------------#

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'erro': 'Não encontrado!'}), 404)

@app.errorhandler(405)
def method_not_found(error):
    return make_response(jsonify({'erro': 'Método não encontrado!'}), 405)

if __name__ == '__main__':
    app.run(port='5002')