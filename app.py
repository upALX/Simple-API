from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

tableReaded = pd.read_csv('API-DATA.csv')


@app.route('/')
def index():
    welc = 'Welcome to simple API (this is not endpoint)'
    return welc

@app.route('/dataSales')
def dataSales():
    valuesSales = tableReaded['Vendas'].sum()
    return jsonify('Vendas {}'.format(valuesSales))

@app.route('/dataTV')
def dataTV():
    valuesTV = tableReaded['TV'].sum()
    return jsonify('TV {}'.format(valuesTV))

@app.route('/dataRadio')
def dataRadio():
    valuesRadio = tableReaded['Radio'].sum()
    return jsonify('Radio {}'.format(valuesRadio))

@app.route('/dataJornal')
def dataJournal():
    valuesJornal = tableReaded['Jornal'].sum()
    return jsonify('Jornal {}'.format(valuesJornal))

app.run()
