from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/pagar', methods=['POST'])
def pagar():
    data = request.get_json()
    numero_tarjeta = data.get('numero_tarjeta')
    monto = data.get('monto')
    nombre = data.get('nombre')
    codigo_CVV = data.get('codigo_CVV')
    
    saldo_disponible = 5000

    if numero_tarjeta == 123456789 and monto <= saldo_disponible:
        return jsonify({"resultado": True})
    else:
        return jsonify({"resultado": False})

@app.route('/comprar', methods=['POST'])
def comprar():
    data = request.get_json()
    id_producto = data.get('id_producto')
    precio = data.get('precio')
    numero_productos = data.get('numero_productos')
    total = data.get('total')

    if (precio * numero_productos) == total:
        return jsonify({"resultado": True})
    else:
        return jsonify({"resultado": False})

if __name__ == '__main__':
   
    app.run(port=5000, debug=True)