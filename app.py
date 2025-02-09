from flask import Flask, render_template
import json

app = Flask(__name__)

with open('./inventory.json', encoding="utf-8") as json_file:
    parsed_json = json.load(json_file)

def extract_data(json_data):
    extracted_data = {}
    for guitar in json_data['guitars']:
        extracted_data[guitar['id']] = {
            'id': guitar['id'],
            'make': guitar['make'],
            'model': guitar['model'],
            'color': guitar['color'],
            'strings': guitar['strings'],
            'notes': guitar['notes'],
            'shape': guitar['shape'],
            'value': guitar['value'],
            'pickups': guitar['pickups'],
            'year': guitar['year'],
            'picture': guitar['picture'],
            'purchased': guitar['purchased'],
            'serial_number': guitar['serial_number'],
        }
    return extracted_data

guitars_dict = extract_data(parsed_json)

@app.route('/')
def display_data():
    return render_template('home.html', guitars=guitars_dict)

if __name__ == '__main__':
    app.run(debug=True)