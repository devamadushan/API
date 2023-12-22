from flask import Flask, render_template, request, jsonify, url_for
import requests





app = Flask(__name__)


# country = input("lr nom de la vile :")


# try:
#
#     print(json)
#     print(json['name']['official'])
# except Exception as e:
#     print(f"Une erreur s'est produite : {e}")


@app.route('/')
def index():
    try:
        api_lien = "https://restcountries.com/v3.1/all"
        json_data = requests.get(api_lien).json()
        print(json_data)
        return render_template('index.html', info=json_data)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return "Erreur lors de la récupération des données depuis l'API."


@app.route('/pays')
def pays():
    api_lien = "https://restcountries.com/v3.1/all"
    json_data = requests.get(api_lien).json()
    return render_template('lesPays.html', info=json_data)


@app.route('/rechercher', methods=['POST'])
def rechercher():
    recherche = request.form['recherchePays']
    api_lien = f"https://restcountries.com/v3.1/name/{recherche}"
    json_data = requests.get(api_lien).json()
    print(json_data)
    return render_template('rechercheParPays.html', info=json_data)

@app.route('/rechercher/<nom>')
def rechercherpays(nom):

    api_lien = f"https://restcountries.com/v3.1/name/{nom}"
    json_data = requests.get(api_lien).json()
    print(nom)
    print(json_data)
    return render_template('rechercheParPays.html', info=json_data)

if __name__ == '__main__':
    app.run(debug=True)
