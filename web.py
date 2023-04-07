from flask import Flask, request, jsonify
import numpy as np
import pickle

# Charger le modèle pré-entrainé
model = pickle.load(open("class_dia.pkl", "rb"))

# Initialiser l'application Flask
app = Flask(__name__)

# Définir la route principale pour la prédiction
@app.route('/predict',methods=['POST'])
def predict():
    # Récupérer les entrées de l'utilisateur
    inputs = request.get_json(force=True)
    
    # Prétraiter les données d'entrée et les convertir en un tableau numpy utilisable pour la prédiction
    input_array = [inputs['outcome'], inputs['age'], inputs['gendera'], inputs['BMI'], inputs['hypertensive'],
                    inputs['atrialfibrillation'], inputs['deficiencyanemias'], inputs['depression'], inputs['temperature'], inputs['Urine output']]
    input_array = np.array(input_array).reshape(1, -1)
    
    # Effectuer la prédiction à l'aide du modèle
    prediction = model.predict(input_array)
    
    # Retourner la prédiction sous forme de réponse JSON
    output = {'prediction': int(prediction[0])}
    return jsonify(output)

# Exécuter l'application Flask sur un serveur local
if __name__ == '__main__':
    app.run(debug=True)
