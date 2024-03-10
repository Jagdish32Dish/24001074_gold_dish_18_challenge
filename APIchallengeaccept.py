import re
import pandas as pd
import challengeaccepted as ca
from flask import Flask, jsonify
import databasechallenge as dbc
# flask
app = Flask(__name__)

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from



# swagerr
app.json_encoder = LazyJSONEncoder
swagger_template = {
    "info": {
        "title":  "API Documentation for Data Processing and Modeling",
        "version": "1.0.0",
        "description": "Dokumentasi API"
    },
    "host": "127.0.0.1:5000"
}
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json',
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)

##body api
@swag_from("docs/text_processing.yml", methods=['POST'])
@app.route('/text-processing', methods=['POST'])
def text_processing():

    text = request.form.get('text')
    text_cleaned = ca.cleandata(text)

    json_response = {
        'status_code': 200,
        'description': "Teks yang sudah diproses",
        'data': text_cleaned,
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text_processing_file.yml", methods=['POST'])
@app.route('/text-processing-file', methods=['POST'])
def text_processing_file():

    # Upladed file
    file = request.files.getlist('file')[0]

    # Import file csv ke Pandas
    df = pd.read_csv(file, encoding='ISO-8859-1')
    df['aftercleansed']=df['Tweet'].apply(ca.cleandata)
    df_result=df[['Tweet', 'aftercleansed']]
    # ambil text dalam format list
    texts = df['aftercleansed'].values.tolist()
    dbc.import_db(df_result)

    json_response = {
        'status_code': 200,
        'description': "Teks yang sudah diproses",
        'data': texts,
    }

    response_data = jsonify(json_response)
    return response_data

##running api
if __name__ == '__main__':
   app.run()

