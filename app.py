from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Métriques : Températures à Paris
data_paris = [
    {"heure": "08:00", "temp": 12},
    {"heure": "10:00", "temp": 14},
    {"heure": "12:00", "temp": 18},
    {"heure": "14:00", "temp": 20},
    {"heure": "16:00", "temp": 19},
    {"heure": "18:00", "temp": 15}
]

@app.route('/')
def index():
    # Envoie vers le fichier HTML dans le dossier templates
    return render_template('graphique.html')

@app.route('/api/paris')
def api_paris():
    # Envoie les données au format JSON pour le graphique
    return jsonify(data_paris)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
