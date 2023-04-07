import pickle
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, url_for



# Initialiser l'application Flask
app = Flask(__name__)
# Charger le modèle pré-entrainé
model = pickle.load(open("diab.pkl", "rb"))

# Route pour la page d'accueil avec la visualisation de graphiques
@app.route('/')
def home():
    # Générer l'URL de l'image à l'aide de url_for
    image_url = url_for('static', filename='image/IA.jpeg')
    # Rendre le template HTML avec le graphique en arrière-plan
    return render_template('home1.html', image_url = image_url)


# Route pour la page de prédiction avec le formulaire
@app.route('/predict', methods=['POST'])
def predict():
    # Si la méthode est POST, cela signifie qu'un formulaire a été soumis
    # Récupérer les entrées de l'utilisateur
    if request.method == 'POST':
        age = request.form['age']
        gendera = request.form['gendera']
        BMI = request.form['BMI']    
        depression = request.form['depression']
        temperature = request.form['temperature']
        
        
        # Prétraiter les données d'entrée et les convertir en un tableau numpy utilisable pour la prédiction
        input_array = [age, gendera, BMI, depression, temperature]
        input_array = np.array(input_array).reshape(1, -1)
        
        # Effectuer la prédiction à l'aide du modèle
        prediction = model.predict(input_array)
        
        # Retourner la prédiction sous forme de réponse HTML
        result = 'Le résultat de votre recherche est : ' + str(prediction[0])
        if prediction[0]==0:
            pred = " Vous n'est pas atteint du diabete"
        else:
            pred = "Vous avez le Diabete"
        
        return render_template('result.html',result = pred)
    else:
        render_template('home1.html')
        
    

# Exécuter l'application Flask sur un serveur local
if __name__ == '__main__':
    app.run(debug=True)
