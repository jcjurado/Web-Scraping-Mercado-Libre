from flask import Flask,jsonify, request
from functions import todosProductos, limite_producto

#AGREGADO
import json

app = Flask(__name__)
@app.route('/mercadoLibre',methods=['GET'])
def mercadoLibre():
    
    data = json.loads(request.data)
    print(data)
    if 'limite' not in data:

        titulos, urls,precios = todosProductos(data["producto"])
    else:
        titulos, urls,precios = limite_producto(data["producto"],data["limite"])
    # print(data,type(data))
    # print(data["producto"])
    
    return jsonify({"datos":{"titulos":titulos,"urls":urls,"precios":precios}})

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)