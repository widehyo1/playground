from flask import Flask, jsonify, request
import lxc

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def list_containers():
    containers = lxc.list_containers()
    return jsonify({"containers": containers})

@app.route('/build', methods=['POST'])
def build():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    
    name = data.get('name')
    container = lxc.Container(name)
    payload = dict(**data)
    payload.pop('name')
    if not container.defined:
        if container.create('download', 0, payload):
            return jsonify({'message': 'container created'})
        else:
            return jsonify({'message': 'creation failed'})
    else:
        return jsonify({"message": "container already exists"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
