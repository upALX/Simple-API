from flask import Flask,jsonify
import pandas as pd

app = Flask(__name__)

tableReaded = pd.read_csv('API-DATA.csv')

@app.route('/')
def singlePage():
    valuesSales = tableReaded['Vendas'].sum()
    valuesTV = tableReaded['TV'].sum()
    valuesRadio = tableReaded['Radio'].sum()
    valuesJornal = tableReaded['Jornal'].sum()
    return jsonify(
            'TV {}'.format(valuesTV),
            'Radio {}'.format(valuesRadio),
            'Jornal {}'.format(valuesJornal),
            'Vendas {}'.format(valuesSales))

app.run()