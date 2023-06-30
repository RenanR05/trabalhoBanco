from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/carDatabase"
mongo = PyMongo(app)

@app.route('/marcas', methods=['POST'])
def create_marca():
    marca = request.json
    result = mongo.db.marcas.insert_one(marca)
    marca_id = result.inserted_id
    return jsonify({'message': 'Marca criada com sucesso', 'marca_id': str(marca_id)}), 201


@app.route('/marcas/<id>', methods=['GET'])
def get_marca(id):
    marca = mongo.db.marcas.find_one({'_id': ObjectId(id)})
    return jsonify(marca), 200

@app.route('/marcas', methods=['GET'])
def get_marcas():
    marcas = mongo.db.marcas.find()
    serialized_marcas = []
    for marca in marcas:
        marca['_id'] = str(marca['_id'])  # Converte ObjectId para string
        serialized_marcas.append(marca)
    return jsonify(serialized_marcas), 200


@app.route('/marcas/<id>', methods=['PUT'])
def update_marca(id):
    mongo.db.marcas.update_one({'_id': ObjectId(id)}, {'$set': request.json})
    return jsonify({'message': 'Marca atualizada com sucesso'}), 200

@app.route('/marcas/<id>', methods=['DELETE'])
def delete_marca(id):
    mongo.db.marcas.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Marca excluída com sucesso'}), 200

@app.route('/modelos', methods=['POST'])
def create_modelo():
    id = mongo.db.modelos.insert(request.json)
    return jsonify(str(ObjectId(id))), 201

@app.route('/modelos/<id>', methods=['GET'])
def get_modelo(id):
    modelo = mongo.db.modelos.find_one({'_id': ObjectId(id)})
    return jsonify(modelo), 200

@app.route('/modelos/<id>', methods=['PUT'])
def update_modelo(id):
    mongo.db.modelos.update_one({'_id': ObjectId(id)}, {'$set': request.json})
    return jsonify({'message': 'Modelo atualizado com sucesso'}), 200

@app.route('/modelos/<id>', methods=['DELETE'])
def delete_modelo(id):
    mongo.db.modelos.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Modelo excluído com sucesso'}), 200

@app.route('/carros', methods=['POST'])
def create_carro():
    id = mongo.db.carros.insert(request.json)
    return jsonify(str(ObjectId(id))), 201

@app.route('/carros/<id>', methods=['GET'])
def get_carro(id):
    carro = mongo.db.carros.find_one({'_id': ObjectId(id)})
    return jsonify(carro), 200

@app.route('/carros/<id>', methods=['PUT'])
def update_carro(id):
    mongo.db.carros.update_one({'_id': ObjectId(id)}, {'$set': request.json})
    return jsonify({'message': 'Carro atualizado com sucesso'}), 200

@app.route('/carros/<id>', methods=['DELETE'])
def delete_carro(id):
    mongo.db.carros.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Carro excluído com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)
