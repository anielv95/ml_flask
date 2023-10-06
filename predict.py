from flask import Flask
from flask import request
from flask import jsonify

def predict_single(input={
                    "oraciones": [
                    "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
                    "San Francisco considera prohibir los robots de entrega en la acera."
                    ]
            }):
    output = {
            "resultado": [
            {
            "oración": "Apple está buscando comprar una startup del Reino Unido por mil millonesde dólares.",
            "entidades": {
            "Apple": "ORG",
            "Reino Unido": "LOC",
            }
            },
            {
            "oración": "San Francisco considera prohibir los robots de entrega en la acera.",
            "entidades": {
            "San Francisco": "LOC"
            }
            }
            ]
            }
    return output

app = Flask("ner")

@app.route('/predict', methods=['POST']) 
def predict():
    customer = request.get_json()  

    prediction = predict_single(customer)

    return jsonify(prediction)  

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=8585)