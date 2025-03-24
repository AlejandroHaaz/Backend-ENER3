from flask import Flask, request, jsonify
from flask_cors import CORS
from model import mongo, init_db
from config import Config

# Inicializar Flask y configuraciones
app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "*"}})

# Inicializar MongoDB
init_db(app)

# Endpoint para recibir información del formulario de contacto
@app.route('/contacto', methods=['POST'])
def contacto():
    data = request.get_json()

    # Validar que todos los campos requeridos estén presentes y no vacíos
    required_fields = ['nombre', 'apellido', 'email', 'telefono', 'estado']
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return jsonify({"msg": f"El campo '{field}' es obligatorio y no puede estar vacío"}), 400

    # Insertar los datos en MongoDB
    result = mongo.db.intparties.insert_one({
        "nombre": data['nombre'],
        "apellido": data['apellido'],
        "email": data['email'],
        "telefono": data['telefono'],
        "estado": data['estado'],
        "mensaje": data.get('mensaje', '')  # Campo opcional
    })

    if result.acknowledged:
        return jsonify({"msg": "Formulario enviado correctamente"}), 201
    else:
        return jsonify({"msg": "Error al enviar el formulario"}), 500

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
